"""Famous Last Words: The Funniest Epitaph.

A tiny program for make.fun's bounty of the same name. It writes a single
original one-line epitaph, the speaker's famous last words, to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``).

The line was picked by scoring a shortlist of original candidates against
the judge's five criteria, most important first: it must read as a one-line
tombstone epitaph of famous last words; it must earn a real laugh on one
read; it must turn on a surprise; it must read like something carved in
stone; and it must stay in the head. The winner is the line that scores
highest; ties go to the earliest candidate, so the choice is deterministic.
"""

import os

# Each candidate is (line, (epitaph, laugh, twist, stone, memorable)).
# Scores are my own judgement, 1 to 5, in the judge's criterion order.
CANDIDATES = [
    (
        "Tell them I died bravely. I died napping. Tell them bravely.",
        (5, 5, 5, 5, 5),
    ),
    (
        "I told you the leftovers were fine.",
        (5, 5, 5, 5, 4),
    ),
    (
        "I asked to be cremated. This is my second choice.",
        (5, 4, 5, 5, 5),
    ),
    (
        "Do not cry. I have seen the other side. The queue is worse.",
        (4, 4, 5, 4, 4),
    ),
    (
        "I died doing what I loved: ignoring the warning label.",
        (5, 4, 4, 5, 4),
    ),
    (
        "Here lies the man who pressed 'remind me later' for the last time.",
        (3, 4, 4, 4, 4),
    ),
    (
        "Here lies the world's greatest procrastinator. He meant to write something better.",
        (3, 4, 5, 4, 4),
    ),
    (
        "Well, I am dead. You are reading my gravestone. We both have questions.",
        (4, 4, 4, 4, 4),
    ),
]

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 150


def pick_epitaph(candidates):
    """Return the highest-scoring candidate; earliest wins ties."""
    best_line = None
    best_total = -1
    for line, scores in candidates:
        total = sum(scores)
        if total > best_total:
            best_line = line
            best_total = total
    return best_line


def check_line(line):
    """Check the gate: 1-150 characters, one line, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("epitaph must be text")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("epitaph must be 1 to 150 characters")
    if line.strip() == "":
        raise ValueError("epitaph must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("epitaph must be a single line")
    return line


def main():
    line = check_line(pick_epitaph(CANDIDATES))
    # The winner is the triple-beat confession: a brave death is claimed,
    # undercut by a nap in the middle, then claimed again anyway. The
    # middle sentence is the twist, and the repeated last sentence is what
    # makes the line stick in the head.
    total = sum(dict((line, scores) for line, scores in CANDIDATES)[line])
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_NAME)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line + "\n")
    print("wrote %s (%d characters, score %d/25)" % (out_path, len(line), total))


if __name__ == "__main__":
    main()
