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
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return pd.read_csv(os.path.join(BASE_DIR, "main_data.csv"))

df_clean = load_data()

# ==========================================
# 2. SIDEBAR INTERAKTIF (Syarat Nilai Tinggi!)
# ==========================================
st.sidebar.image("https://img.icons8.com/clouds/100/000000/wind.png")
st.sidebar.title("Navigasi & Filter")
st.sidebar.markdown("Dashboard analisis kualitas udara kota Beijing tahun **2016**.")

# Widget pilihan stasiun (Bisa pilih lebih dari satu)
stasiun_pilihan = st.sidebar.multiselect(
    "Pilih Stasiun Pemantau:",
    options=df_clean['station'].unique(),
    default=df_clean['station'].unique()[:3] # Default memunculkan 3 stasiun awal
)

# Proses penyaringan data secara realtime berdasarkan ketukan user
df_filtered = df_clean[df_clean['station'].isin(stasiun_pilihan)]

# ==========================================
# 3. MAIN PAGE DASHBOARD
# ==========================================
st.title("🌤️ Air Quality Analysis Dashboard (2016)")
st.markdown("---")

# Menampilkan Ringkasan Angka (Metrics)
col1, col2 = st.columns(2)
with col1:
    st.metric("Rata-rata PM2.5 Wilayah Terpilih", f"{df_filtered['PM2.5'].mean().round(2)} µg/m³")
with col2:
    st.metric("Total Record Data", f"{len(df_filtered)} Jam")

st.markdown("### 📊 Hasil Visualisasi Data")

# --- GRAFIK 1: Kategori Waktu ---
st.subheader("1. Rata-Rata Kadar PM2.5 Berdasarkan Kategori Waktu")
rata_pm25_waktu = df_filtered.groupby('kategori_waktu')['PM2.5'].mean().reset_index()

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x='kategori_waktu', y='PM2.5', data=rata_pm25_waktu, order=['Pagi', 'Siang', 'Malam'], palette='Blues_r', ax=ax)
ax.set_xlabel("Kategori Waktu")
ax.set_ylabel("Rata-Rata PM2.5 (µg/m³)")
st.pyplot(fig)

# --- GRAFIK 2: Kasus Tidak Sehat per Stasiun ---
st.subheader("2. Frekuensi Kasus Kualitas Udara 'Tidak Sehat' per Stasiun")
tidak_sehat_df = df_filtered[df_filtered['status_udara'] == 'Tidak Sehat']
frekuensi_stasiun = tidak_sehat_df.groupby('station').size().reset_index(name='jumlah_kasus_tidak_sehat').sort_values(by='jumlah_kasus_tidak_sehat', ascending=False)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x='jumlah_kasus_tidak_sehat', y='station', data=frekuensi_stasiun, palette='Reds_r', ax=ax2)
ax2.set_xlabel("Jumlah Kasus / Frekuensi (Jam)")
ax2.set_ylabel("Stasiun Pemantau")
st.pyplot(fig2)

st.markdown("---")
st.caption("Proyek Akhir Belajar Analisis Data dengan Python")
