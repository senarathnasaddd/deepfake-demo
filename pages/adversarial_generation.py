# File: pages/adversarial_generation.py
import streamlit as st
from PIL import Image
import io
import base64

# Dummy protection functions (replace with real implementations)
def run_fgsm(image): return image
def run_pgd(image): return image
def run_multi_fgsm(image, steps): return image

# Page setup
st.set_page_config(page_title="Deepfake Prevention", layout="centered")
st.title("🔐 Deepfake Prevention")

st.markdown("""
This module protects your image using adversarial perturbations (FGSM, PGD, Iterative FGSM) to resist deepfake generation.
""")

uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "png"])

def show_image_in_box(img: Image.Image, caption: str):
    """Display image in a centered 2-inch styled box"""
    resized_img = img.resize((192, 192))
    buf = io.BytesIO()
    resized_img.save(buf, format="PNG")
    img_base64 = base64.b64encode(buf.getvalue()).decode()

    st.markdown(f"""
    <div style="text-align: center;">
        <div style="width: 192px; height: 192px; margin: auto; border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center;">
            <img src="data:image/png;base64,{img_base64}" style="max-width: 100%; max-height: 100%; object-fit: contain;" />
        </div>
        <p style="margin-top: 0.5em;"><strong>{caption}</strong></p>
    </div>
    """, unsafe_allow_html=True)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize((256, 256))
    show_image_in_box(image, "🖼️ Original Image")

    method = st.selectbox("🔐 Choose Protection Method", ["FGSM", "PGD", "Iterative FGSM (Multi-step)"])

    steps = None
    if method == "Iterative FGSM (Multi-step)":
        steps = st.number_input("🔁 Iterations", min_value=1, max_value=20, value=5, step=1)

    # Centered Run Protection Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        run_clicked = st.button("🚀 Run Protection", use_container_width=True)

    if run_clicked:
        if method == "FGSM":
            result_img = run_fgsm(image)
        elif method == "PGD":
            result_img = run_pgd(image)
        else:
            result_img = run_multi_fgsm(image, steps=steps)

        st.success(f"{method} applied successfully! 🎉")
        show_image_in_box(result_img, "🔒 Protected Image")

        # Centered download button
        download_buf = io.BytesIO()
        result_img.save(download_buf, format="PNG")
        download_buf.seek(0)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download Protected Image",
                data=download_buf,
                file_name="protected_image.png",
                mime="image/png",
                use_container_width=True
            )

# Navigation to other modules
st.markdown("### Navigate to Other Modules")
col1, col2 = st.columns(2)
with col1:
    if st.button("Go to Generation", use_container_width=True):
        st.switch_page("pages/deepfake_generation.py")
with col2:
    if st.button("Go to Detection", use_container_width=True):
        st.switch_page("pages/deepfake_detection.py")
