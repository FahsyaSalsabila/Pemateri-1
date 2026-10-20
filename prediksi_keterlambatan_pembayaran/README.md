# Prediksi Keterlambatan Pembayaran Pelanggan

Proyek pembelajaran berdasarkan materi **Make Sense of Data with Analytics and AI**. Proyek ini menganalisis invoice dan membangun model Machine Learning sederhana untuk memperkirakan apakah pembayaran invoice berpotensi terlambat.

## Studi kasus

PT Maju Bersama adalah perusahaan distributor dengan banyak transaksi. Keterlambatan pembayaran dapat meningkatkan piutang dan mengganggu arus kas. Analisis data dapat membantu perusahaan mengenali invoice yang perlu diperhatikan lebih awal.

## Tujuan

- Menyiapkan dan memeriksa kualitas data.
- Melakukan analisis deskriptif sederhana.
- Membandingkan model Logistic Regression dan Random Forest.
- Mengevaluasi model dengan Accuracy, Precision, Recall, F1-score, dan ROC-AUC.
- Menyimpan hasil perbandingan, prediksi data uji, dan grafik.

## Teknologi

- Python
- pandas dan NumPy
- scikit-learn
- Matplotlib
- Visual Studio Code

## Struktur proyek

```text
prediksi_keterlambatan_pembayaran/
├── data/
│   └── invoices.csv              # dibuat oleh generate_data.py
├── outputs/                      # hasil analisis dibuat otomatis
├── generate_data.py              # membuat data sintetis
├── main.py                       # analisis dan pemodelan
├── requirements.txt
├── .gitignore
└── README.md
```

## Cara menjalankan di VS Code

Pastikan Python sudah terpasang. Buka folder proyek di VS Code, lalu buka terminal.

### 1. Buat virtual environment (opsional, disarankan)

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

Jika perintah `python` tidak dikenali, coba gunakan `py`.

### 2. Pasang library

```bash
pip install -r requirements.txt
```

### 3. Buat dataset sintetis

```bash
python generate_data.py
```

### 4. Jalankan analisis dan model

```bash
python main.py
```

Hasil metrik akan tampil di terminal. File hasil tersimpan di folder `outputs/`.

## Penjelasan data

Semua data dibuat secara sintetis untuk keperluan pembelajaran, bukan data asli pelanggan atau perusahaan.

| Kolom | Arti |
|---|---|
| `invoice_amount` | Nilai invoice |
| `payment_terms_days` | Batas waktu pembayaran dalam hari |
| `customer_tenure_months` | Lama menjadi pelanggan |
| `previous_late_payments` | Jumlah riwayat keterlambatan sebelumnya |
| `order_count_6m` | Jumlah pesanan dalam enam bulan |
| `payment_method` | Metode pembayaran |
| `customer_segment` | Segmen pelanggan |
| `invoice_month` | Bulan invoice |
| `late_payment` | Target: 1 terlambat, 0 tidak terlambat |

Label pada dataset ini adalah contoh sintetis, bukan definisi operasional perusahaan nyata. Untuk penerapan sebenarnya, tim bisnis harus menentukan batas keterlambatan yang jelas, misalnya pembayaran belum diterima 30 hari setelah jatuh tempo.

## Metode analisis

1. **Data preparation:** memeriksa duplikasi dan nilai kosong, lalu menyiapkan fitur numerik dan kategorikal.
2. **Descriptive analytics:** melihat distribusi status pembayaran dan persentase invoice terlambat.
3. **Predictive analytics:** melatih Logistic Regression dan Random Forest.
4. **Evaluasi:** membandingkan Accuracy, Precision, Recall, F1-score, dan ROC-AUC. Recall penting karena mengukur proporsi invoice terlambat yang berhasil ditemukan model.
5. **Pelaporan:** menyimpan tabel perbandingan, prediksi data uji, dan grafik.

## Interpretasi dan batasan

- Akurasi tinggi tidak otomatis berarti model bagus, terutama jika kelas terlambat lebih sedikit daripada kelas tidak terlambat.
- Perhatikan Recall dan ROC-AUC serta confusion matrix.
- Model yang dipilih dalam contoh ini berdasarkan Recall tertinggi pada data uji; untuk penggunaan nyata, pemilihan model juga perlu mempertimbangkan biaya salah prediksi, validasi waktu, dan kebutuhan bisnis.
- Dataset sintetis hanya untuk demonstrasi. Jangan mengklaim hasilnya sebagai prediksi nyata.
- Keputusan akhir terkait penagihan harus tetap dilakukan oleh manusia.
- Jangan mengunggah data pelanggan asli, nomor rekening, alamat, atau informasi pribadi ke repositori publik.

## Mengunggah ke GitHub

1. Buat repositori baru di GitHub, misalnya `prediksi-keterlambatan-pembayaran`.
2. Jangan tambahkan README dari GitHub jika file README sudah ada di folder lokal (atau ikuti instruksi GitHub untuk repositori yang sudah memiliki file).
3. Buka terminal di folder proyek dan jalankan:

```bash
git init
git add .
git commit -m "Initial project: payment delay prediction"
git branch -M main
git remote add origin https://github.com/USERNAME/prediksi-keterlambatan-pembayaran.git
git push -u origin main
```

Ganti `USERNAME` dengan nama akun GitHub milikmu. Pastikan Git sudah terpasang dan kamu sudah login/terautentikasi. Jika GitHub memberi URL repositori berbeda, gunakan URL milik repositorimu.

## Kesimpulan

Proyek ini menunjukkan alur dasar analisis data dari penyiapan data hingga evaluasi model prediksi. Hasilnya dapat menjadi bahan pendukung keputusan, tetapi perlu data nyata yang berkualitas dan validasi lebih lanjut sebelum diterapkan di perusahaan.
