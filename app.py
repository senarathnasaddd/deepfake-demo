import streamlit as st

st.set_page_config(page_title="Deepfake Research Portal", layout="wide")

# Custom CSS for professional layout
st.markdown("""
    <style>
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #aaa;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #111827;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        height: 100%;
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #fff;
    }
    .card-desc {
        font-size: 1rem;
        color: #ccc;
    }
    .nav-button {
        margin-top: 1.5rem;
        text-align: center;
    }
    .stButton > button {
        width: 100%;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        background-color: #2563eb;
        color: white;
    }
    .stButton > button:hover {
        background-color: #1e40af;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-title">Tensor Minds Web Demo</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">An interactive portal demonstrating Deepfake Generation, Detection, and Prevention Modules.</div>', unsafe_allow_html=True)

# Layout for three modules
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🎭 Generation</div>
        <div class="card-desc">
            Uses MediaPipe to extract facial features and blend them into source images to generate realistic deepfakes.
        </div>
        <div class="nav-button">
    """, unsafe_allow_html=True)
    st.button("Go to Generation", use_container_width=True, key="gen")
    st.markdown("</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🕵️ Detection</div>
        <div class="card-desc">
            Detects manipulated images using multi-stage classification across diverse datasets to test model robustness.
        </div>
        <div class="nav-button">
    """, unsafe_allow_html=True)
    st.button("Go to Detection", use_container_width=True, key="det")
    st.markdown("</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">🔐 Prevention</div>
        <div class="card-desc">
            Applies adversarial perturbations (FGSM, PGD, MFGSM) to make face images more resilient to deepfake attacks.
        </div>
        <div class="nav-button">
    """, unsafe_allow_html=True)
    st.button("Go to Prevention", use_container_width=True, key="prev")
    st.markdown("</div></div>", unsafe_allow_html=True)

# Navigation Logic
if st.session_state.get("gen"):
    st.switch_page("pages/deepfake_generation.py")
if st.session_state.get("det"):
    st.switch_page("pages/deepfake_detection.py")
if st.session_state.get("prev"):
    st.switch_page("pages/adversarial_generation.py")
