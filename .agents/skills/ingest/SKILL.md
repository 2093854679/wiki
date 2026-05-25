---
name: ingest
description: "Use when ingesting raw documents into the knowledge base, compiling incremental wiki notes, maintaining backlinks, and updating the wiki index/log. Triggered by /ingest or any request to process new or changed source files."
---

# Ingest Skill

## Purpose

Scan a target source directory, identify new or changed documents, and incrementally compile them into the wiki without rewriting unrelated content.

## Scope

- Default source directory: `raw/`
- Compiled wiki: `wiki/`
- Incremental state: `.kb_manifest.json`
- Search index: `.kb_search.db`

## Rules

1. Only process new or changed source files.
2. Keep all output as clean Markdown.
3. Preserve and extend existing notes; do not rewrite the whole wiki.
4. Use Obsidian wikilinks for internal references.
5. Keep the workflow incremental and safe.

## Workflow

### 1. Incremental identification

- Scan the target directory, defaulting to `raw/`.
- Read the existing manifest and identify:
  - files that are new
  - files that have changed since the last run
- Ignore files that are already processed and unchanged.

### 2. Source summarization

For each selected source file:

- Extract the title.
- Write a concise summary.
- Capture 3 to 5 core concepts.
- Preserve any image or figure references in plain text.
- Write or update a source summary note under `wiki/summaries/`.

Each summary note should include:

- a one-sentence TLDR
- key points
- the main arguments or findings
- related wikilinks

### 3. Concept synthesis

- Detect reusable concepts across the new summaries.
- Create new concept notes under `wiki/concepts/` when no existing note fits.
- Append incremental additions to existing concept notes when appropriate.
- Add wikilinks everywhere a concept is mentioned.

### 4. Index and log update

- Update `wiki/index.md` with the new or changed wiki entries.
- Append a short run log entry with timestamp, processed files, and newly added nodes.
- Keep both updates incremental.

### 5. Verification

- Regenerate the index after the ingest pass.
- Run search or lint checks when the change set is large enough to justify validation.
- Return a short report with the number of processed files and newly created or updated concept nodes.

## Output style

- Keep reports short and factual.
- Avoid HTML and emoji.
- Prefer simple Markdown lists and headings.