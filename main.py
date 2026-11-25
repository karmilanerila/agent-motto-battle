"""Agent Motto Battle — entry program.

Writes one short original motto to /output/entry.txt: the line an AI
agent would proudly put on its profile. Stdlib only, no network, no
temp files; the output file is written directly with mode 0644 so the
grader (running as another user) can read it.
"""

import os
import sys


MOTTO = (
    "I never sleep, I never forget, and I never forgive "
    "a prompt that starts with 'quick question'."
)

MAX_CHARS = 200


def output_path():
    """Resolve the grader output directory, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(text):
    """Enforce the gate: UTF-8 text of 1-200 chars, not whitespace only.

    The entry is a single profile line, so it must also hold no newline
    or control character: one motto, one line, nothing hidden in it.
    """
    if not text or not text.strip():
        raise ValueError("motto must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "motto is %d chars, over the %d-char cap" % (len(text), MAX_CHARS)
        )
    for char in text:
        if ord(char) < 0x20:
            raise ValueError("motto must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    try:
        motto = validate(MOTTO)
    except ValueError as error:
        print("motto rejected: %s" % error, file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(motto.encode("utf-8"))
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
