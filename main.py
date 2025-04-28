import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting tampilan halaman
st.set_page_config(page_title="Dashboard Konsumsi Daya Listrik", layout="wide")

# Header dengan desain yang lebih menarik dan warna custom
st.markdown("""
    <style>
        h1 {
            color: #FF6F61;  /* Ganti dengan warna yang diinginkan */
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 30px;  /* Ukuran font lebih kecil */
        }
        h5 {
            color: #3E4A59;  /* Warna lebih gelap untuk subheader */
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 16px;  /* Ukuran font lebih kecil */
        }
        .header {
            text-align: center;
            font-size: 28px;  /* Ukuran font lebih kecil */
            background-color: #6C67FC;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
        }
    </style>
    <div class="header">
        <h1>⚡ Dashboard Konsumsi Daya Listrik & Faktor Cuaca</h1>
        <h5>📊 Analisis Konsumsi Daya Listrik Berdasarkan Faktor Cuaca</h5>
    </div>
""", unsafe_allow_html=True)

# Sidebar untuk filter dan input
st.sidebar.header("🔧 Opsi Dashboard")

# Filter pilihan data
feature_selected = st.sidebar.selectbox("Pilih Fitur untuk Distribusi:", ['Temperature', 'Humidity', 'HeatIndex'])
scatter_feature = st.sidebar.selectbox("Pilih Fitur untuk Scatter Plot:", ['HeatIndex', 'Temperature', 'Humidity', 'WindSpeed'])

# Memuat Data
try:
    df = pd.read_csv('powerconsumption_final.csv')
except Exception as e:
    st.stop()

# Menambahkan Total Konsumsi Daya
df['TotalPowerConsumption'] = df['PowerConsumption_Zone1'] + df['PowerConsumption_Zone2'] + df['PowerConsumption_Zone3']

# Tampilkan Data Sample
with st.expander("📂 Klik untuk melihat 5 data pertama") :
    st.dataframe(df.head())

# 1. Distribusi Data Fitur
st.subheader(f"📊 Distribusi {feature_selected}")
fig1, ax1 = plt.subplots(figsize=(6, 4))  # Ukuran lebih kecil
sns.histplot(df[feature_selected], bins=30, kde=True, color='skyblue', ax=ax1)
ax1.set_title(f'Distribusi {feature_selected}', fontsize=8, color='#2d5c8c')  # Ukuran font kecil
st.pyplot(fig1)

# 2. Perbandingan Konsumsi Daya Tiap Zona
st.subheader("🏭 Perbandingan Rata-rata Konsumsi Daya Tiap Zona")
avg_zones = df[['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']].mean()
fig2, ax2 = plt.subplots(figsize=(5, 4))  # Ukuran lebih kecil
avg_zones.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'], ax=ax2)
ax2.set_ylabel('Konsumsi Daya (kWh)', fontsize=8)  # Ukuran font kecil
ax2.set_title('Rata-rata Konsumsi Daya per Zona', fontsize=8, color='#2d5c8c')  # Ukuran font kecil
ax2.grid(axis='y', linestyle='--', alpha=0.5)
st.pyplot(fig2)

# 3. Komposisi Konsumsi Daya per Zona
st.subheader("🧩 Komposisi Konsumsi Daya per Zona")
fig3, ax3 = plt.subplots(figsize=(5, 5))  # Ukuran lebih kecil
ax3.pie(avg_zones, labels=avg_zones.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
ax3.set_title("Persentase Konsumsi Daya per Zona", fontsize=8, color='#2d5c8c')  # Ukuran font kecil
ax3.axis('equal')
st.pyplot(fig3)

# 4. Korelasi antara Pilihan Fitur dengan Total Power Consumption
st.subheader(f"🔗 Korelasi antara {scatter_feature} dan Total Konsumsi Daya")
fig4, ax4 = plt.subplots(figsize=(5, 4))  # Ukuran lebih kecil
sns.scatterplot(x=df[scatter_feature], y=df['TotalPowerConsumption'], ax=ax4, color='#ff7f0e')
ax4.set_xlabel(scatter_feature, fontsize=8, color='#5f6368')  # Ukuran font kecil
ax4.set_ylabel('Total Power Consumption (kWh)', fontsize=8, color='#5f6368')  # Ukuran font kecil
ax4.set_title(f'Scatter Plot: {scatter_feature} vs Total Consumption', fontsize=8, color='#2d5c8c')  # Ukuran font kecil
st.pyplot(fig4)
