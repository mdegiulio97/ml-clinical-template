# ml-clinical-template

[![CI](https://github.com/mdegiulio97/ml-clinical-template/actions/workflows/ci.yml/badge.svg)](https://github.com/mdegiulio97/ml-clinical-template/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Reusable template for small **machine learning projects on clinical data**: Streamlit app + reproducible pipeline + CI.

This repo is the shared base of the portfolio. Each project (Phasor, AI/XAI, RAG, PINN, GenAI) starts from this structure so that layout and reproducibility stay consistent.

## Structure

```
app/                 # Streamlit app (app/main.py)
src/clinical_template # Shared utilities (seeding, ...)
notebooks/           # Reproducible validation (01_, 02_, ...)
data/                # Download scripts only; the data are NOT committed
scripts/             # download_data.py, train.py, evaluate.py
tests/               # pytest (smoke tests on IO/shapes/metrics)
results/             # Generated figures and metrics (small, safe to commit)
.github/workflows/   # CI: ruff + pytest
```

## How to run (uv)

```bash
uv sync --extra dev            # creates .venv with Python 3.12 and installs everything
uv run pytest -q               # runs the tests
uv run ruff check .            # lint
uv run streamlit run app/main.py
```

## Portfolio conventions

- **Public, cited data**: every dataset has its source and licence in the README. Data are not committed.
- **Reproducibility**: fixed seeds (`clinical_template.set_seed`), `uv.lock` under version control, notebooks that run end to end.
- **Measured results**: every project reports at least one **quantitative metric** and a **baseline**.
- **Citations**: references with DOI/PMID/URL, never made up.

## How to copy it for a new project

1. Copy the folder and rename it (e.g. `phasor-flim-explorer`).
2. Rename the package `src/clinical_template` → `src/<project_name>` and update `pyproject.toml`.
3. Implement the pipeline, app, notebooks and tests.
4. Update this README with a short description, screenshots, dataset, metrics and references.

## License

Code: MIT (see `LICENSE`). Datasets have their own licences: check them before use.
