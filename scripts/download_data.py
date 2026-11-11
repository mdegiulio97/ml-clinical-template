"""Idempotent download of the project's public data.

Portfolio rules:
- Data are NEVER committed (see .gitignore).
- The script must be idempotent: if the files exist, it does not download them again.
- ALWAYS document the dataset's source and licence in the README.

This is a template placeholder: each project overrides it.
"""

from __future__ import annotations

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    print(f"Data folder ready: {DATA_DIR}")
    print("Placeholder: implement the project's dataset download here.")


if __name__ == "__main__":
    main()
