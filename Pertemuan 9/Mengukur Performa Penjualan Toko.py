import pandas as pd
import numpy as np

# 1. Membuat Data Dummy Penjualan Harian (dalam juta rupiah)
data_penjualan = [12, 15, 14, 13, 16, 50, 14, 15, 12, 13] # Angka 50 adalah outlier
df = pd.DataFrame({'Penjualan_Juta': data_penjualan})

# 2. Menggunakan fungsi deskriptif bawaan Pandas
print("--- Ringkasan Statistik Penjualan ---")
print(df.describe())

# 3. Menghitung manual
mean = df['Penjualan_Juta'].mean()
median = df['Penjualan_Juta'].median()
std_dev = df['Penjualan_Juta'].std()

print(f"\nRata-rata (Mean) : {mean} Juta")
print(f"Nilai Tengah (Median): {median} Juta")
print(f"Standar Deviasi : {std_dev:.2f} Juta")