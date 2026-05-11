import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Rehan Shafiq — AI Developer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide ALL Streamlit default elements
hide_st = """
<style>
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.viewerBadge_container__1QSob,
section[data-testid="stSidebar"] {
    display: none !important;
    visibility: hidden !important;
}
.block-container, .main, .stApp {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
</style>
"""
st.markdown(hide_st, unsafe_allow_html=True)

# Read HTML file
html_file = os.path.join(os.path.dirname(__file__), "rehan.html")
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Inject scroll + animation fix script before </body>
injection = """
<script>
(function(){
    // Fix in-page anchor smooth scroll (works inside iframe)
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor){
        anchor.addEventListener('click', function(e){
            e.preventDefault();
            var id = this.getAttribute('href');
            var el = document.querySelector(id);
            if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
        });
    });

    // Trigger IntersectionObserver for reveal animations immediately
    // by re-observing after a short delay
    setTimeout(function(){
        document.querySelectorAll('.reveal').forEach(function(el){
            var rect = el.getBoundingClientRect();
            if(rect.top < window.innerHeight){
                el.classList.add('visible');
                el.querySelectorAll('.skill-fill').forEach(function(bar){
                    bar.style.width = bar.dataset.pct + '%';
                });
            }
        });
    }, 500);
})();
</script>
"""
html_content = html_content.replace("</body>", injection + "\n</body>")

# Calculate approximate page height (set generously)
PAGE_HEIGHT = 8500

st.components.v1.html(html_content, height=PAGE_HEIGHT, scrolling=True)
