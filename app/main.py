"""App Streamlit di esempio del template.

Sostituisci questo contenuto con l'interfaccia specifica del progetto.
Avvia con:  uv run streamlit run app/main.py
"""

import streamlit as st

from clinical_template import set_seed

st.set_page_config(page_title="Clinical ML Template", layout="wide")

set_seed(0)

st.title("🧪 Clinical ML Template")
st.write(
    "Template riusabile per mini-progetti di ML clinico. "
    "Duplica questa cartella, rinomina il package e implementa la tua pipeline."
)

st.success("Ambiente attivo correttamente.")
