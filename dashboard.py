import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur konfigurasi halaman agar menggunakan mode wide (lebar)
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")

sns.set(style='darkgrid')

def get_total_count_by_hour_df(hour_df):
    hour_count_df = hour_df.groupby(by="hours").agg({"count_cr": ["sum"]})
    return hour_count_df

def count_by_day_df(day_df):
    day_df_count_2011 = day_df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return day_df_count_2011

def total_registered_df(day_df):
    reg_df = day_df.groupby(by="dteday").agg({
        "registered": "sum"
    })
    reg_df = reg_df.reset_index()
    reg_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
    return reg_df

def total_casual_df(day_df):
    cas_df = day_df.groupby(by="dteday").agg({
        "casual": ["sum"]
    })
    cas_df = cas_df.reset_index()
    cas_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
    return cas_df

def sum_order(hour_df):
    sum_order_items_df = hour_df.groupby("hours").count_cr.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

def macem_season(day_df): 
    season_df = day_df.groupby(by="season").count_cr.sum().reset_index() 
    return season_df

# Load Data
days_df = pd.read_csv("https://raw.githubusercontent.com/Lidafatma/dashboard/main/day_clean.csv")
hours_df = pd.read_csv("https://raw.githubusercontent.com/Lidafatma/dashboard/main/hour_clean.csv")

datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(drop=True, inplace=True)    

hours_df.sort_values(by="dteday", inplace=True)
hours_df.reset_index(drop=True, inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hours_df[column] = pd.to_datetime(hours_df[column])

min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()

min_date_hour = hours_df["dteday"].min()
max_date_hour = hours_df["dteday"].max()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image1_hH9B4gs.jpg", width=200)
    st.markdown("---")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days]
    )

# Filter Data berdasarkan Sidebar
main_df_days = days_df[(days_df["dteday"] >= pd.to_datetime(start_date)) & 
                       (days_df["dteday"] <= pd.to_datetime(end_date))]

main_df_hour = hours_df[(hours_df["dteday"] >= pd.to_datetime(start_date)) & 
                        (hours_df["dteday"] <= pd.to_datetime(end_date))]

# Proses Data dengan Fungsi
hour_count_df = get_total_count_by_hour_df(main_df_hour)
day_df_count_2011 = count_by_day_df(main_df_days)
reg_df = total_registered_df(main_df_days)
cas_df = total_casual_df(main_df_days)
sum_order_items_df = sum_order(main_df_hour)
season_df = macem_season(main_df_days) # Menggunakan main_df_days agar konsisten dengan musim harian

# --- MAIN DASHBOARD ---
st.header('Bike Sharing Dashboard 🚲✨')

# 1. METRICS
st.subheader('Daily Sharing Summary')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = main_df_days.count_cr.sum()
    st.metric("Total Sharing Bike", value=f"{total_orders:,}")

with col2:
    total_sum_reg = reg_df.register_sum.sum()
    st.metric("Total Registered", value=f"{total_sum_reg:,}")

with col3:
    total_sum_cas = cas_df.casual_sum.sum()
    st.metric("Total Casual", value=f"{total_sum_cas:,}")

st.markdown("---")

# 2. PERFORMA PENJUALAN PERUSAHAAN
st.subheader("Performa Penjualan Perusahaan dalam Beberapa Tahun Terakhir")

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(
    main_df_days["dteday"],
    main_df_days["count_cr"],
    marker='o', 
    linewidth=1.5,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10)
st.pyplot(fig)

st.markdown("---")

# 3. JAM PENYEWAAN TERBANYAK & TERSEDIKIT
st.subheader("Jam Berapa yang Paling Banyak dan Paling Sedikit Disewa?")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

sns.barplot(x="hours", y="count_cr", data=sum_order_items_df.head(5), palette=["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3"], ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Hours", fontsize=12)
ax[0].set_title("Jam dengan Banyak Penyewa", loc="center", fontsize=14)
ax[0].tick_params(axis='y', labelsize=10)
ax[0].tick_params(axis='x', labelsize=10)
 
sns.barplot(x="hours", y="count_cr", data=sum_order_items_df.sort_values(by="hours", ascending=True).head(5), palette=["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9"], ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Hours", fontsize=12)
ax[1].set_title("Jam dengan Sedikit Penyewa", loc="center", fontsize=14)
ax[1].tick_params(axis='y', labelsize=10)
ax[1].tick_params(axis='x', labelsize=10)

st.pyplot(fig)

st.markdown("---")

# Layout 2 Kolom untuk Grafik Musim & Perbandingan Customer agar Rapi
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Musim dengan Penyewaan Terbanyak")
    colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9"]
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(
        y="count_cr", 
        x="season",
        data=season_df.sort_values(by="count_cr", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    st.pyplot(fig)

with col_right:
    st.subheader("Perbandingan Registered vs Casual")
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    
    # Membuat nilai pie chart dinamis berdasarkan data terfilter
    labels = ['Casual', 'Registered']
    sizes = [total_sum_cas, total_sum_reg]
    explode = (0, 0.1) 

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=["#D3D3D3", "#90CAF9"],
            shadow=True, startangle=90)
    ax1.axis('equal') 
    st.pyplot(fig1)
