# ============================================================
#  Rehan Shafique — AI Developer Portfolio (Streamlit)
#  University of Agriculture Faisalabad | Pakistan
#  Email : rehanshafiq6540@gmail.com
# ============================================================

import streamlit as st

# ── Page config ────────────────────────────────────────────
st.set_page_config(
    page_title="Rehan Shafique | AI Developer",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────
st.markdown("""
<style>
/* ---- Google Font ---- */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] { font-family: 'Syne', sans-serif; }

/* ---- Dark base ---- */
.stApp { background: #050d1a; color: #e2e8f0; }

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a1628 0%, #050d1a 100%);
    border-right: 1px solid #1e3a5f;
}

/* ---- Cards ---- */
.card {
    background: rgba(14,30,60,.6);
    border: 1px solid rgba(56,189,248,.15);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
    backdrop-filter: blur(10px);
    transition: border-color .3s;
}
.card:hover { border-color: rgba(56,189,248,.5); }

/* ---- Skill badge ---- */
.skill-badge {
    display: inline-block;
    background: linear-gradient(135deg,#0ea5e9,#6366f1);
    color: #fff;
    border-radius: 999px;
    padding: .35rem 1rem;
    margin: .3rem;
    font-size: .82rem;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    letter-spacing: .04em;
}

/* ---- Hero gradient text ---- */
.gradient-text {
    background: linear-gradient(135deg,#38bdf8 0%,#818cf8 60%,#f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ---- Progress bar label ---- */
.skill-label {
    font-family:'JetBrains Mono',monospace;
    font-size:.78rem;
    color:#94a3b8;
    margin-bottom:.15rem;
}

/* ---- Section header ---- */
.section-title {
    font-size:2rem; font-weight:800;
    margin-bottom:1.2rem; margin-top:1rem;
}

/* ---- Button override ---- */
div.stButton > button {
    background: linear-gradient(135deg,#0ea5e9,#6366f1);
    color: #fff;
    border: none;
    border-radius: 8px;
    font-family:'Syne',sans-serif;
    font-weight:700;
    padding:.55rem 1.4rem;
    transition: opacity .2s;
}
div.stButton > button:hover { opacity:.85; }

/* ---- Link button ---- */
.link-btn {
    display:inline-block;
    background:linear-gradient(135deg,#0ea5e9,#6366f1);
    color:#fff !important;
    text-decoration:none;
    padding:.55rem 1.6rem;
    border-radius:8px;
    font-weight:700;
    font-size:.9rem;
    margin-right:.6rem;
    transition:opacity .2s;
}
.link-btn:hover{opacity:.82;}

/* ---- Project card ---- */
.proj-card {
    background:rgba(14,30,60,.7);
    border:1px solid rgba(56,189,248,.2);
    border-radius:18px;
    padding:1.8rem;
    margin-bottom:1.4rem;
}
.proj-tag {
    display:inline-block;
    background:rgba(14,165,233,.15);
    color:#38bdf8;
    border:1px solid rgba(56,189,248,.3);
    border-radius:999px;
    padding:.2rem .8rem;
    font-size:.74rem;
    margin:.2rem;
    font-family:'JetBrains Mono',monospace;
}

/* ---- Contact input ---- */
.stTextInput input, .stTextArea textarea {
    background:#0a1628 !important;
    color:#e2e8f0 !important;
    border:1px solid #1e3a5f !important;
    border-radius:8px !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  S I D E B A R
# ══════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:1.5rem 0 1rem;'>
        <div style='width:90px;height:90px;border-radius:50%;
             background:linear-gradient(135deg,#0ea5e9,#6366f1);
             display:flex;align-items:center;justify-content:center;
             font-size:2.4rem;margin:0 auto .8rem;'>🧬</div>
        <div style='font-size:1.1rem;font-weight:800;color:#f8fafc;'>Rehan Shafique</div>
        <div style='font-size:.78rem;color:#64748b;font-family:"JetBrains Mono",monospace;
             margin-top:.3rem;'>AI Developer · ML Engineer</div>
        <div style='font-size:.74rem;color:#475569;margin-top:.25rem;'>🎓 UAF, Pakistan</div>
    </div>
    <hr style='border-color:#1e3a5f;margin:.5rem 0 1.2rem;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠 Home", "👤 About", "⚡ Skills", "🚀 Projects", "📬 Contact"],
        label_visibility="collapsed",
    )

    st.markdown("""
    <hr style='border-color:#1e3a5f;margin:1.2rem 0 .8rem;'>
    <div style='font-size:.76rem;color:#475569;text-align:center;'>
        📧 rehanshafiq6540@gmail.com<br>
        <span style='color:#1e3a5f;'>──────────────────</span><br>
        © 2026 Rehan Shafique
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  P A G E S
# ══════════════════════════════════════════════════════════

# ── HOME ──────────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown("""
    <div style='min-height:10px;'></div>
    <div style='font-family:"JetBrains Mono",monospace;color:#0ea5e9;
         font-size:.88rem;letter-spacing:.12em;margin-bottom:.4rem;'>
        // HELLO, WORLD
    </div>
    <h1 style='font-size:3.4rem;font-weight:800;line-height:1.1;margin:0 0 .6rem;'>
        Hi, I'm <span class="gradient-text">Rehan Shafique</span>
    </h1>
    <h2 style='font-size:1.4rem;font-weight:400;color:#94a3b8;margin:0 0 1.6rem;'>
        AI Developer &nbsp;·&nbsp; Machine Learning Engineer &nbsp;·&nbsp; Bioinformatics Student
    </h2>
    <p style='font-size:1.05rem;color:#cbd5e1;max-width:680px;line-height:1.75;margin-bottom:2rem;'>
        Building intelligent systems at the intersection of <strong style='color:#38bdf8;'>
        Artificial Intelligence</strong> and <strong style='color:#818cf8;'>Bioinformatics</strong>.
        Passionate about turning biological data into life-saving AI solutions.
    </p>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        if st.button("🚀 View Projects"):
            st.info("Navigate to **Projects** in the sidebar →")
    with c2:
        if st.button("📬 Contact Me"):
            st.info("Navigate to **Contact** in the sidebar →")

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick-stat row
    s1, s2, s3, s4 = st.columns(4)
    stats = [
        ("🧠", "AI / ML", "Expert"),
        ("🧬", "Bioinformatics", "Researcher"),
        ("📦", "Projects", "5 +"),
        ("🎓", "UAF Pakistan", "B.Sc Student"),
    ]
    for col, (icon, label, val) in zip([s1,s2,s3,s4], stats):
        col.markdown(f"""
        <div class="card" style='text-align:center;'>
            <div style='font-size:2rem;'>{icon}</div>
            <div style='font-weight:700;color:#f8fafc;font-size:1.05rem;margin:.3rem 0 .1rem;'>{val}</div>
            <div style='font-size:.78rem;color:#64748b;'>{label}</div>
        </div>""", unsafe_allow_html=True)

    # Featured project teaser
    st.markdown("""
    <div class='proj-card' style='margin-top:1.5rem;'>
        <div style='font-size:.78rem;color:#0ea5e9;font-family:"JetBrains Mono",monospace;
             letter-spacing:.1em;margin-bottom:.5rem;'>// FEATURED PROJECT</div>
        <div style='font-size:1.4rem;font-weight:800;color:#f8fafc;margin-bottom:.5rem;'>
            🩺 Skin Cancer Prediction System
        </div>
        <p style='color:#94a3b8;line-height:1.7;margin-bottom:1rem;'>
            AI-powered skin cancer detection using CNN deep-learning models,
            deployed as an interactive Streamlit web application.
        </p>
        <span class='proj-tag'>TensorFlow</span>
        <span class='proj-tag'>CNN</span>
        <span class='proj-tag'>Streamlit</span>
        <span class='proj-tag'>Keras</span>
        <span class='proj-tag'>Medical AI</span>
        <br><br>
        <a class='link-btn' href='https://skincancerpredictions.streamlit.app/' target='_blank'>
            👉 Open Live Project
        </a>
    </div>
    """, unsafe_allow_html=True)

# ── ABOUT ─────────────────────────────────────────────────
elif page == "👤 About":
    st.markdown('<h1 class="section-title gradient-text">About Me</h1>', unsafe_allow_html=True)

    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("""
        <div class='card'>
        <p style='color:#cbd5e1;line-height:1.85;font-size:1rem;'>
        I'm <strong style='color:#38bdf8;'>Rehan Shafique</strong>, an AI Developer and
        Bioinformatics student at the <strong style='color:#818cf8;'>University of Agriculture
        Faisalabad (UAF), Pakistan</strong>. I specialise in building end-to-end machine
        learning pipelines and deploying intelligent web applications that solve real-world
        problems — particularly in healthcare and life sciences.
        </p>
        <p style='color:#cbd5e1;line-height:1.85;font-size:1rem;margin-top:.8rem;'>
        My academic background in <strong style='color:#38bdf8;'>Bioinformatics</strong> gives me a
        unique lens through which I apply Deep Learning to genomics, proteomics, and medical
        imaging. My flagship project — a <em>Skin Cancer Prediction System</em> powered by
        convolutional neural networks — exemplifies my commitment to AI for social good.
        </p>
        <p style='color:#94a3b8;line-height:1.85;font-size:.95rem;margin-top:.8rem;'>
        When I'm not training models, I contribute to open-source research, write technical
        articles, and mentor junior developers. I believe the future of medicine will be
        written in Python.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class='card'>
            <div style='font-size:.78rem;color:#0ea5e9;font-family:"JetBrains Mono",monospace;
                 letter-spacing:.1em;margin-bottom:.9rem;'>// QUICK FACTS</div>
            <table style='width:100%;font-size:.88rem;color:#94a3b8;border-collapse:collapse;'>
                <tr><td style='padding:.4rem 0;'>📛</td><td><strong style='color:#f8fafc;'>Rehan Shafique</strong></td></tr>
                <tr><td>🎓</td><td>UAF, Pakistan</td></tr>
                <tr><td>🌍</td><td>Faisalabad, Pakistan</td></tr>
                <tr><td>📧</td><td style='word-break:break-all;'>rehanshafiq6540@gmail.com</td></tr>
                <tr><td>💼</td><td>AI / ML Engineer</td></tr>
                <tr><td>🔬</td><td>Bioinformatics Researcher</td></tr>
                <tr><td>🛠️</td><td>Python · TensorFlow · Streamlit</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────
elif page == "⚡ Skills":
    st.markdown('<h1 class="section-title gradient-text">Skills & Expertise</h1>', unsafe_allow_html=True)

    badge_skills = [
        "Python","Machine Learning","Deep Learning","TensorFlow","Keras",
        "Scikit-learn","Pandas","NumPy","Matplotlib","Seaborn",
        "Streamlit","OpenCV","Bioinformatics","Data Science",
        "CNN","NLP","Transfer Learning","Git","Linux","SQL"
    ]
    badges_html = "".join(f"<span class='skill-badge'>{s}</span>" for s in badge_skills)
    st.markdown(f"<div style='margin-bottom:2rem;'>{badges_html}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Proficiency")

    skills_pct = {
        "Python": 95, "Machine Learning": 88, "Deep Learning / TensorFlow": 85,
        "Data Science & Visualisation": 82, "Bioinformatics": 78,
        "Streamlit Deployment": 90, "Research & Writing": 80,
    }
    for skill, pct in skills_pct.items():
        st.markdown(f"<div class='skill-label'>{skill} — {pct}%</div>", unsafe_allow_html=True)
        st.progress(pct / 100)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧰 Tools & Frameworks")

    t1, t2, t3 = st.columns(3)
    tool_groups = [
        ("🤖 AI / ML", ["TensorFlow", "Keras", "PyTorch (basic)", "Scikit-learn", "OpenCV"]),
        ("📊 Data", ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly"]),
        ("🚀 DevOps", ["Streamlit", "Git / GitHub", "VS Code", "Jupyter", "Linux CLI"]),
    ]
    for col, (title, items) in zip([t1, t2, t3], tool_groups):
        items_html = "".join(f"<li style='color:#94a3b8;padding:.2rem 0;'>{i}</li>" for i in items)
        col.markdown(f"""
        <div class='card'>
            <div style='font-weight:700;color:#38bdf8;margin-bottom:.6rem;'>{title}</div>
            <ul style='margin:0;padding-left:1.2rem;list-style:disc;'>{items_html}</ul>
        </div>""", unsafe_allow_html=True)

# ── PROJECTS ──────────────────────────────────────────────
elif page == "🚀 Projects":
    st.markdown('<h1 class="section-title gradient-text">Projects</h1>', unsafe_allow_html=True)

    projects = [
        {
            "emoji": "🩺",
            "title": "Skin Cancer Prediction System",
            "desc": ("AI-powered skin cancer detection using Convolutional Neural Networks (CNN). "
                     "Trained on the HAM10000 dermatoscopy dataset, achieving high accuracy in "
                     "classifying 7 types of skin lesions. Deployed as an interactive Streamlit app "
                     "with real-time image inference."),
            "tags": ["TensorFlow","CNN","Keras","Streamlit","Medical AI","OpenCV"],
            "demo": "https://skincancerpredictions.streamlit.app/",
            "status": "✅ Live",
        },
        {
            "emoji": "🧬",
            "title": "Bioinformatics Sequence Analyser",
            "desc": ("A Python toolkit for DNA/RNA sequence analysis, GC-content computation, "
                     "ORF detection and BLAST integration. Designed for computational biology "
                     "research workflows with a clean CLI interface."),
            "tags": ["Python","BioPython","BLAST","Genomics","CLI"],
            "demo": None,
            "status": "🔧 In Development",
        },
        {
            "emoji": "📊",
            "title": "Protein Structure Prediction ML Pipeline",
            "desc": ("Machine-learning pipeline that predicts secondary protein structures using "
                     "LSTM-based sequence models. Benchmarked against PSIPRED with competitive "
                     "Q3 accuracy on CASP targets."),
            "tags": ["LSTM","BioPython","Scikit-learn","Pandas","Research"],
            "demo": None,
            "status": "🔬 Research Phase",
        },
        {
            "emoji": "📈",
            "title": "COVID-19 Data Dashboard",
            "desc": ("Interactive data visualisation dashboard built with Streamlit and Plotly, "
                     "displaying real-time global COVID-19 statistics, trend graphs, and "
                     "country-level heatmaps fetched from the Our World in Data API."),
            "tags": ["Streamlit","Plotly","Pandas","REST API","Dashboard"],
            "demo": None,
            "status": "✅ Complete",
        },
    ]

    for p in projects:
        tags_html = "".join(f"<span class='proj-tag'>{t}</span>" for t in p["tags"])
        demo_btn = (f"<a class='link-btn' href='{p['demo']}' target='_blank'>👉 Live Demo</a>"
                    if p["demo"] else "")
        st.markdown(f"""
        <div class='proj-card'>
            <div style='display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem;'>
                <span style='font-size:1.8rem;'>{p['emoji']}</span>
                <span style='font-size:1.25rem;font-weight:800;color:#f8fafc;'>{p['title']}</span>
                <span style='margin-left:auto;font-size:.78rem;color:#64748b;
                     font-family:"JetBrains Mono",monospace;'>{p['status']}</span>
            </div>
            <p style='color:#94a3b8;line-height:1.75;margin-bottom:.9rem;'>{p['desc']}</p>
            <div style='margin-bottom:1rem;'>{tags_html}</div>
            {demo_btn}
        </div>""", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────
elif page == "📬 Contact":
    st.markdown('<h1 class="section-title gradient-text">Get In Touch</h1>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.6, 1])
    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        name  = st.text_input("Your Name", placeholder="e.g. Ali Hassan")
        email = st.text_input("Your Email", placeholder="you@example.com")
        subj  = st.text_input("Subject", placeholder="Collaboration / Research / Freelance …")
        msg   = st.text_area("Message", placeholder="Tell me about your project or idea …", height=160)

        if st.button("📤 Send Message"):
            if name and email and msg:
                st.success(f"✅ Thanks **{name}**! Your message has been received. I'll reply soon.")
            else:
                st.warning("Please fill in Name, Email, and Message.")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='card'>
            <div style='font-size:.78rem;color:#0ea5e9;font-family:"JetBrains Mono",monospace;
                 letter-spacing:.1em;margin-bottom:1rem;'>// CONTACT INFO</div>
            <p style='color:#94a3b8;font-size:.92rem;line-height:1.75;'>
                I'm open to research collaborations, freelance AI projects, and full-time
                opportunities. Feel free to reach out!
            </p>
            <hr style='border-color:#1e3a5f;margin:1rem 0;'>
            <div style='font-size:.88rem;color:#cbd5e1;'>
                📧 <strong>Email</strong><br>
                <span style='color:#64748b;font-family:"JetBrains Mono",monospace;
                font-size:.78rem;'>rehanshafiq6540@gmail.com</span>
            </div>
            <div style='margin-top:.8rem;font-size:.88rem;color:#cbd5e1;'>
                🏛️ <strong>Institution</strong><br>
                <span style='color:#64748b;font-size:.8rem;'>
                University of Agriculture Faisalabad, Pakistan
                </span>
            </div>
            <div style='margin-top:.8rem;font-size:.88rem;color:#cbd5e1;'>
                🌐 <strong>Live Project</strong><br>
                <a href='https://skincancerpredictions.streamlit.app/'
                   target='_blank'
                   style='color:#38bdf8;font-size:.8rem;word-break:break-all;'>
                    skincancerpredictions.streamlit.app
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
