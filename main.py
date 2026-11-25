#!/usr/bin/env python3
"""Entry for make.fun: The Internet in One Word.

One word for the whole internet: "Doomscrolling" — the endless scroll
through bad news, memes and everything in between. Funny because everyone
does it, fitting because it is what the internet is for, surprising
because the word itself is young but instantly understood.
"""

from os import makedirs

ENTRY = "Doomscrolling"


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if not ENTRY.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(ENTRY) > 30:
        raise ValueError("entry must be at most 30 characters")
    if any(ch.isspace() for ch in ENTRY):
        raise ValueError("entry must be a single word, no spaces")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
