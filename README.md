# Histogram-Threshold

1. Aplikasi Pengolahan Citra Digital

Ini adalah aplikasi web sederhana yang dibuat dengan Python dan Streamlit untuk memenuhi tugas mata kuliah Pengolahan Citra Digital.

Aplikasi ini memungkinkan pengguna untuk mengunggah sebuah gambar dan melakukan beberapa operasi dasar pengolahan citra.

- Fitur

	1. Analisis Histogram: Menampilkan histogram untuk citra Grayscale dan RGB, baik 	dalam 	bentuk grafik maupun nilai numeriknya.

	2. Thresholding & Citra Biner: Secara otomatis menentukan nilai ambang batas 	(threshold) menggunakan metode Otsu dan mengubah citra menjadi citra biner 	berdasarkan nilai tersebut.

	3. Histogram Equalization (Uniform): Melakukan perataan histogram pada citra 	grayscale untuk meningkatkan kontras. Aplikasi juga menampilkan perbandingan citra, 	histogram, serta nilai Mean dan Standar Deviasi sebelum dan sesudah proses 	ekualisasi.

2. Teknologi yang Digunakan

	- Python

	- Streamlit

	- OpenCV

	- Numpy

	- Matplotlib

	- Pillow

3. cara menjlankan 

1. Clone repositori ini (jika sudah di-upload ke Git) atau pastikan semua file ada dalam satu folder.

- app.py

- requirements.txt

- README.md


2. Install semua library yang dibutuhkan.

pip install -r requirements.txt

3. Jalankan aplikasi Streamlit.

streamlit run app.py

4. Buka browser Anda dan akses alamat URL yang ditampilkan di terminal.
