# 🚲 Bike Sharing Data Analysis

## Deskripsi
Project ini bertujuan untuk menganalisis pola penggunaan layanan bike sharing guna memahami perilaku pengguna berdasarkan waktu serta perbedaan antara tipe pengguna (*casual* dan *registered*).

---

## Struktur Direktori

- **/dashboard**: Memuat file `dashboard.py` dan data hasil pembersihan (`main_data.csv`).
- **/data**: Berisi data mentah yang digunakan selama proses analisis.
- **notebook.ipynb**: Mencakup keseluruhan proses analisis lengkap dari tahap *Gathering* hingga *Conclusion*.
- **requirements.txt**: Daftar dependensi atau library Python yang dibutuhkan.
- **README.md**: Memuat penjelasan serta panduan penggunaan prject.

---

## Insight

- Terdapat pola penggunaan sepeda yang signifikan pada jam-jam sibuk, yaitu pagi dan sore hari
- Hari kerja menunjukkan pola aktivitas rutin, sedangkan akhir pekan cenderung lebih stabil.
- Pengguna *registered* mendominasi penggunaan, terutama pada jam-jam sibuk.
- Pengguna *casual* lebih banyak menggunakan sepeda pada waktu santai, terutama siang hingga sore hari.

---

## Setup Environment - Shell/Terminal

1. Install semua dependencies:
pip install -r requirements.txt

2. Jalankan dashboard:
streamlit run dashboard/dashboard.py