import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting tampilan halaman
st.set_page_config(page_title="Dashboard Konsumsi Daya Listrik", layout="wide")

# Header
st.markdown("""
    <h1 style='text-align: center; color: navy;'>⚡ Dashboard Konsumsi Daya Listrik & Faktor Cuaca</h1>
    <h5 style='text-align: center; color: grey;'>📚 Analisis dari Dataset PowerConsumption_Final</h5>
    <hr>
""", unsafe_allow_html=True)

# Sidebar untuk opsi
st.sidebar.header("🔧 Opsi Dashboard")
feature_selected = st.sidebar.selectbox("Pilih Fitur Distribusi:", ['Temperature', 'Humidity', 'HeatIndex'])

# Load data
try:
    df = pd.read_csv('powerconsumption_final.csv')
    st.sidebar.success("✅ Data berhasil dimuat")
except Exception as e:
    st.sidebar.error(f"❌ Gagal memuat data: {e}")
    st.stop()

# Hitung total konsumsi daya
df['TotalPowerConsumption'] = df['PowerConsumption_Zone1'] + df['PowerConsumption_Zone2'] + df['PowerConsumption_Zone3']

# Tampilkan 5 data pertama
with st.expander("📂 Klik untuk lihat 5 data pertama"):
    st.dataframe(df.head())

# Section 1 - Distribution
st.subheader(f"📊 Distribusi {feature_selected}")
fig1, ax1 = plt.subplots(figsize=(8,4))
sns.histplot(df[feature_selected], bins=30, kde=True, color='skyblue', ax=ax1)
ax1.set_title(f'Distribusi {feature_selected}', fontsize=14)
st.pyplot(fig1)

# Section 2 - Comparison Konsumsi Tiap Zona
st.subheader("🏭 Perbandingan Rata-rata Konsumsi Tiap Zona")
avg_zones = df[['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']].mean()
fig2, ax2 = plt.subplots(figsize=(7,5))
avg_zones.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'], ax=ax2)
ax2.set_ylabel('Konsumsi Daya (kWh)')
ax2.set_title('Rata-rata Konsumsi Tiap Zona')
st.pyplot(fig2)

# Section 3 - Composition Proporsi Konsumsi
st.subheader("🧩 Komposisi Proporsi Konsumsi Daya")
fig3, ax3 = plt.subplots(figsize=(6,6))
ax3.pie(avg_zones, labels=avg_zones.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
ax3.set_title("Persentase Konsumsi Daya per Zona")
ax3.axis('equal')
st.pyplot(fig3)

# Section 4 - Relationship HeatIndex vs Total Power Consumption
st.subheader("🔗 Korelasi Heat Index dengan Konsumsi Total")
fig4, ax4 = plt.subplots(figsize=(8,5))
sns.scatterplot(x=df['HeatIndex'], y=df['TotalPowerConsumption'], ax=ax4)
ax4.set_xlabel('Heat Index')
ax4.set_ylabel('Total Power Consumption (kWh)')
ax4.set_title('Scatter Plot: HeatIndex vs Total Consumption')
st.pyplot(fig4)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 - [Nama Anda] | Sistem Informasi A 📘</p>", unsafe_allow_html=True)
