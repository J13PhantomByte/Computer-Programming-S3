
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Membuat data mentah saham
data_saham = {
    'Date': ['15/01/2026', '16/01/2026', '17/01/2026',
             '18/01/2026', '19/01/2026', '20/01/2026',
             '21/01/2026'],
    'Harga_Tutup': [1500, 1520, 1480, 1550, 1600, 1580, 1620],
    'Volume': [1000, 1200, 900, 1500, 2000, 1800, 2200]
}

df_saham = pd.DataFrame(data_saham)

# 2. Konversi Date menjadi Datetime
df_saham['Date'] = pd.to_datetime(
    df_saham['Date'],
    format='%d/%m/%Y'
)

# 3. Menjadikan Date sebagai Index
df_saham.set_index('Date', inplace=True)

print("Data Saham:")
print(df_saham)

print("\nTipe Data:")
print(df_saham.dtypes)

# 4. Visualisasi Statis menggunakan Matplotlib
plt.figure(figsize=(10, 5))

plt.plot(
    df_saham.index,
    df_saham['Harga_Tutup'],
    marker='o',
    color='blue',
    linestyle='-'
)

plt.title("Pergerakan Harga Saham")
plt.xlabel("Tanggal")
plt.ylabel("Harga Penutupan")
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Visualisasi Interaktif menggunakan Plotly
df_plotly = df_saham.reset_index()

fig = px.line(
    df_plotly,
    x='Date',
    y='Volume',
    title='Volume Transaksi Interaktif',
    markers=True
)

fig.update_layout(
    xaxis_title='Tanggal',
    yaxis_title='Volume Transaksi',
    template='plotly_white'
)

# Simpan grafik sebagai HTML mandiri
fig.write_html(
    "grafik_saham.html",
    include_plotlyjs=True,
    auto_open=True
)

print("Grafik berhasil dibuat!")