import streamlit as st
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# --- FUNGSI-FUNGSI BANTUAN ---

def calculate_and_plot_hist_grayscale(image):
    """Menghitung dan menampilkan histogram untuk citra grayscale."""
    # Pastikan citra dalam format grayscale (jika belum)
    if len(image.shape) > 2:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
        
    # Hitung histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    
    # Buat plot
    fig, ax = plt.subplots()
    ax.plot(hist, color='gray')
    ax.set_title("Histogram Grayscale")
    ax.set_xlabel("Intensitas Piksel")
    ax.set_ylabel("Jumlah Piksel")
    ax.grid(True)
    plt.xlim([0, 256])
    
    return fig, hist

def calculate_and_plot_hist_rgb(image_bgr):
    """Menghitung dan menampilkan histogram untuk citra RGB."""
    color = ('b', 'g', 'r')
    fig, ax = plt.subplots()
    hists = {}
    
    for i, col in enumerate(color):
        hist = cv2.calcHist([image_bgr], [i], None, [256], [0, 256])
        hists[col] = hist
        ax.plot(hist, color=col)
    
    ax.set_title("Histogram RGB")
    ax.set_xlabel("Intensitas Piksel")
    ax.set_ylabel("Jumlah Piksel")
    ax.grid(True)
    plt.xlim([0, 256])
    
    return fig, hists

# --- KONFIGURASI HALAMAN STREAMLIT ---
st.set_page_config(page_title="Pengolahan Citra Digital", layout="wide")
st.title("Tugas Pengolahan Citra Digital")
st.write("Unggah sebuah gambar untuk melakukan analisis histogram, thresholding, dan ekualisasi.")

# --- SIDEBAR UNTUK UPLOAD GAMBAR ---
with st.sidebar:
    st.header("Upload Citra")
    uploaded_file = st.file_uploader("Pilih sebuah file gambar...", type=["jpg", "jpeg", "png", "bmp"])

# --- AREA UTAMA ---
if uploaded_file is not None:
    # Membaca gambar yang diunggah
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)
    
    # Konversi dari RGB (PIL) ke BGR (OpenCV)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    st.header("Citra Asli")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Citra RGB Asli", use_container_width=True)
    with col2:
        st.image(gray_image, caption="Citra Grayscale", use_container_width=True)

    st.markdown("---")
    
    # --- 1. TAMPILKAN HISTOGRAM RGB DAN GRAYSCALE ---
    st.header("1. Analisis Histogram")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Histogram Grayscale")
        fig_gray, hist_gray_values = calculate_and_plot_hist_grayscale(gray_image)
        st.pyplot(fig_gray)
        with st.expander("Lihat Nilai Angka Histogram Grayscale"):
            st.write(hist_gray_values)
            
    with col2:
        st.subheader("Histogram RGB")
        fig_rgb, hists_rgb_values = calculate_and_plot_hist_rgb(img_bgr)
        st.pyplot(fig_rgb)
        with st.expander("Lihat Nilai Angka Histogram RGB"):
            st.write("Blue:", hists_rgb_values['b'])
            st.write("Green:", hists_rgb_values['g'])
            st.write("Red:", hists_rgb_values['r'])

    st.markdown("---")

    # --- 2. THRESHOLDING DAN CITRA BINER ---
    st.header("2. Thresholding dan Citra Biner")
    
    # Menggunakan metode Otsu untuk menentukan threshold secara otomatis dari dua puncak
    # Ini adalah pendekatan standar untuk menemukan threshold optimal pada histogram bimodal
    thresh_val, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    st.info(f"Nilai Threshold yang didapat dari metode Otsu (dua puncak) adalah: **{int(thresh_val)}**")

    col1, col2 = st.columns(2)
    with col1:
        st.image(gray_image, caption="Citra Grayscale (Sebelum)", use_container_width=True)
    with col2:
        st.image(binary_image, caption="Citra Biner (Sesudah)", use_container_width=True)
        
    st.markdown("---")
    
    # --- 3. HISTOGRAM EQUALIZATION ---
    st.header("3. Histogram Equalization (Uniform)")
    
    # Lakukan ekualisasi
    equalized_image = cv2.equalizeHist(gray_image)
    
    # Hitung mean dan std dev
    mean_before = np.mean(gray_image)
    std_before = np.std(gray_image)
    mean_after = np.mean(equalized_image)
    std_after = np.std(equalized_image)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sebelum Ekualisasi")
        st.image(gray_image, caption="Citra Grayscale Original", use_container_width=True)
        st.write(f"**Mean:** {mean_before:.2f}")
        st.write(f"**Standard Deviasi:** {std_before:.2f}")
        fig_hist_before, _ = calculate_and_plot_hist_grayscale(gray_image)
        st.pyplot(fig_hist_before)

    with col2:
        st.subheader("Sesudah Ekualisasi")
        st.image(equalized_image, caption="Citra Hasil Ekualisasi", use_container_width=True)
        st.write(f"**Mean:** {mean_after:.2f}")
        st.write(f"**Standard Deviasi:** {std_after:.2f}")
        fig_hist_after, _ = calculate_and_plot_hist_grayscale(equalized_image)
        st.pyplot(fig_hist_after)
        
else:
    st.info("Silakan unggah sebuah gambar melalui panel di sebelah kiri untuk memulai.")

