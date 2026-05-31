import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 1. LOAD DATA (Kebal dari Error Path Cloud)
# ==========================================
@st.cache_data
def load_data():
    if os.path.exists("main_data.csv"):
        return pd.read_csv("main_data.csv")
    elif os.path.exists("dashboard/main_data.csv"):
        return pd.read_csv("dashboard/main_data.csv")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return pd.read_csv(os.path.join(BASE_DIR, "main_data.csv"))

df_clean = load_data()

# ==========================================
# 2. SIDEBAR INTERAKTIF
# ==========================================
st.sidebar.image("https://img.icons8.com/clouds/100/000000/wind.png")
st.sidebar.title("Navigasi & Filter")
st.sidebar.markdown("Dashboard analisis kualitas udara kota Beijing tahun **2016**.")

opsi_stasiun = ["All Stations"] + list(df_clean['station'].unique())
stasiun_pilihan = st.sidebar.selectbox(
    "Pilih Stasiun Pemantau:",
    options=opsi_stasiun,
    index=0
)

if stasiun_pilihan == "All Stations":
    df_filtered = df_clean
else:
    df_filtered = df_clean[df_clean['station'] == stasiun_pilihan]

# ==========================================
# 3. MAIN PAGE DASHBOARD
# ==========================================
st.title("🌤️ Air Quality Analysis Dashboard (2016)")
st.markdown("---")

# Menampilkan Ringkasan Angka (Metrics)
col1, col2 = st.columns(2)
with col1:
    st.metric("Stasiun Aktif", stasiun_pilihan)
with col2:
    st.metric("Rata-rata PM2.5 Wilayah", f"{df_filtered['PM2.5'].mean().round(2)} µg/m³")

st.markdown("### 📊 Hasil Visualisasi & Analisis Data")

# --- GRAFIK 1: Kategori Waktu ---
st.subheader("1. Rata-Rata Kadar PM2.5 Berdasarkan Kategori Waktu")

# Memastikan urutan Pagi, Siang, Malam rapi
rata_pm25_waktu = df_filtered.groupby('kategori_waktu')['PM2.5'].mean().reset_index()
rata_pm25_waktu['kategori_waktu'] = pd.Categorical(rata_pm25_waktu['kategori_waktu'], categories=['Pagi', 'Siang', 'Malam'], ordered=True)
rata_pm25_waktu = rata_pm25_waktu.sort_values('kategori_waktu')

fig, ax = plt.subplots(figsize=(8, 4))

# REVISI WARNA: Batang tertinggi diberi warna biru menonjol, sisanya abu-abu seragam
max_val1 = rata_pm25_waktu['PM2.5'].max()
colors1 = ['#1f77b4' if y == max_val1 else '#dcdde1' for y in rata_pm25_waktu['PM2.5']]

sns.barplot(x='kategori_waktu', y='PM2.5', data=rata_pm25_waktu, palette=colors1, hue='kategori_waktu', legend=False, ax=ax)
ax.set_xlabel("Kategori Waktu")
ax.set_ylabel("Rata-Rata PM2.5 (µg/m³)")
st.pyplot(fig)

# REVISI INSIGHT: Menambahkan penjelasan komprehensif di bawah grafik
st.markdown("""
> 💡 **Insight Analisis Waktu Harian:** Rata-rata kadar polusi PM2.5 menunjukkan variasi berdasarkan waktu harian. 
> Kadar polusi secara konsisten mencapai puncaknya pada waktu **Malam hari** dibandingkan pagi atau siang hari. 
> Hal ini dipengaruhi oleh penurunan suhu malam hari dan aktivitas inversi atmosfer yang memerangkap polutan di dekat permukaan tanah.
""")
st.markdown("<br>", unsafe_allow_html=True)

# --- GRAFIK 2: Kasus Tidak Sehat per Stasiun ---
st.subheader("2. Frekuensi Kasus Kualitas Udara 'Tidak Sehat' per Stasiun")
tidak_sehat_df = df_filtered[df_filtered['status_udara'] == 'Tidak Sehat']

if len(tidak_sehat_df) > 0:
    frekuensi_stasiun = tidak_sehat_df.groupby('station').size().reset_index(name='jumlah_kasus_tidak_sehat').sort_values(by='jumlah_kasus_tidak_sehat', ascending=False)
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    
    # REVISI WARNA: Batang tertinggi diberi warna merah menonjol, sisanya abu-abu seragam
    max_val2 = frekuensi_stasiun['jumlah_kasus_tidak_sehat'].max()
    colors2 = ['#d62728' if y == max_val2 else '#dcdde1' for y in frekuensi_stasiun['jumlah_kasus_tidak_sehat']]
    
    sns.barplot(x='jumlah_kasus_tidak_sehat', y='station', data=frekuensi_stasiun, palette=colors2, hue='station', legend=False, ax=ax2)
    ax2.set_xlabel("Jumlah Kasus / Frekuensi (Jam)")
    ax2.set_ylabel("Stasiun Pemantau")
    st.pyplot(fig2)
    
    # REVISI INSIGHT: Menambahkan penjelasan komprehensif di bawah grafik
    st.markdown("""
    > 💡 **Insight Analisis Kritis Wilayah:** Berdasarkan hasil pemetaan kondisi polusi (*manual clustering*), stasiun pemantau tertentu memiliki frekuensi jam dengan status kualitas udara **'Tidak Sehat'** yang jauh lebih tinggi. 
    > Warna merah menonjol menandakan area *hotspot* polusi paling kritis yang memerlukan intervensi kebijakan pengendalian emisi kendaraan dan industri secara lebih ketat.
    """)
else:
    st.info("Tidak ada kasus udara 'Tidak Sehat' pada kondisi stasiun terpilih.")

st.markdown("---")
st.caption("Proyek Akhir Belajar Analisis Data dengan Python")
