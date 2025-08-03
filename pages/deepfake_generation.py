# File: pages/deepfake_generation.py
import streamlit as st

st.set_page_config(page_title="Deepfake Generation", layout="centered")
st.title("🤖 Deepfake Generation")

st.markdown("""
This module showcases how deepfake videos or images are generated using models like StarGAN or StyleGAN.
""")

st.info("Demo and controls for deepfake generation will be implemented here.")

st.markdown("### Navigate to Other Modules")
col1, col2 = st.columns(2)
with col1:
    if st.button("Go to Detection", use_container_width=True):
        st.switch_page("pages/deepfake_detection.py")
with col2:
    if st.button("Go to Prevention", use_container_width=True):
        st.switch_page("pages/adversarial_generation.py")