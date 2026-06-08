# ml-clinical-template

> Template riusabile per mini-progetti di **Machine Learning su dati clinici**: app Streamlit + pipeline riproducibile + CI.

Questo repo è la base comune del portfolio. Ogni progetto (Phasor, AI/XAI, RAG, PINN, GenAI) parte da questa struttura per garantire coerenza e riproducibilità.

## Struttura

```
app/                 # App Streamlit (app/main.py)
src/clinical_template # Utility condivise (seeding, ...)
notebooks/           # Validazione riproducibile (01_, 02_, ...)
data/                # Solo script di download; i dati NON sono committati
scripts/             # download_data.py, train.py, evaluate.py
tests/               # pytest (smoke test su IO/shape/metriche)
results/             # Figure e metriche generate (piccole, committabili)
.github/workflows/   # CI: ruff + pytest
```

## Come eseguire (uv)

```bash
uv sync --extra dev            # crea .venv con Python 3.12 e installa tutto
uv run pytest -q               # esegue i test
uv run ruff check .            # lint
uv run streamlit run app/main.py
```

## Standard del portfolio

- **Dati pubblici e citati**: ogni dataset ha fonte + licenza nel README. I dati non si committano.
- **Riproducibilità**: seed fissati (`clinical_template.set_seed`), `uv.lock` versionato, notebook eseguibili end-to-end.
- **Valore dimostrato**: ogni progetto riporta almeno una **metrica quantitativa** + una **baseline**.
- **Citazioni**: riferimenti con DOI/PMID/URL, mai inventati.

## Come duplicare per un nuovo progetto

1. Copia la cartella e rinominala (es. `phasor-flim-explorer`).
2. Rinomina il package `src/clinical_template` → `src/<nome_progetto>` e aggiorna `pyproject.toml`.
3. Implementa pipeline, app, notebook e test.
4. Aggiorna questo README con pitch, screenshot, dataset, metriche e riferimenti.

## Licenza

Codice: MIT (vedi `LICENSE`). I dataset hanno licenze proprie: verificale prima dell'uso.
