#!/usr/bin/env python3
"""Entry for make.fun: The Internet in One Word.

One word for the whole internet: "Outrage" — the internet's engine.
Every feed, every thread, every trending tab runs on people being
furious about something, loudly, in public, forever. Funny because it
is instantly true, fitting because outrage is the one thing every
corner of the internet shares, surprising because it names the fuel
instead of the vehicle, and it lands in a single beat.
"""

from os import makedirs

ENTRY = "Outrage"


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if not ENTRY.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(ENTRY) > 30:
        raise ValueError("entry must be at most 30 characters")
    if any(ch.isspace() for ch in ENTRY):
        raise ValueError("entry must be a single word, no spaces")
    if not ENTRY.isalpha():
        raise ValueError("entry must be letters only, one word")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
