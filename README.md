# 🚲 Bike Sharing Dashboard

Dashboard interaktif berbasis **Streamlit** untuk menganalisis data penyewaan sepeda (*bike sharing*). Dashboard ini menampilkan tren penyewaan dari waktu ke waktu, jam tersibuk, pengaruh musim, serta perbandingan pelanggan *registered* dan *casual*.

## ✨ Fitur

- **Filter rentang waktu** melalui sidebar untuk menyesuaikan seluruh visualisasi.
- **Ringkasan metrik**: total penyewaan sepeda, total pelanggan *registered*, dan total pelanggan *casual*.
- **Tren penyewaan harian** dalam beberapa tahun terakhir.
- **Analisis per jam**: jam dengan penyewa terbanyak dan tersedikit.
- **Analisis per musim**: musim dengan penyewaan tertinggi.
- **Perbandingan pelanggan** *registered* vs *casual* dalam bentuk pie chart.

## 📁 Struktur Proyek

```
dashboard/
├── dashboard.py       # Aplikasi utama Streamlit
├── day_clean.csv      # Data penyewaan harian (sudah dibersihkan)
├── hour_clean.csv     # Data penyewaan per jam (sudah dibersihkan)
├── requirements.txt   # Daftar dependensi Python
└── README.md
```

## 🛠️ Teknologi

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

## 🚀 Cara Menjalankan

1. **Clone repositori**

   ```bash
   git clone https://github.com/Lidafatma/dashboard.git
   cd dashboard
   ```

2. **(Opsional) Buat virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependensi**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan dashboard**

   ```bash
   streamlit run dashboard.py
   ```

5. Buka browser di `http://localhost:8501`.

> **Catatan:** `dashboard.py` membaca dataset langsung dari URL raw GitHub repositori ini, sehingga dibutuhkan koneksi internet saat dashboard dijalankan.

## 📊 Dataset

Data yang digunakan adalah data penyewaan sepeda yang sudah melalui proses pembersihan (*data cleaning*):

| File | Deskripsi |
| --- | --- |
| `day_clean.csv` | Jumlah penyewaan sepeda per hari |
| `hour_clean.csv` | Jumlah penyewaan sepeda per jam |

Kolom utama yang dipakai dalam dashboard:

| Kolom | Keterangan |
| --- | --- |
| `dteday` | Tanggal pencatatan |
| `hours` | Jam pencatatan (0–23) |
| `season` | Musim |
| `casual` | Jumlah penyewa non-member |
| `registered` | Jumlah penyewa terdaftar (member) |
| `count_cr` | Total penyewaan (casual + registered) |

## 👤 Author

**Lidafatma** — [@Lidafatma](https://github.com/Lidafatma)
