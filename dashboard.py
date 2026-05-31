import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return pd.read_csv(os.path.join(BASE_DIR, "main_data.csv"))

df_filtered = load_data()

st.title("🌤️ Air Quality Analysis Dashboard (2016)")
st.markdown("---")

st.subheader("1. Rata-Rata Kadar PM2.5 Berdasarkan Kategori Waktu")
rata_pm25_waktu = df_filtered.groupby('kategori_waktu')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x='kategori_waktu', y='PM2.5', data=rata_pm25_waktu, order=['Pagi', 'Siang', 'Malam'], palette='Blues_r', ax=ax)
st.pyplot(fig)

st.subheader("2. Frekuensi Kasus Kualitas Udara 'Tidak Sehat' per Stasiun")
tidak_sehat_df = df_filtered[df_filtered['status_udara'] == 'Tidak Sehat']
frekuensi_stasiun = tidak_sehat_df.groupby('station').size().reset_index(name='jumlah_kasus_tidak_sehat').sort_values(by='jumlah_kasus_tidak_sehat', ascending=False)
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x='jumlah_kasus_tidak_sehat', y='station', data=frekuensi_stasiun, palette='Reds_r', ax=ax2)
st.pyplot(fig2)