import pandas as pd
import numpy as np

# 1. Membuat DataFrame Kotor
data_mentah = {
'ID': ['K01', 'K02', 'K03', 'K01', 'K04', 'K05'], # K01 muncul 2x
'Nama': ['Andi', 'Budi', 'Citra', 'Andi', 'Diana', 'Eka'],
'Umur': [25, np.nan, 22, 25, 28, np.nan], # Ada 2 data kosong
'Gaji': [5000000, 6500000, 7000000, 5000000, np.nan, 4500000]
}
df = pd.DataFrame(data_mentah)

print("--- Data Mentah (Kotor) ---")
print(df)

# 2. Cek dan Hapus Data Duplikat
jumlah_duplikat = df.duplicated().sum()
print(f"\nDitemukan {jumlah_duplikat} baris data duplikat.")

# Menghapus duplikat secara permanen dengan inplace=True
df.drop_duplicates(inplace=True)
print("\n--- Data Setelah Duplikat Dihapus ---")
print(df)

# Cek di kolom mana saja terdapat data kosong
print("--- Pengecekan Missing Values ---")
print(df.isnull().sum())

# OPSi A: Menghapus baris yang memiliki NaN
# df_hapus = df.dropna()
# print(df_hapus)

# OPSi B: Imputasi (Mengisi nilai yang kosong) - Ini yang sering dipakai!
# 1. Mengisi umur kosong dengan nilai rata-rata (mean)
rata_umur = df['Umur'].mean()
df['Umur'] = df['Umur'].fillna(rata_umur)

# 2. Mengisi gaji kosong dengan nilai spesifik (misal: UMR 4.500.000)
df['Gaji'] = df['Gaji'].fillna(4500000)

print("\n--- Data Setelah Missing Values Diisi ---")
print(df)