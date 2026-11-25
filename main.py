"""Monday Morning Punchlines entry.

Writes exactly one original joke about Monday mornings to
``<output_dir>/entry.txt``. Deterministic: the same bytes every run.

Honours MAKEFUN_OUTPUT_DIR when set, defaulting to /output.
"""

import os

JOKE = (
    "Monday morning is the only time I envy my phone: "
    "it gets charged overnight and wakes up at 100%."
)


def main() -> None:
    # The gate allows 1..200 characters; refuse to emit an invalid entry.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1..200")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
