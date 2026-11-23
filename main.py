#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes -- entry program.

Writes one single-line office joke to /output/entry.txt.
Deterministic: every run writes exactly the same bytes.
No network, no arguments, standard library only.
"""

import os

JOKE = "My manager calls it \u2018wearing many hats\u2019 \u2014 payroll calls it one salary."


def main() -> None:
    text = JOKE.strip()
    assert text, "joke must not be blank"
    assert "\n" not in text, "joke must be a single line"
    assert len(text) < 200, "joke must be under 200 characters"
    assert len(text.encode("utf-8")) < 200, "joke must be under 200 UTF-8 bytes"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("characters: %d" % len(text))


if __name__ == "__main__":
    main()
