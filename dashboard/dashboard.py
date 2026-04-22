import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# -------------------
# PAGE CONFIGURATION
# -------------------
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# -------------------
# LOAD DATA
# -------------------
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'main_data.csv')

    if not os.path.exists(file_path):
        file_path = 'main_data.csv'

    df = pd.read_csv(file_path)
    return df

df = load_data()

# Validasi data
if df.empty:
    st.error("Data tidak ditemukan.")
    st.stop()

# -------------------
# SIDEBAR FILTER
# -------------------
st.sidebar.header("🔍 Filter Data")

# Filter season
if 'season' in df.columns:
    season = st.sidebar.multiselect(
        "Pilih Season:",
        options=df['season'].unique(),
        default=df['season'].unique()
    )
    df = df[df['season'].isin(season)]

# Filter year
if 'yr' in df.columns:
    year = st.sidebar.multiselect(
        "Pilih Tahun:",
        options=df['yr'].unique(),
        default=df['yr'].unique()
    )
    df = df[df['yr'].isin(year)]

# -------------------
# TIME CATEGORY
# -------------------
def categorize_hour(hour):
    if 0 <= hour < 5:
        return 'Dini Hari'
    elif 5 <= hour < 11:
        return 'Pagi Hari'
    elif 11 <= hour < 15:
        return 'Siang Hari'
    elif 15 <= hour < 18:
        return 'Sore Hari'
    else:
        return 'Malam Hari'

df['time_category'] = df['hr'].apply(categorize_hour)


# -------------------
# MAIN DASHBOARD
# -------------------
st.title("🚲 Bike Sharing Analytics Dashboard")
st.markdown("Dashboard ini menampilkan pola penggunaan sepeda berdasarkan waktu dan tipe pengguna untuk memahami karakteristik penggunaan sepeda dalam aktivitas sehari-hari")
st.divider()

# PERFORMANCE METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Penggunaan", f"{df['cnt'].sum():,}")

with col2:
    st.metric("Rata-rata per Jam", f"{df['cnt'].mean():.0f}")

with col3:
    st.metric("Peak Penggunaan", f"{df['cnt'].max():,}")

st.divider()

# VISUALIZATIONS
col1, col2 = st.columns(2)

# 🔹 Weekday vs Weekend
with col2:
    st.subheader("Weekday vs Weekend")

    # Memastikan mapping benar
    df['day_type'] = df['workingday'].map({
        'Yes': 'Weekday',
        'No': 'Weekend'
    })

    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='hr', y='cnt', hue='day_type', ax=ax)

    ax.set_title("Pola Penggunaan Sepeda: Weekday vs Weekend")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.grid(True, linestyle='--', alpha=0.3)

    st.pyplot(fig)

# 🔹 Casual vs Registered
with col1:
    st.subheader("Casual vs Registered")

    hourly_users = df.groupby('hr')[['casual','registered']].mean()

    fig, ax = plt.subplots()

    ax.plot(hourly_users.index, hourly_users['casual'], label='Casual')
    ax.plot(hourly_users.index, hourly_users['registered'], label='Registered')
    ax.legend()

    ax.set_title("Pola Penggunaan Sepeda: Casual vs Registered")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Pengguna")
    ax.grid(True, linestyle='--', alpha=0.3)

    st.pyplot(fig)

# INSIGHT
with st.expander("📌 Analysis Insight", expanded=True):
    st.write("""
    1. **Pola Waktu Penggunaan**  
    Penggunaan sepeda menunjukkan pola yang jelas, dengan peningkatan pada pagi dan sore hari, terutama pada hari kerja. Hal ini menunjukkan penggunaan sepeda sebagai sarana transportasi utama.

    2. **Perbedaan Hari Kerja vs Akhir Pekan**  
    Pada hari kerja, terdapat dua puncak penggunaan, yaitu jam berangkat dan pulang kerja, sedangkan pada akhir pekan cenderung lebih stabil tanpa peningkatan yang signifikan.

    3. **Perilaku Pengguna**  
    Pengguna *registered* mendominasi penggunaan, terutama pada jam-jam sibuk. Sementara itu, pengguna *casual* cenderung bersepeda pada siang hingga sore hari untuk aktivitas rekreasi.
    """)