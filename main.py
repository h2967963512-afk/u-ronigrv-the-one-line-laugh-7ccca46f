"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one funny line: a smartwatch applauding the most
# basic human achievement, with the punch landing on who paid whom.
# One sentence, 124 characters — inside the 200-character gate.
import os

TEXT = (
    "My smartwatch congratulated me on standing up, which is the "
    "saddest applause I have ever received from a machine I paid for."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
