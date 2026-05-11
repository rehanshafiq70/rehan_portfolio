import streamlit as st
import os

st.set_page_config(
    page_title="Rehan Shafiq — AI Developer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        .stApp {
            margin: 0;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Load and render the HTML file
html_file = os.path.join(os.path.dirname(__file__), "rehan.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=6000, scrolling=True)
