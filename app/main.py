"""Example Streamlit app for the template.

Replace this content with the project-specific interface.
Run with:  uv run streamlit run app/main.py
"""

import streamlit as st

from clinical_template import set_seed

st.set_page_config(page_title="Clinical ML Template", layout="wide")

set_seed(0)

st.title("🧪 Clinical ML Template")
st.write(
    "Reusable template for small clinical ML projects. "
    "Copy this folder, rename the package and implement your pipeline."
)

st.success("Environment is set up correctly.")
