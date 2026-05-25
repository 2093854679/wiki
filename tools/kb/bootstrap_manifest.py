"""Bootstrap .kb_manifest.json from existing raw/ files."""
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

raw_dir = Path("raw")
manifest = {}

for f in raw_dir.rglob("*"):
    if not f.is_file() or f.name.startswith("."):
        continue
    rel = str(f.relative_to(raw_dir)).replace("\\", "/")
    manifest[rel] = {
        "hash": hashlib.sha256(f.read_bytes()).hexdigest(),
        "last_compiled": datetime.now(timezone.utc).isoformat(),
    }

out_path = Path("tools/kb/cache/.kb_manifest.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(f"Bootstrapped manifest with {len(manifest)} files")
