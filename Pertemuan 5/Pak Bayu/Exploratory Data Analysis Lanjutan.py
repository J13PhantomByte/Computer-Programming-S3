import pandas as pd

# 1. Membuat Dataset Karyawan
data = {
'Nama': ['Andi', 'Budi', 'Citra', 'Diana', 'Eka', 'Fajar'],
'Departemen': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT'],
'Gender': ['L', 'L', 'P', 'P', 'L', 'L'],
'Pengalaman_Thn': [2, 5, 3, 10, 1, 8],
'Gaji_Juta': [6.0, 7.5, 7.0, 15.0, 4.5, 12.0]
}
df = pd.DataFrame(data)

# 2. Menggunakan Groupby untuk agregasi
print("--- Rata-rata Gaji per Departemen ---")
# Dikelompokkan berdasarkan 'Departemen', lalu dihitung rata-rata (.mean) 'Gaji_Juta'
rata_gaji = df.groupby('Departemen')['Gaji_Juta'].mean()
print(rata_gaji)

# 3. Menghitung jumlah karyawan per departemen
print("\n--- Jumlah Karyawan per Departemen ---")
jumlah_karyawan = df.groupby('Departemen')['Nama'].count()
print(jumlah_karyawan)


# Membuat Pivot Table Karyawan

# Membuat Pivot Table
# values = Kolom yang mau dihitung angkanya
# index = Kategori untuk baris (ke bawah)
# columns = Kategori untuk kolom (ke samping)
# aggfunc = Fungsi perhitungannya (mean, sum, count, dll)
tabel_pivot = pd.pivot_table(
df,
values='Gaji_Juta',
index='Departemen',
columns='Gender',
aggfunc='mean',
fill_value=0 # Mengisi nilai kosong/NaN dengan angka 0
)

print("--- Pivot Table Rata-rata Gaji (Departemen vs Gender) ---")
print(tabel_pivot)

# Hubungan Pengalaman Kerja vs Gaji

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))

# Membuat Scatter Plot
# x = sumbu horizontal, y = sumbu vertikal
# hue = memberi warna berbeda berdasarkan kategori departemen
sns.scatterplot(
data=df,
x='Pengalaman_Thn',
y='Gaji_Juta',
hue='Departemen',
s=100 # s adalah ukuran (size) titik
)

plt.title("Hubungan Pengalaman Kerja dan Gaji Karyawan")
plt.xlabel("Pengalaman (Tahun)")
plt.ylabel("Gaji (Juta Rupiah)")
plt.grid(True, linestyle='--', alpha=0.6) # Menambah garis bantu

plt.show()