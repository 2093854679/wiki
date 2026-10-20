"""Local query normalization and line-preserving Markdown passages."""
from __future__ import annotations

import re

import yaml

CHIP_RE = re.compile(r"(?<![a-zA-Z0-9])BK\d{4}[A-Z]?(?![a-zA-Z0-9])", re.I)
ASCII_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9_]*")
CJK_RE = re.compile(r"[\u3400-\u9fff]+")
ANCHOR_RE = re.compile(r'<a\s+id="([^"<>]+)"[^>]*>\s*</a>')
SYMBOL_RE = re.compile(r"\b(?:bk|rtos|os|esp|pvPort|vTask|xTask|xQueue|xSemaphore)[A-Za-z0-9_]*\b")

# These are retrieval aliases, not technical equivalence claims.
ALIASES = {
    "串口": ["uart", "serial"], "uart": ["串口"],
    "初始化": ["init", "initialize"], "init": ["初始化"],
    "中断": ["interrupt", "isr"], "interrupt": ["中断", "isr"],
    "低功耗": ["power", "sleep", "pm", "低压", "保活"],
    "深度睡眠": ["deep", "sleep", "deepsleep"], "唤醒": ["wakeup", "wake"],
    "休眠": ["sleep", "pm"], "睡眠": ["sleep", "pm"],
    "配网": ["provisioning", "softap", "blufi"], "蓝牙": ["ble", "bluetooth"],
    "升级": ["ota", "upgrade"], "回滚": ["rollback", "回退"],
    "确认": ["confirm", "confirmation"], "执行区": ["partition", "分区"],
    "任务": ["task", "thread"], "任务栈": ["stack", "栈"],
    "栈不足": ["stack", "overflow", "溢出"], "栈溢出": ["stack", "overflow"],
    "内存": ["memory", "heap"], "堆": ["heap"],
    "优先级": ["priority"], "调度": ["scheduler", "schedule"],
    "消息队列": ["queue"], "信号量": ["semaphore"], "互斥": ["mutex"],
    "时钟拉伸": ["stretch", "stretching"], "iic": ["i2c"],
    "文件系统": ["filesystem", "littlefs", "fatfs"],
    "显示": ["display", "lcd", "lvgl"], "播放": ["play", "playback"],
    "摄像头": ["camera", "uvc", "dvp"], "音频": ["audio"],
    "桌面宠物": ["桌面萌宠", "desktop", "pet"], "桌面萌宠": ["桌面宠物", "desktop", "pet"],
    "安全启动": ["secure", "boot"], "启动": ["boot", "startup"],
    "核间通信": ["ipc", "mailbox"], "共享内存": ["shared", "memory", "ipc"],
    "读写": ["read", "write"], "接收": ["receive", "rx"], "发送": ["send", "tx"],
}
STOP_PHRASES = ["请问", "告诉我", "帮我", "如何", "怎么做", "怎么办", "怎么", "是什么", "有哪些", "的", "接口", "文档", "资料"]
STOP_ASCII = {"the", "a", "an", "of", "to", "how", "what", "is", "for", "and", "ap", "cp", "smp"}


def frontmatter(text):
    text = text.lstrip("\ufeff")
    if text.startswith("---\n") and (end := text.find("\n---\n", 4)) > 0:
        try:
            data = yaml.safe_load(text[4:end])
            return (data if isinstance(data, dict) else {}), text[:end + 5].count("\n")
        except yaml.YAMLError:
            pass
    return {}, 0


def clean_text(text):
    text = text.lstrip("\ufeff")
    text = ANCHOR_RE.sub("", text)
    text = re.sub(r"!\[([^\]]*)\]\([^\n]*?\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^\n]*?\)", r"\1", text)
    text = re.sub(r"<[^>\n]+>", "", text)
    text = re.sub(r"\\([_\[\]*#])", r"\1", text)
    return text.strip()


def terms(text):
    text = clean_text(text).lower()
    output = set(ASCII_RE.findall(text))
    for token in list(output):
        if "_" in token:
            output.update(p for p in token.split("_") if p)
    for run in CJK_RE.findall(text):
        if len(run) <= 12:
            output.add(run)
        output.update(run[i:i + 2] for i in range(len(run) - 1))
    return output


def query_plan(query, chip=None, family=None, processor=None):
    chips = list(chip) if isinstance(chip, (list, tuple)) else ([chip] if chip else [])
    explicit_chips = bool(chips)
    inferred = CHIP_RE.findall(query)
    if not chips:
        chips = inferred
    chips = sorted(set(c.upper() for c in chips))
    sides = {s.upper() for s in re.findall(r"(?<![A-Za-z])(?:AP|CP)(?![A-Za-z])", query, re.I)}
    if not processor and len(sides) == 1:
        processor = next(iter(sides))
    if not family:
        for phrase, value in [(r"\bAVDK[ _-]+SMP\b", "bk_avdk_smp"), (r"\bAIDK\b", "bk_aidk"), (r"\bIDK\b", "bk_idk"), (r"\bAVDK\b", "bk_avdk")]:
            if re.search(phrase, query, re.I):
                family = value
                break
    text = CHIP_RE.sub(" ", query)
    text = re.sub(r"\bA\s*/\s*B\b", " AB ", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z])(?:AP|CP|SMP)(?![A-Za-z])", " ", text, flags=re.I)
    text = re.sub(r"\b(?:AVDK[ _-]+SMP|AVDK|AIDK|IDK)\b", " ", text, flags=re.I)
    for phrase in STOP_PHRASES:
        text = text.replace(phrase, " ")
    primary = terms(text) - STOP_ASCII
    primary = {t for t in primary if len(t) > 1 or t.isascii()}
    groups, expanded = [], set(primary)
    lowered = clean_text(query).lower()
    for phrase, variants in ALIASES.items():
        if phrase in lowered:
            group = {phrase, *variants}
            groups.append(group)
            for word in group:
                expanded.update(terms(word))
    symbols = [s.lower() for s in SYMBOL_RE.findall(clean_text(query)) if "_" in s or s.startswith(("vTask", "xTask", "xQueue", "xSemaphore"))]
    expanded -= {c.lower() for c in chips}
    return {"chips": chips, "family": family.lower() if family else None, "processor": processor.upper() if processor else None, "primary": sorted(primary), "expanded": sorted(expanded), "groups": groups, "symbols": symbols, "explicit_chips": explicit_chips}


def passages(text, max_chars=2200):
    """Yield original line bounds; headings inside code fences stay literal."""
    text = text.lstrip("\ufeff")
    _, skip = frontmatter(text)
    lines = text.splitlines()
    heading, anchor, start, buffer, size = [], "", skip + 1, [], 0
    chunk_heading, chunk_anchor = [], ""
    fence = None
    output = []

    def flush(end):
        nonlocal buffer, start, size
        content = "\n".join(buffer).strip()
        substantive = re.sub(r"^#{1,6}\s+.*$", "", content, flags=re.M)
        if clean_text(substantive):
            output.append({"start_line": start, "end_line": end, "heading": " / ".join(chunk_heading), "anchor": chunk_anchor, "content": content})
        buffer, size = [], 0

    for number, line in enumerate(lines[skip:], skip + 1):
        stripped = line.strip().lstrip("> ")
        mark = re.match(r"(`{3,}|~{3,})", stripped)
        h = re.match(r"^(#{1,6})\s+(.+)", line) if not fence else None
        ids = ANCHOR_RE.findall(line) if not fence else []
        function_start = ids and any(x.startswith(("_CPP", "group__", "c.")) for x in ids)
        if not fence and ((h and buffer) or (function_start and size > 450) or size >= max_chars):
            flush(number - 1)
            start = number
        if h:
            level, title = len(h.group(1)), clean_text(h.group(2))
            heading = heading[:level - 1] + [title]
            anchor = ""
        if ids:
            # The first Sphinx ID is normally the canonical deep-link target.
            anchor = ids[0]
            if not clean_text(re.sub(r"^#{1,6}\s+.*$", "", "\n".join(buffer), flags=re.M)):
                chunk_anchor = anchor
        if not buffer:
            start = number
            chunk_heading, chunk_anchor = list(heading), anchor
        buffer.append(line)
        size += len(line) + 1
        if mark:
            if fence is None:
                fence = mark.group(1)[0]
            elif mark.group(1)[0] == fence:
                fence = None
        if size > 14000:
            flush(number)
            start = number + 1
    if buffer:
        flush(len(lines))
    return output


def list_values(value):
    if value is None:
        return []
    if isinstance(value, dict):
        return list(dict.fromkeys(str(v) for v in value.values()))
    if isinstance(value, (list, tuple, set)):
        return [str(v) for v in value]
    return [x.strip() for x in str(value).split(",") if x.strip()]
