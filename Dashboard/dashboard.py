import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


csv_file_path = 'Dashboard/all_data.csv' 
data = pd.read_csv(csv_file_path)


data['dteday'] = pd.to_datetime(data['dteday'])
st.title('Bike Sharing Dashboard ✨')

# Sidebar for date range selection
st.sidebar.header('Rentang Waktu')
start_date = st.sidebar.date_input('Mulai', data['dteday'].min().date())
end_date = st.sidebar.date_input('Selesai', data['dteday'].max().date())

# Add image above date range
image_path = 'sepeda.jpeg' 
st.sidebar.image(image_path, caption='Bike Sharing', use_column_width=True)

# Filter data based on the selected date range
filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]

# menunjukkan total orders and total revenue
total_orders = filtered_data['cnt'].sum()
total_revenue = total_orders * 1.04  

st.subheader('Penyewaan Sepeda Harian')
st.metric('Total Penyewaan', total_orders)
st.metric('Total Pendapatan', f'AUD {total_revenue:,.2f}')

# time series of daily orders
fig, ax = plt.subplots()
ax.plot(filtered_data['dteday'], filtered_data['cnt'], label='Penyewaan Harian', marker='o', linestyle='-')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Best dan worst performing days
st.subheader('Hari Terbaik & Terburuk dalam Penyewaan Sepeda')
best_day = filtered_data.loc[filtered_data['cnt'].idxmax()]
worst_day = filtered_data.loc[filtered_data['cnt'].idxmin()]

col1, col2 = st.columns(2)
with col1:
    st.metric('Hari Terbaik', best_day['dteday'].strftime('%Y-%m-%d'), int(best_day['cnt']))
with col2:
    st.metric('Hari Terburuk', worst_day['dteday'].strftime('%Y-%m-%d'), int(worst_day['cnt']))

# Penjelasan tentang penyewaan sepeda
st.subheader('Tentang Penyewaan Sepeda')
st.write("""
Penyewaan sepeda memungkinkan pengguna untuk menyewa sepeda dari suatu tempat dan mengembalikannya di lokasi lain. Data yang tersedia mencakup jumlah sepeda yang disewa setiap hari, serta kondisi cuaca, hari kerja, dan lain-lain. Analisis ini membantu kita memahami pola penyewaan sepeda berdasarkan faktor lingkungan dan hari kerja.
""")

# rata-rata penyewaan sepeda berdasarkan cuaca
st.subheader('Rata-rata Penyewaan Sepeda Berdasarkan Cuaca')
avg_by_weather = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()

# Mapping cuaca to labels
weather_labels = {
    1: 'Cerah / Berawan',
    2: 'Berkabut / Awan Pecah',
    3: 'Hujan Ringan / Salju Ringan',
    4: 'Hujan Lebat / Badai Petir'
}
avg_by_weather['weathersit'] = avg_by_weather['weathersit'].map(weather_labels)

# Plot bar chart for average rentals by weather
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=avg_by_weather, ax=ax)
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Penyewaan')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
st.pyplot(fig)

# rata-rata penyewaan sepeda berdasarkan hari kerja atau bukan
st.subheader('Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja / Libur')
avg_by_workingday = filtered_data.groupby('workingday')['cnt'].mean().reset_index()

# Mapping workingday to labels
workingday_labels = {0: 'Hari Libur', 1: 'Hari Kerja'}
avg_by_workingday['workingday'] = avg_by_workingday['workingday'].map(workingday_labels)

# Plot bar chart for average rentals by working day
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=avg_by_workingday, ax=ax)
ax.set_xlabel('Hari')
ax.set_ylabel('Rata-rata Penyewaan')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja / Libur')
st.pyplot(fig)

# Penjelasan tentang output yang diberikan 
st.subheader('Penjelasan mengenai penyewaan sepeda berdasarkan cuaca dan hari kerja/libur')
st.write("""
Dalam barplot diatas menunjukkan bahwa kondisi cuaca yang cerah dan sedikit awan sangat mendukung aktivitas penyewaan sepeda. Pengguna cenderung lebih banyak menyewa sepeda ketika cuaca baik. Sedangkan Kondisi cuaca yang buruk seperti hujan ringan atau salju ringan memiliki dampak signifikan terhadap penurunan jumlah penyewaan sepeda. Hal ini mencerminkan bahwa pengguna cenderung menghindari menyewa sepeda dalam cuaca yang tidak bersahabat.
""")
st.write("""
Dari hasil barplot di atas dapat diketahui bahwa Jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan akhir pekan.
""")
