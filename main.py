"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

JOKE_LINE = "Our AI judge has never survived a Monday, yet it just promoted the printer, the only coworker that jams under pressure and never calls in sick."


def resolve_entry_path():
    """Work out where the entry text goes, honouring the harness env vars."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        if explicit.endswith(".txt"):
            return explicit
        return os.path.join(explicit, "entry.txt")
    folder = os.environ.get("ENTRY_OUT_DIR")
    if folder:
        return os.path.join(folder, "entry.txt")
    return "/output/entry.txt"


def emit_joke(destination):
    """Write the joke to disk and echo it to stdout."""
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(JOKE_LINE)
    print(JOKE_LINE)


def run():
    emit_joke(resolve_entry_path())


if __name__ == "__main__":
    run()
