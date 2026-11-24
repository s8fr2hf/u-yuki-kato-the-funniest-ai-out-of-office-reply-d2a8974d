#!/usr/bin/env python3
"""Copy the out-of-office reply to /output/entry.txt."""

import os

ENTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(text, output_dir):
    """Write text to <output_dir>/entry.txt atomically.

    A crash mid-write can never leave a truncated entry.txt behind:
    the text goes to a temp file in the same directory first, then is
    renamed into place. No chmod calls: the grader runs as an
    unprivileged user on directories it does not own.
    """
    os.makedirs(output_dir, exist_ok=True)
    tmp_path = os.path.join(output_dir, "entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, os.path.join(output_dir, "entry.txt"))


def main():
    with open(ENTRY, "r", encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 160 or not text.strip():
        raise SystemExit("entry must be 1-160 non-whitespace characters")
    write_entry(text, OUTPUT_DIR)


if __name__ == "__main__":
    main()
