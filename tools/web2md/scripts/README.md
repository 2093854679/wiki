# Local web2md helpers

These scripts are vault-specific utilities for the BK_IDK mirror.

- `bk_doc_to_md.py`: crawl Beken docs and write Markdown into `raw/bk_doc/bk_idk/`
- `localize_bk_doc_images.py`: download referenced images, rewrite Markdown links, and prune non-Markdown/non-image leftovers
- `cleanup_bk_doc_output.py`: remove any remaining non-Markdown/non-image artifacts from the BK_IDK mirror
