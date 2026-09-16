import numpy as np

# 1. Membuat numpy array dasar
umur = np.array([22, 25, 24, 28, 23])
print("Data Umur (Array):", umur)
print("Rata-rata Umur   :", np.mean(umur))

# 2. Membuat Dummy Data (Data Simulasi)
# Membuat 5 data gaji acak antara 4.000.000 sampai 10.000.000
gaji_dummy = np.random.randint(low=4000000, high=10000000, size=5)
print("\nSimulasi Gaji Karyawan Baru:")
print(gaji_dummy)

# Numpy Menggunakan 'np.nan' (Not a Number) untuk mempersentasikan data kosong
data_kosong = np.array([10, 20, np.nan, 40])
print("\nContoh array dengan data kosong (NaN):", data_kosong)