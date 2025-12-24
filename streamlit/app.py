import streamlit as st
import numpy as np
import tensorflow as tf
import os
from PIL import Image

# ===============================
# KONFIGURASI PATH PROJECT
# ===============================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MODEL_PATHS = {
    "CNN Scratch": os.path.join(PROJECT_ROOT, "models", "cnn_scratch.h5"),
    "MobileNetV2": os.path.join(PROJECT_ROOT, "models", "mobilenetv2.h5"),
    "ResNet50": os.path.join(PROJECT_ROOT, "models", "resnet50.h5"),
}

CLASS_DIR = os.path.join(PROJECT_ROOT, "dataset", "processed", "train")

# 🔥 FIX UTAMA: bersihkan nama kelas & pastikan hanya folder
CLASS_NAMES = sorted([
    os.path.splitext(cls)[0]
    for cls in os.listdir(CLASS_DIR)
    if os.path.isdir(os.path.join(CLASS_DIR, cls))
])

IMG_SIZE = (224, 224)

# ===============================
# LOAD MODEL (CACHE)
# ===============================
@st.cache_resource
def load_model(model_path):
    return tf.keras.models.load_model(model_path, compile=False)

# ===============================
# PREPROCESS IMAGE
# ===============================
def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# ===============================
# STREAMLIT CONFIG
# ===============================
st.set_page_config(
    page_title="Birds Classification - UAP",
    layout="centered"
)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("⚙️ Pengaturan Model")
model_name = st.sidebar.selectbox(
    "Pilih Model Klasifikasi",
    list(MODEL_PATHS.keys())
)

st.sidebar.markdown("---")
st.sidebar.info(f"**Model Aktif:**  \n{model_name}")

model = load_model(MODEL_PATHS[model_name])

# ===============================
# MAIN UI
# ===============================
st.title("🦜 Birds Image Classification")
st.markdown(
    """
    **Ujian Akhir Praktikum Pembelajaran Mesin**  
    Klasifikasi citra burung menggunakan CNN, MobileNetV2, dan ResNet50
    """
)

# ===============================
# UPLOAD GAMBAR
# ===============================
uploaded_file = st.file_uploader(
    "📤 Upload Gambar Burung",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar Input", use_column_width=True)

    image_array = preprocess_image(image)

    if st.button("🔍 Prediksi"):
        prediction = model.predict(image_array)[0]  # (num_classes,)

        # Prediksi utama
        predicted_index = np.argmax(prediction)
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = float(prediction[predicted_index])

        st.success(f"**Prediksi:** {predicted_class}")
        st.info(f"**Confidence Tertinggi:** {confidence * 100:.2f}%")

        # ===============================
        # CONFIDENCE SETIAP KELAS
        # ===============================
        st.markdown("### 📊 Confidence Setiap Kelas")

        class_confidence = {
            CLASS_NAMES[i]: float(prediction[i]) * 100
            for i in range(len(CLASS_NAMES))
        }

        # Urutkan dari tertinggi ke terendah
        class_confidence = dict(
            sorted(class_confidence.items(), key=lambda x: x[1], reverse=True)
        )

        for class_name, conf in class_confidence.items():
            st.write(f"**{class_name}** — {conf:.2f}%")
            st.progress(conf / 100.0)

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("© UAP Pembelajaran Mesin | Birds Image Classification")
