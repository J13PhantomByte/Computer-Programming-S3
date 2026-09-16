import pandas as pd

# Data dengan penulisan departemen yang berantakan
data = {'Nama': ['Fajar', 'Gita', 'Hani'],
'Dept': [' IT ', 'hrd', ' Finance ']}
df_karyawan = pd.DataFrame(data)

print("--- Data Sebelum Cleaning Teks ---")
# Terlihat spasi berantakan jika dicetak dalam bentuk list
print(df_karyawan['Dept'].tolist())

# 1. Menghapus spasi di awal dan akhir teks (.str.strip())
df_karyawan['Dept'] = df_karyawan['Dept'].str.strip()

# 2. Menyeragamkan menjadi huruf kapital semua (.str.upper())
df_karyawan['Dept'] = df_karyawan['Dept'].str.upper()

# 3. Mengganti istilah (Misal HRD diganti menjadi HR)
df_karyawan['Dept'] = df_karyawan['Dept'].replace('HRD', 'HR')

print("\n--- Data Setelah Cleaning Teks ---")
print(df_karyawan['Dept'].tolist())