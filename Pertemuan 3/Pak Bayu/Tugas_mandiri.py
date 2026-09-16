import pandas as pd
import numpy as np

# Data toko
data_toko = {
    "ID_Trx": ["T01", "T02", "T01", "T03", "T04", "T05"],
    "Produk": [" Laptop", "mouse", " Laptop", "KEYBOARD", "monitor ", "mouse"],
    "Harga": [7500000, 150000, 7500000, np.nan, 2000000, np.nan],
    "Jumlah": [1, 5, 1, 2, np.nan, 3]
}

# 1. Ubah dictionary menjadi DataFrame
df_toko = pd.DataFrame(data_toko)

print("Data sebelum dibersihkan:")
print(df_toko)


# 2. Hapus baris yang duplikat
df_toko = df_toko.drop_duplicates()

# Hapus spasi berlebih pada kolom Produk
df_toko["Produk"] = df_toko["Produk"].str.strip()

# Ubah semua teks menjadi Title Case
df_toko["Produk"] = df_toko["Produk"].str.title()


# 3. Menangani Missing Values

# Isi nilai kosong pada kolom Jumlah dengan 1
df_toko["Jumlah"] = df_toko["Jumlah"].fillna(1)

# Isi nilai kosong pada kolom Harga dengan rata-rata harga
df_toko["Harga"] = df_toko["Harga"].fillna(df_toko["Harga"].mean())


# 4. Export DataFrame yang sudah bersih ke CSV
df_toko.to_csv("transaksi_bersih.csv", index=False)

print("\nData setelah dibersihkan:")
print(df_toko)

print("\nFile berhasil disimpan sebagai transaksi_bersih.csv")