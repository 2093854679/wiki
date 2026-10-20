import json
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, Mock

from click.testing import CliRunner

from tools.kb.retrieval import passages, query_plan
from tools.kb.retrieval_engine import SearchEngine, cmd_search, cmd_context, read_document


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.raw, self.wiki = self.root / "raw", self.root / "wiki"
        self.raw.mkdir()
        self.wiki.mkdir()
        self.cfg = {"paths": {"raw_dir": str(self.raw), "wiki_dir": str(self.wiki), "search_db": str(self.root / "search.db")}}
        self.config_patch = patch("tools.kb.retrieval_engine.get_config", return_value=self.cfg)
        self.config_patch.start()
        for chip, side, version in [("BK7236", "", "v2.0.1"), ("BK7258", "AP", "v3.1.1"), ("BK7259", "AP", "v4.0.1"), ("BK7259", "CP", "v4.0.1")]:
            name = f"{chip}-{side or 'base'}"
            self.write(self.raw / name / "uart.md", f"---\nchip: {chip}\nsdk_family: bk_avdk_smp\nsdk_version: {version}\nprocessor: {side or 'null'}\nmirror_status: current\n---\n# UART 串口使用指南\n\nUART initialization 初始化。\n\n## 中断接收\nUART receive RX interrupt callback.\n")
        self.write(self.raw / "old.md", "---\nchip: BK7236\nmirror_status: historical-unverified\n---\n# UART 历史旧版\nUART serial initialization.\n")
        self.write(self.raw / "shared.md", "---\nchip: BK7235,BK7258\nsdk_family: bk_matter\nsdk_version: v2.0.1\n---\n# Matter Controller\nMatter commissioning 配网。\n")
        late = "---\nchip: BK7236\nsdk_family: bk_idk\nsdk_version: v2.0.1\n---\n# WiFi API\n\n" + "Unrelated introduction text.\n" * 500
        late += '<a id="wifi-start"></a>\n## bk\\_wifi\\_sta\\_start\n\nCall bk\\_wifi\\_sta\\_start() after configuration.\nReturns BK_OK.\n'
        self.write(self.raw / "wifi.md", late)
        self.write(self.wiki / "concepts/memory.md", "# FreeRTOS 内存管理\n\n任务栈不足、stack overflow、溢出需要检查任务栈和 heap。\n")
        self.write(self.wiki / "summaries/uart.md", "> **Source:** [UART](../../raw/BK7236-base/uart.md)\n# UART 简介\nUART initialization 初始化。\n")
        self.write(self.wiki / "outputs/old-audit.md", "# UART 历史审计\nUART 初始化 错误记录。\n")
        self.engine = SearchEngine(self.root / "search.db")
        self.engine.index(self.wiki, self.raw)

    def tearDown(self):
        self.config_patch.stop()
        self.temp.cleanup()

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")

    def test_chinese_question_matches_and_never_switches_chip(self):
        rows = self.engine.search("BK7236串口初始化怎么做", limit=5)
        self.assertTrue(rows)
        self.assertTrue(all(all(s["chip"] == "BK7236" for s in r["matching_scopes"]) for r in rows))
        self.assertFalse(any(r["status"] == "historical-unverified" for r in rows))

    def test_strict_processor_and_version(self):
        rows = self.engine.search("BK7259 AP 的 UART 接口", family="bk_avdk_smp", version="v4.0.1")
        self.assertTrue(rows)
        self.assertEqual({s["processor"] for r in rows for s in r["matching_scopes"]}, {"AP"})
        self.assertFalse(self.engine.search("BK7259 UART", processor="AP", version="v3.1.1"))

    def test_api_symbol_returns_late_original_lines(self):
        rows = self.engine.search("bk_wifi_sta_start", chip="BK7236")
        self.assertTrue(rows)
        self.assertEqual(rows[0]["workspace_path"], "raw/wifi.md")
        self.assertGreater(rows[0]["start_line"], 400)
        self.assertIn("bk_wifi_sta_start", rows[0]["snippet"])
        evidence = read_document(rows[0]["workspace_path"], rows[0]["start_line"], rows[0]["end_line"])
        self.assertIn("sta\\_start", evidence["content"])

    def test_chinese_task_stack_query(self):
        rows = self.engine.search("FreeRTOS 任务栈不足怎么办")
        self.assertEqual(rows[0]["path"], "concepts/memory.md")

    def test_shared_chip_document_is_not_dropped(self):
        rows = self.engine.search("Matter 配网", chip="BK7258", family="bk_matter")
        self.assertEqual(rows[0]["workspace_path"], "raw/shared.md")

    def test_summary_inherits_exact_source_scope(self):
        rows = self.engine.search("UART 初始化", chip="BK7236", kind="summary")
        self.assertTrue(rows)
        self.assertEqual(rows[0]["matching_scopes"][0]["chip"], "BK7236")

    def test_historical_and_outputs_require_explicit_request(self):
        normal = self.engine.search("UART", limit=30)
        self.assertFalse(any(r["kind"] == "output" or r["status"] == "historical-unverified" for r in normal))
        historical = self.engine.search("UART", include_historical=True, limit=30)
        self.assertTrue(any(r["status"] == "historical-unverified" for r in historical))
        self.assertTrue(self.engine.search("UART", kind="output"))

    def test_context_budget_and_no_unrelated_default_documents(self):
        pack = self.engine.context("UART", max_chars=180, limit=5)
        self.assertLessEqual(pack["characters"], 180)
        self.assertTrue(pack["documents"])
        self.assertFalse(self.engine.context("ZZZZ_NONEXISTENT", chip="BK9999")["documents"])

    def test_json_stdout_is_machine_readable(self):
        for command, args in [(cmd_search, ["串口", "--chip", "BK7259", "--processor", "CP", "--json-output"]), (cmd_context, ["串口", "--chip", "BK7259", "--processor", "AP", "--json-output"])]:
            result = CliRunner().invoke(command, args)
            self.assertEqual(result.exit_code, 0, result.output)
            self.assertTrue(json.loads(result.output))

    def test_read_rejects_outside_document_roots(self):
        self.write(self.root / "secret.md", "private")
        with self.assertRaises(ValueError):
            read_document(str(self.root / "secret.md"))
        with self.assertRaises(ValueError):
            read_document("raw/../../secret.md")

    def test_reindex_replaces_removed_documents(self):
        (self.raw / "shared.md").unlink()
        self.engine.index(self.wiki, self.raw)
        self.assertFalse(self.engine.search("Matter", family="bk_matter"))

    def test_chunker_does_not_treat_code_comments_as_headings(self):
        text = "# Guide\n\n```python\n# not a heading\nprint('demo')\n```\n\n## Next\nDetails\n"
        chunks = passages(text)
        self.assertEqual(len(chunks), 2)
        self.assertEqual(chunks[0]["heading"], "Guide")
        self.assertIn("# not a heading", chunks[0]["content"])

    def test_chip_suffix_and_softap_are_unambiguous(self):
        self.assertEqual(query_plan("BK7236N SoftAP 配网")["chips"], ["BK7236N"])
        self.assertIsNone(query_plan("BK7236N SoftAP 配网")["processor"])

    def test_lowercase_processor_and_ab_partition_terms(self):
        self.assertEqual(query_plan("BK7259 cp UART")["processor"], "CP")
        self.assertIn("ab", query_plan("BK7236 A/B OTA 升级确认")["primary"])
        self.assertNotIn("b", query_plan("BK7236 A/B OTA 升级确认")["primary"])

    def test_bom_titles_and_heading_only_passages(self):
        self.write(self.wiki / "concepts/pet.md", "\ufeff# 桌面宠物 GIF 播放\n\n## SD 卡\n读取 GIF 并播放动画。\n")
        self.engine.index(self.wiki, self.raw)
        row = self.engine.search("桌面宠物 GIF 播放")[0]
        self.assertEqual(row["title"], "桌面宠物 GIF 播放")
        self.assertEqual(row["start_line"], 3)
        self.assertIn("读取", row["snippet"])

    def test_chip_only_query_can_browse_scoped_documents(self):
        rows = self.engine.search("BK7236")
        self.assertTrue(rows)
        self.assertTrue(all(s["chip"] == "BK7236" for r in rows for s in r["matching_scopes"]))

    def test_module_title_beats_unrelated_initialization_mentions(self):
        self.write(self.raw / "mesh.md", "---\nchip: BK7236\n---\n# Bluetooth Mesh\n初始化 init initialization initialize 一连串初始化步骤。\n")
        self.engine.index(self.wiki, self.raw)
        self.assertIn("uart", self.engine.search("BK7236 串口初始化")[0]["path"])

    def test_multi_chip_comparison_keeps_identical_evidence(self):
        rows = self.engine.search("UART", chip=["BK7258", "BK7259"], processor="AP", limit=20)
        self.assertEqual({s["chip"] for r in rows for s in r["matching_scopes"]}, {"BK7258", "BK7259"})

    def test_evidence_scopes_keep_version_and_chip_paired(self):
        self.write(self.wiki / "summaries/multiple.md", "> **Source:** [A](../../raw/BK7258-AP/uart.md), [B](../../raw/BK7259-AP/uart.md)\n# UART 多版本\nUART 初始化对照说明。\n")
        self.engine.index(self.wiki, self.raw)
        self.assertFalse(self.engine.search("UART", chip="BK7258", version="v4.0.1", kind="summary"))

    def test_query_with_no_evidence_does_not_call_llm(self):
        from tools.kb.query import cmd_query
        with patch("tools.kb.query.get_config", return_value=self.cfg), patch("tools.kb.query.complete_with_context") as llm:
            result=CliRunner().invoke(cmd_query,["ZZZZ_NONEXISTENT","--chip","BK9999","--no-save"])
        self.assertEqual(result.exit_code,0,result.output)
        llm.assert_not_called()

    def test_http_query_string_routes_and_forwards_scope(self):
        from tools.kb.server import SearchHandler
        handler=SearchHandler.__new__(SearchHandler)
        handler.path="/api/search?q=UART&chip=BK7259&processor=CP"
        with patch.object(handler,"_handle_search") as route:
            handler.do_GET()
            route.assert_called_once()
        handler.engine=Mock()
        handler.engine.search.return_value=[]
        handler.wfile=io.BytesIO()
        with patch.object(handler,"send_response"),patch.object(handler,"send_header"),patch.object(handler,"end_headers"):
            handler._handle_search()
        handler.engine.search.assert_called_once_with("UART",limit=20,chip=["BK7259"],processor="CP",include_historical=False)

    def test_function_definition_beats_usage_mentions(self):
        self.write(self.raw / "api-reference/uart.md", "---\nchip: BK7236\n---\n# UART API\n\n## bk_uart_init\n<a id=\"_CPPv4bk_uart_init\"></a>\nint bk_uart_init(int port);\nInitialize the UART peripheral.\n")
        self.write(self.raw / "cli_api.md", "---\nchip: BK7236\n---\n# UART CLI examples\nCall bk_uart_init(0) from the shell.\n")
        self.engine.index(self.wiki, self.raw)
        row=self.engine.search("bk_uart_init",chip="BK7236")[0]
        self.assertEqual(row["path"],"api-reference/uart.md")
        self.assertEqual(row["anchor"],"_CPPv4bk_uart_init")


if __name__ == "__main__":
    unittest.main()
