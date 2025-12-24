# 🦜 Klasifikasi Citra Burung Beo Menggunakan Deep Learning

Project ini bertujuan untuk melakukan **klasifikasi citra burung beo (parrot)** menggunakan
metode **Deep Learning (Convolutional Neural Network)**.
Model dilatih menggunakan dataset citra burung beo dan diimplementasikan
dalam bentuk **dashboard interaktif menggunakan Streamlit**.

---

## 🎯 Tujuan Project
- Mengklasifikasikan citra burung beo berdasarkan kelas/jenis
- Menerapkan Deep Learning untuk pengenalan citra
- Menyediakan antarmuka web sederhana untuk melakukan prediksi gambar

---

## 🧠 Teknologi yang Digunakan
- **Python 3.10 (python.org)**
- **TensorFlow / Keras**
- **Streamlit**
- **NumPy**
- **Pillow (PIL)**
- **Matplotlib** (opsional, untuk visualisasi)
- **Scikit-learn** (opsional, evaluasi model)

---

## 📁 Struktur Folder Project
UAP_Birds_Classification/
│
├── app.py # Aplikasi Streamlit
├── README.md # Dokumentasi project
├── requirements.txt # Daftar dependency
│
├── dataset/
│ └── processed/
│ └── train/
│ ├── parrot_1/
│ ├── parrot_2/
│ └── ...
│
├── models/
│ ├── cnn.h5
│ ├── mobilenet.h5
│ └── resnet50.h5
│
└── notebooks/
└── train_3_models.ipynb # Notebook training model

