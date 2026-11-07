PRAKTIKUM 10 - SSD1030
Tahap 2: Latih & Ekspor Model
Tahap 3: Aplikasi Prediksi Kelulusan dengan Streamlit

CARA MENJALANKAN:
1. Buka folder ini di VS Code.
2. Instal library:
   pip install -r requirements.txt
3. Latih model:
   python 1_latih_model.py
4. Jalankan aplikasi:
   streamlit run app.py

PENGUJIAN SESUAI MODUL:
- Pengujian 1: IPK 3.8, Total SKS 150 -> tampilan hijau (LULUS TEPAT WAKTU).
- Pengujian 2: ubah IPK menjadi 2.5, Total SKS tetap 150 -> tampilan merah (TIDAK LULUS).

Catatan: Model adalah demonstrasi berdasarkan lima data contoh dari modul praktikum.
