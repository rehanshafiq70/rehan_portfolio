"""
Rehan Shafiq — AI Developer Portfolio
Streamlit wrapper for full HTML/CSS/JS portfolio
Deployment: GitHub + Streamlit Cloud (Python 3.11)
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# ─── PAGE CONFIG ────────────────────────────────────────────────
st.set_page_config(
    page_title="Rehan Shafiq — AI Developer & Bioinformatics Researcher",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://github.com/rehanshafiq70",
        "About": "Portfolio of Rehan Shafiq — AI Developer & Bioinformatics Researcher",
    },
)

# ─── HIDE ALL STREAMLIT CHROME ───────────────────────────────────
# Removes header, footer, padding so the HTML fills the entire viewport
st.markdown(
    """
    <style>
        /* Hide Streamlit default UI */
        #MainMenu          { display: none !important; }
        header             { display: none !important; }
        footer             { display: none !important; }
        .stDeployButton    { display: none !important; }

        /* Remove all padding / margins from the app container */
        .block-container {
            padding: 0 !important;
            margin:  0 !important;
            max-width: 100vw !important;
        }
        .main > div                          { padding: 0 !important; }
        [data-testid="stAppViewContainer"]   { padding: 0 !important; }
        [data-testid="stVerticalBlock"]      { gap: 0 !important; }
        [data-testid="stHorizontalBlock"]    { gap: 0 !important; }

        /* Make the iframe fill the screen */
        iframe {
            display: block;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─── LOAD HTML FILE ─────────────────────────────────────────────
HTML_FILE = "rehan.html"

def load_html(filepath: str) -> str:
    """Read portfolio HTML from disk with UTF-8 encoding."""
    if not os.path.exists(filepath):
        st.error(
            f"❌ HTML file not found: `{filepath}`\n\n"
            "Make sure `rehan.html` is in the **same folder** as `app.py` "
            "before pushing to GitHub."
        )
        st.stop()
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

html_content = load_html(HTML_FILE)

# ─── RENDER FULL HTML PORTFOLIO ─────────────────────────────────
# height is set generously to cover the full scrollable page.
# scrolling=True enables native scroll inside the component iframe.
components.html(
    html_content,
    height=5800,   # covers all sections: hero + about + projects + skills + connect + contact + footer
    scrolling=True,
)
