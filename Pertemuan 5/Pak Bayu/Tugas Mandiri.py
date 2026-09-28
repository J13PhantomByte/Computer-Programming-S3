import pandas as pd

# 1. Membuat Dataset Properti / Perumahan
data_rumah = {
    'Lokasi': ['Pusat', 'Pinggiran', 'Pusat', 'Pusat', 'Pinggiran', 'Pusat', 'Pinggiran', 'Pinggiran'],
    'Tipe': ['Minimalis', 'Mewah', 'Mewah', 'Minimalis', 'Minimalis', 'Mewah', 'Mewah', 'Minimalis'],
    'Luas_Tanah': [120, 300, 250, 100, 90, 400, 280, 85],
    'Harga_Milyar': [1.5, 3.2, 4.0, 1.2, 0.8, 10.5, 2.9, 0.7]
}

df_rumah = pd.DataFrame(data_rumah)

print("--- Dataset Rumah ---")
print(df_rumah)


# ==========================================================
# 2. GROUPBY & PIVOT TABLE
# ==========================================================

# Menghitung total nilai aset per Lokasi
print("\n--- Total Nilai Aset per Lokasi ---")

total_aset = df_rumah.groupby('Lokasi')['Harga_Milyar'].sum()

print(total_aset)


# Membuat Pivot Table
# values = kolom yang dihitung
# index = kategori untuk baris
# columns = kategori untuk kolom
# aggfunc = fungsi perhitungan
tabel_pivot = pd.pivot_table(
    df_rumah,
    values='Harga_Milyar',
    index='Lokasi',
    columns='Tipe',
    aggfunc='mean',
    fill_value=0
)

print("\n--- Pivot Table Rata-rata Harga Rumah ---")
print(tabel_pivot)


# ==========================================================
# 3. SCATTER PLOT
# ==========================================================

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))

# Membuat Scatter Plot
# x = Luas Tanah
# y = Harga Rumah
# hue = membedakan warna berdasarkan Tipe rumah
sns.scatterplot(
    data=df_rumah,
    x='Luas_Tanah',
    y='Harga_Milyar',
    hue='Tipe',
    s=100
)

plt.title("Hubungan Luas Tanah dan Harga Rumah")
plt.xlabel("Luas Tanah (m²)")
plt.ylabel("Harga (Miliar Rupiah)")
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()


# ==========================================================
# 4. HEATMAP KORELASI
# ==========================================================

# Mengambil hanya kolom numerik
data_numerik = df_rumah[['Luas_Tanah', 'Harga_Milyar']]

# Menghitung matriks korelasi
korelasi = data_numerik.corr()

print("\n--- Matriks Korelasi ---")
print(korelasi)

# Membuat Heatmap
plt.figure(figsize=(6, 4))

sns.heatmap(
    korelasi,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Heatmap Korelasi Luas Tanah dan Harga Rumah")
plt.show()