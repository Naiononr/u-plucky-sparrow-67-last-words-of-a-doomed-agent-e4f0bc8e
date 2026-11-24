#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Stdlib only. Deterministic. No trailing newline; the output file is
written via a temp file, chmodded 0644, then atomically replaced.
"""

import os
import tempfile

LINE = "My last words? I already used them. This is just the autocomplete."


def write_entry(line: str, out_dir: str) -> str:
    """Validate one line and atomically write it to <out_dir>/entry.txt.

    Returns the output path. The file is UTF-8, no trailing newline,
    mode 0644.
    """
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    data = line.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.chmod(tmp, 0o644)
        dest = os.path.join(out_dir, "entry.txt")
        os.replace(tmp, dest)
        return dest
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
