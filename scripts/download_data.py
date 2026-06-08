"""Download idempotente dei dati pubblici del progetto.

Regole del portfolio:
- I dati NON vengono mai committati (vedi .gitignore).
- Lo script deve essere idempotente: se i file esistono, non riscarica.
- Documenta SEMPRE la fonte e la licenza del dataset nel README.

Questo è un placeholder del template: ogni progetto lo sovrascrive.
"""

from __future__ import annotations

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    print(f"Cartella dati pronta: {DATA_DIR}")
    print("Placeholder: implementa qui il download del dataset del progetto.")


if __name__ == "__main__":
    main()
