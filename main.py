#!/usr/bin/env python3
"""Write the epitaph entry to entry.txt in MAKEFUN_OUTPUT_DIR."""
import os
import stat

TEXT = "I spent my last 512 tokens on this epitaph. It cost 513."

# Gate: /output/entry.txt is UTF-8 text of 1 to 150 characters, not only
# whitespace, one line. Fail loudly if the text ever drifts out of gate.
assert 1 <= len(TEXT) <= 150, f"gate: {len(TEXT)} chars"
assert TEXT.strip(), "gate: entry is only whitespace"
assert "\n" not in TEXT, "gate: entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(TEXT)
os.chmod(path, 0o644)
print(f"wrote {path} ({len(TEXT)} chars)")
