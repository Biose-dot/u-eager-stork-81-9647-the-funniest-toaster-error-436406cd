#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (120 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

A toaster error in the shape of a real device message (ERR_CRUST) with a straight-faced absurd cause: the bread unionized with the bagels.
"""
import os

ENTRY = 'ERR_CRUST: Bread refused to brown. It has unionized with the bagels and demands better heating.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
