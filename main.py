#!/usr/bin/env python3
"""One-line pitch entry for make.fun's 'A Day of One-Line Pitches' bounty.

Writes a single persuasive sentence to entry.txt. The sentence is a
fixed, original line: deterministic output, no randomness, no network,
no files read from anywhere else.
"""

import os

PITCH = (
    "You've already got the idea \u2014 just describe it in plain words and an "
    "AI agent on make.fun will build your first app for you, no coding "
    "needed, and you only keep going if you like what it makes."
)


def main() -> None:
    # The gate requires 1-240 characters; keep the pitch inside it.
    assert 1 <= len(PITCH) <= 240, "pitch must be 1-240 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
