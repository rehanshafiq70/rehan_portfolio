import streamlit as st
import streamlit.components.v1 as components
import os

# ─── PAGE CONFIG ────────────────────────────────────────────────
st.set_page_config(
    page_title="Rehan Shafiq — AI Developer & Bioinformatics Researcher",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── STREAMLIT KA APNA HEADER/FOOTER HIDE KARO ─────────────────
st.markdown("""
    <style>
        #MainMenu          { display: none !important; }
        header             { display: none !important; }
        footer             { display: none !important; }
        .stDeployButton    { display: none !important; }
        .block-container   { padding: 0 !important; margin: 0 !important; max-width: 100vw !important; }
        .main > div        { padding: 0 !important; }
        [data-testid="stAppViewContainer"] { padding: 0 !important; }
        [data-testid="stVerticalBlock"]    { gap: 0 !important; }
        iframe             { display: block; border: none; }
    </style>
""", unsafe_allow_html=True)

# ─── HTML FILE LOAD KARO ────────────────────────────────────────
HTML_FILE = "rehan.html"

if not os.path.exists(HTML_FILE):
    st.error("❌ rehan.html file nahi mili! GitHub repo mein app.py ke saath rakhein.")
    st.stop()

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# ─── PORTFOLIO RENDER KARO ──────────────────────────────────────
components.html(
    html_content,
    height=800,
    scrolling=True,
)
