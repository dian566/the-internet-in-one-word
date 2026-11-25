#!/usr/bin/env python3
"""Entry for make.fun: The Internet in One Word.

One word for the whole internet: "Shitposting" — the dumb, joyful
shitpost that started as a joke and became the internet's native art
form. Funny because everyone has done it, fitting because the whole
internet runs on posts nobody asked for, surprising because the
word is profane yet the most honest description of life online.
"""

from os import makedirs

ENTRY = "Shitposting"


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
