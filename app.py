import streamlit as st
import joblib

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Prediksi Kelulusan", page_icon="🎓")
st.title("🎓 Sistem Prediksi Kelulusan Mahasiswa")
st.write(
    "Masukkan IPK dan total SKS untuk melihat hasil prediksi kelulusan."
)

# 2. Load model hasil pelatihan Tahap 2
@st.cache_resource
def load_model():
    return joblib.load("model_kelulusan.pkl")

try:
    model = load_model()
except FileNotFoundError:
    st.error("File model tidak ditemukan. Jalankan `python 1_latih_model.py` terlebih dahulu.")
    st.stop()

# 3. Form input
with st.form("form_prediksi"):
    st.subheader("Masukkan Data Mahasiswa")
    ipk = st.number_input(
        "IPK (0.0 - 4.0)",
        min_value=0.0,
        max_value=4.0,
        value=3.8,
        step=0.1,
        format="%.1f"
    )
    sks = st.number_input(
        "Total SKS",
        min_value=0,
        max_value=200,
        value=150,
        step=1
    )
    tombol = st.form_submit_button("Prediksi Kelulusan")

# 4. Tampilkan hasil hanya setelah tombol ditekan
if tombol:
    hasil = int(model.predict([[ipk, sks]])[0])
    st.divider()
    st.subheader("Hasil Prediksi")

    if hasil == 1:
        st.success(
            f"Mahasiswa dengan IPK {ipk:.1f} dan SKS {sks} "
            "diprediksi LULUS TEPAT WAKTU."
        )
    else:
        st.error(
            f"Mahasiswa dengan IPK {ipk:.1f} dan SKS {sks} "
            "diprediksi TIDAK LULUS."
        )
