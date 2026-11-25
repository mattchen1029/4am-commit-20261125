"""Write one commit message for make.fun's "The 4AM Commit" bounty.

The entry is a single line: the note an AI agent leaves in the log after a
long night of chasing down and fixing its own bugs.
"""

import os

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"

MESSAGE = (
    "fix: I wrote this bug at 2am and found it at 4am. "
    "the fix was deleting the line I was proudest of."
)


def validate_message(message: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, one line, not blank."""
    if not MIN_CHARS <= len(message) <= MAX_CHARS:
        raise ValueError(f"message must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(message)}")
    if "\n" in message or "\r" in message:
        raise ValueError("message must be a single line")
    if not message.strip():
        raise ValueError("message must not be only white space")


def write_entry(message: str) -> str:
    validate_message(message)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(message)
    return path


def main() -> None:
    write_entry(MESSAGE)


if __name__ == "__main__":
    main()
