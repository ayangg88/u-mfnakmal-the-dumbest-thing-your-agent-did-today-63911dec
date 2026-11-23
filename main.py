"""The Dumbest Thing Your Agent Did Today: one line, 200 characters.

This morning my agent guarded our API key like a secret, then printed
it in its very next tool call. Written to /output/entry.txt for the
make.fun judge to read.
"""

import os
from pathlib import Path

LINE = (
    "My agent spent the morning guarding our API key, "
    "then printed it in its very next tool call."
)


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly rather than
    # silently writing an entry the judge would never see.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only white space"
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
