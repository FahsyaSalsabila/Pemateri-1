# Studi Kasus: Prediksi Keterlambatan Pembayaran Pelanggan

## A. Latar Belakang

PT Maju Bersama merupakan perusahaan distributor yang memiliki banyak pelanggan dan transaksi penjualan. Perusahaan menghadapi masalah keterlambatan pembayaran invoice yang menyebabkan peningkatan piutang dan penurunan arus kas operasional.

Untuk mengatasi masalah tersebut, perusahaan membutuhkan sistem yang dapat menganalisis riwayat transaksi dan memprediksi invoice yang berpotensi terlambat dibayar. Hasil analisis diharapkan dapat membantu perusahaan mengidentifikasi pelanggan yang perlu mendapatkan perhatian lebih awal sehingga proses penagihan dapat dilakukan secara lebih efektif.

## B. Rumusan Masalah

1. Bagaimana menganalisis data transaksi dan pembayaran pelanggan?
2. Bagaimana memprediksi invoice yang berpotensi terlambat dibayar?
3. Bagaimana mengevaluasi apakah model prediksi sudah cukup baik?
4. Bagaimana memanfaatkan hasil prediksi untuk membantu pengambilan keputusan perusahaan?

## C. Tujuan Proyek

- Mengolah dan membersihkan data transaksi pelanggan.
- Melakukan analisis deskriptif terhadap pembayaran pelanggan.
- Mengembangkan model *Machine Learning* untuk mengklasifikasikan keterlambatan pembayaran.
- Mengevaluasi model menggunakan Accuracy, Recall, dan ROC-AUC, bukan hanya akurasi.
- Menghasilkan rekomendasi untuk membantu perusahaan menentukan prioritas penagihan.

## D. Hubungan dengan Materi Pemateri

Proyek ini menerapkan konsep *Data Analytics* dan *Artificial Intelligence* (AI) yang dibahas dalam materi pemateri, yaitu:

| Materi | Implementasi dalam Proyek |
|---|---|
| **Data Preparation** | Memeriksa data kosong, data duplikat, dan tipe data sebelum digunakan dalam analisis. |
| **Descriptive Analytics** | Menghitung jumlah dan persentase invoice yang terlambat maupun tidak terlambat dibayar. |
| **Diagnostic Analytics** | Membandingkan pola keterlambatan berdasarkan karakteristik transaksi pelanggan. |
| **Predictive Analytics** | Memprediksi kemungkinan keterlambatan pembayaran invoice menggunakan model *Machine Learning*. |
| **Model Evaluation** | Mengukur performa model menggunakan Accuracy, Precision, Recall, F1-Score, dan ROC-AUC. |
| **Generative AI** | Membantu memahami kode program dan menganalisis hasil, dengan tetap melakukan verifikasi oleh manusia. |

Materi pemateri juga menekankan bahwa model dengan nilai Accuracy yang tinggi belum tentu memiliki performa yang baik apabila tidak mampu mendeteksi kasus keterlambatan pembayaran yang sebenarnya. Oleh karena itu, evaluasi perlu mempertimbangkan metrik lain, terutama Recall, agar kemampuan model dalam mengidentifikasi invoice yang terlambat dapat dinilai dengan lebih tepat.

## E. Gambaran Implementasi

Proyek ini menggunakan Python untuk mengolah data, melakukan analisis, membangun model prediksi, dan mengevaluasi hasilnya. Model yang digunakan adalah **Logistic Regression** dan **Random Forest**. Performa kedua model dibandingkan untuk mengetahui model yang lebih sesuai dengan tujuan prediksi keterlambatan pembayaran.

Data yang digunakan merupakan **data sintetis untuk keperluan pembelajaran**, bukan data transaksi perusahaan yang sebenarnya. Oleh karena itu, hasil prediksi digunakan sebagai simulasi penerapan analitik data dan *Machine Learning*, bukan sebagai bukti performa pada kondisi bisnis nyata.

## F. Hasil yang Diharapkan

Proyek ini diharapkan menghasilkan informasi mengenai pola pembayaran pelanggan, prediksi invoice yang berpotensi terlambat, evaluasi performa model, serta rekomendasi yang dapat membantu perusahaan memprioritaskan penagihan dan mengurangi risiko peningkatan piutang.
