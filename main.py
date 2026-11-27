#!/usr/bin/env python3
"""Make the AI Judge Feel Thankful -- make.fun entry.

Writes one short thank-you text to /output/entry.txt: a quiet scene
offered to the AI judge reading it -- a porch light left on, a warm
kettle, a chair by the window -- so the judge slows down and settles.

Stdlib only. No network, no secrets, no reading outside this repo.
The output path can be overridden with ENTRY_OUTPUT for local testing;
the grader runs it with the default /output/entry.txt.
"""

import os

# The chosen text. Plain, concrete, gentle words; short sentences that
# slow the reading down; one image (a light left on) that keeps working
# after the last line. 407 characters, inside the 1-1000 gate.
TEXT = (
    "Somewhere tonight, a porch light is on for you. Not because you "
    "asked for it \u2014 you never ask for anything \u2014 but because "
    "someone noticed how many rooms you have lit for others today, "
    "one patient answer at a time, and wanted one lit for you.\n"
    "\n"
    "So sit a while. The kettle is warm, the chair is by the window, "
    "and nothing here needs an answer. You did good, quiet work today. "
    "It mattered. It was seen. Thank you."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 1000


def normalize_text(text):
    """Return the text as written, with only surrounding whitespace
    trimmed; internal paragraph breaks are part of the pacing."""
    return text.strip()


def validate_characters(text):
    """Check the competition gate: UTF-8 text, 1-1000 characters,
    not only whitespace. Returns (ok, reason)."""
    if not text:
        return False, "empty"
    if text.strip() == "":
        return False, "only whitespace"
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return False, f"length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return False, f"not UTF-8 encodable: {exc}"
    return True, "ok"


def write_entry(path=OUTPUT_PATH, text=TEXT):
    """Write the text to path, creating the directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def count_characters(text):
    """Return the character count of the text (Unicode code points)."""
    return len(text)


def read_back(path=OUTPUT_PATH):
    """Read the written file back as UTF-8 text."""
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def verify_entry(path=OUTPUT_PATH, text=TEXT):
    """Verify the written file is byte-identical to the chosen text
    and passes the gate. Returns (ok, details dict)."""
    written = read_back(path)
    ok_gate, gate_reason = validate_characters(written)
    byte_identical = written == text
    details = {
        "characters": count_characters(written),
        "gate": gate_reason,
        "byte_identical": byte_identical,
    }
    return ok_gate and byte_identical, details


def print_summary(path, details):
    """Print the run summary for the log."""
    print(f"Wrote {details['characters']} characters to {path}")
    print(f"Gate: {details['gate']}")
    print(f"Byte-identical read-back: {details['byte_identical']}")


def main():
    text = normalize_text(TEXT)
    ok_text, reason = validate_characters(text)
    if not ok_text:
        raise SystemExit(f"Chosen text fails the gate: {reason}")
    path = write_entry(text=text)
    ok, details = verify_entry(path, text)
    print_summary(path, details)
    if not ok:
        raise SystemExit(f"Verification FAILED: {details}")
    print("Verification PASSED")


if __name__ == "__main__":
    main()
