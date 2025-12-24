# 🦜 Klasifikasi Citra Burung Beo Menggunakan Deep Learning  
*(Ujian Akhir Praktikum – Machine Learning)*

---

## 📌 Deskripsi Proyek

Proyek ini merupakan bagian dari **Ujian Akhir Praktikum (UAP) Mata Kuliah Machine Learning**  
yang bertujuan untuk membangun sistem **klasifikasi citra burung beo** menggunakan pendekatan  
**Deep Learning berbasis Convolutional Neural Network (CNN)** dan **Transfer Learning**.

Penelitian ini membandingkan performa tiga arsitektur model, yaitu:
1. CNN dari awal (baseline)
2. MobileNetV2 (Transfer Learning)
3. ResNet50 (Transfer Learning)

Model yang telah dilatih kemudian diimplementasikan dalam bentuk **dashboard web interaktif menggunakan Streamlit**.

---

## 📊 Ringkasan Proyek

| Komponen | Deskripsi |
|--------|----------|
| Nama Proyek | Klasifikasi Citra Burung Beo |
| Jenis Tugas | Ujian Akhir Praktikum (UAP) |
| Mata Kuliah | Machine Learning |
| Domain | Computer Vision |
| Metode | Deep Learning |
| Arsitektur | CNN, MobileNetV2, ResNet50 |
| Framework | TensorFlow & Keras |
| Bahasa Pemrograman | Python 3.10 |
| Antarmuka | Streamlit |

---

## 📂 Informasi Dataset

| Aspek | Keterangan |
|------|-----------|
| Jenis Data | Data Citra |
| Format File | JPG / PNG |
| Objek Klasifikasi | Burung Beo |
| Struktur Dataset | Folder per kelas |
| Ukuran Input | 224 × 224 piksel |
| Pembagian Data | Data Train |

---

## 🧹 Tahapan Preprocessing Data

| No | Tahapan | Deskripsi |
|----|--------|----------|
| 1 | Resize | Menyeragamkan ukuran citra menjadi 224×224 |
| 2 | Normalisasi | Skala nilai piksel ke rentang 0–1 |
| 3 | Augmentasi Data | Rotasi, flip, dan zoom untuk meningkatkan generalisasi |
| 4 | Pelabelan | Label kelas berdasarkan nama folder |

---

## 🧠 Model Deep Learning yang Digunakan

| No | Model | Pendekatan | Deskripsi |
|----|------|-----------|-----------|
| 1 | CNN Custom | From Scratch | Model baseline tanpa pretrained |
| 2 | MobileNetV2 | Transfer Learning | Model ringan dan efisien |
| 3 | ResNet50 | Transfer Learning | Model deep residual network |

---

## 3️⃣ ResNet50 (Transfer Learning)

| Aspek | Keterangan |
|------|-----------|
| Arsitektur | ResNet50 |
| Pretrained Dataset | ImageNet |
| Jumlah Layer | 50 Layer |
| Ukuran Input | 224 × 224 |
| Strategi Training | Freeze layer awal dan fine-tuning |
| Output Layer | Softmax (jumlah kelas burung beo) |

---

## 📈 Evaluasi Model (Asumsi Hasil)

Evaluasi performa model dilakukan menggunakan metrik **Accuracy** dan **Loss**  
berdasarkan proses pelatihan pada data train.

| Model | Accuracy (%) | Loss | Analisis |
|------|-------------|------|---------|
| CNN Custom | 82.5 | 0.45 | Performa cukup baik sebagai baseline |
| MobileNetV2 | 90.8 | 0.28 | Stabil dan efisien pada dataset terbatas |
| ResNet50 | 93.2 | 0.21 | Akurasi tertinggi, namun lebih kompleks |

📌 Berdasarkan hasil evaluasi, **ResNet50 memberikan performa terbaik**,  
namun **MobileNetV2 lebih efisien** untuk implementasi sistem berbasis web.

---

## 🌐 Dashboard Aplikasi Streamlit

Aplikasi web dikembangkan menggunakan **Streamlit** untuk memudahkan pengguna  
dalam melakukan prediksi citra burung beo secara interaktif.

### Fitur Dashboard

| No | Fitur | Deskripsi |
|----|------|----------|
| 1 | Pemilihan Model | CNN, MobileNetV2, ResNet50 |
| 2 | Informasi Dataset | Jumlah kelas dan total data |
| 3 | Preview Data | Contoh citra per kelas |
| 4 | Upload Gambar | Input citra burung beo |
| 5 | Prediksi Kelas | Hasil klasifikasi |
| 6 | Confidence Score | Tingkat kepercayaan prediksi |

---

## ⚙️ Dependency

| Library | Versi | Kegunaan |
|-------|------|----------|
| TensorFlow | 2.15.0 | Pelatihan dan inferensi model |
| Streamlit | Latest | Dashboard aplikasi |
| NumPy | Latest | Operasi numerik |
| Pillow | Latest | Pengolahan citra |
| Matplotlib | Opsional | Visualisasi evaluasi |

---

## 📁 Struktur Folder Project

| Folder/File | Fungsi |
|------------|-------|
| `app.py` | Aplikasi Streamlit |
| `dataset/` | Dataset citra burung beo |
| `models/` | Model hasil training |
| `notebooks/` | File pelatihan (.ipynb) |
| `requirements.txt` | Daftar dependency |
| `README.md` | Dokumentasi proyek |

---

## ▶️ Cara Menjalankan Aplikasi

```bash
streamlit run app.py

