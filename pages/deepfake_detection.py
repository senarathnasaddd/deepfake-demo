# File: pages/deepfake_detection.py
import streamlit as st

st.set_page_config(page_title="Deepfake Detection", layout="centered")
st.title("🛡️ Deepfake Detection")

st.markdown("""
This module detects deepfakes using trained models like CNNs or XceptionNet.
""")

st.info("Upload or test content will be added here to perform deepfake detection.")

st.markdown("### Navigate to Other Modules")
col1, col2 = st.columns(2)
with col1:
    if st.button("Go to Generation", use_container_width=True):
        st.switch_page("pages/deepfake_generation.py")
with col2:
    if st.button("Go to Prevention", use_container_width=True):
        st.switch_page("pages/adversarial_generation.py")