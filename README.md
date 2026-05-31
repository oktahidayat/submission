# submission
# Air Quality Analysis Dashboard 🌤️

Proyek ini adalah Dashboard Interaktif Analisis Kualitas Udara di Kota Beijing untuk tahun 2016. Dashboard ini dibangun menggunakan Python dan Streamlit untuk memenuhi kriteria submission proyek akhir kelas Belajar Analisis Data dengan Python.

## 👥 Identitas Pengembang
* **Nama:** Okta Hidayat 
* **Universitas:** Politeknik Negeri Banyuwangi
* **Program:** Teknologi Rekayasa Perangkat Lunak

🛠️ Panduan Menjalankan Dashboard di Lokal (Localhost)
Ikuti langkah-langkah di bawah ini untuk mengeksekusi aplikasi di komputer Anda:

1. Masuk ke Direktori Proyek
Buka Terminal atau Command Prompt (CMD), lalu arahkan ke dalam folder utama tempat Anda mengekstrak submission ini:
```
Bash
cd jalur/ke/folder/submission
```

2. Membuat & Menyiapkan Virtual Environment
Buat sebuah lingkungan virtual baru terisolasi agar library tidak bentrok dengan sistem global komputer Anda:
```
Bash
pip install -r requirements.txt
```

3. Mengaktifkan Virtual Environment
Aktifkan environment yang baru saja dibuat berdasarkan sistem operasi yang Anda gunakan:
- Windows (Command Prompt / CMD):
```
DOS
venv\Scripts\activate.bat
```
- Windows (PowerShell):
```
PowerShell
venv\Scripts\Activate.ps1
```
- macOS/Linux:
```
Bash
source venv/bin/activate
```

4. Instalasi Dependencies (Libraries)
Pastikan virtual environment telah aktif, kemudian instal semua pustaka/library Python yang tercantum di dalam berkas requirements.txt:
```
Bash
pip install -r requirements.txt
```

5. Menjalankan Aplikasi Streamlit
Jalankan perintah di bawah ini untuk meluncurkan dashboard interaktif:
```
streamlit run dashboard/dashboard.py
```
Setelah perintah dijalankan, sistem akan otomatis membuka browser default Anda dan mengarahkannya ke alamat lokal: http://localhost:8501.
