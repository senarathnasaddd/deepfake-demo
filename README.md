# Deepfake Research Demo (Streamlit App)

This project is a modular web demo built with **Streamlit** to support research on **deepfake creation, protection using adversarial attacks**, and **deepfake detection**.

### Project Modules

1. **Deepfake Creation**  
   Upload a face image and simulate deepfake generation (e.g., face swap using StarGAN or similar tools).

2. **Adversarial Protection**  
   Apply adversarial perturbations (FGSM, PGD, Iterative FGSM) to protect images from deepfake misuse.

3. **Detection & Evaluation**  
   Upload an image and simulate detection of deepfakes using classification and evaluation metrics (SSIM, PSNR).

---
needed packages
    streamlit
    numpy
    Pillow

### How to Run

```bash
streamlit run app.py
