
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur tampilan grafik agar lebih rapi
sns.set_theme(style="whitegrid")

nama_file_awal = "online_retail_150.csv"

# Mengecek apakah file dataset sudah ada di komputer. Jika belum, unduh otomatis.
if not os.path.exists(nama_file_awal):
    print("Mengunduh dataset dari HuggingFace... Mohon tunggu sebentar.")
    df_full = pd.read_csv(
        "hf://datasets/jason1966/abhishekrp1517_online-retail-transactions-dataset/Online Retail.csv"
    )

    df_sample = df_full.sample(n=150, random_state=42)
    df_sample.to_csv(nama_file_awal, index=False)
    print(f"Dataset '{nama_file_awal}' berhasil dibuat!\n")
else:
    print(f"Dataset '{nama_file_awal}' sudah tersedia di folder.\n")



print("=" * 60)
print("TUGAS 1: MEMBACA DAN MEMAHAMI DATA")
print("=" * 60)

# 1a. Membaca dataset menggunakan Pandas
df = pd.read_csv(nama_file_awal)

print("\n[1a] 5 Baris Pertama Dataset:")
print(df.head())

print("\n[1a] Jumlah Baris dan Kolom:")
print(f"Jumlah Baris : {df.shape[0]} baris")
print(f"Jumlah Kolom : {df.shape[1]} kolom")

print("\n[1a] Tipe Data Setiap Kolom:")
print(df.dtypes)

# 1b. Identifikasi missing values (nilai kosong) dan data duplikat
print("\n[1b] Jumlah Missing Values per Kolom:")
print(df.isnull().sum())

jumlah_duplikat = df.duplicated().sum()
print(f"\n[1b] Jumlah Data Duplikat: {jumlah_duplikat} baris")


print("\n" + "=" * 60)
print("TUGAS 2: PREPROCESSING DATA")
print("=" * 60)

# 2a. Menangani missing values pada kolom Description dan CustomerID
# - Untuk Description: diisi dengan teks 'UNKNOWN PRODUCT' apabila ada yang kosong
# - Untuk CustomerID: diisi dengan 'GUEST' (atau 0) karena pelanggan tidak login/terdaftar,
#   agar data transaksi barang dan harganya tidak ikut terbuang.
df['Description'] = df['Description'].fillna('UNKNOWN PRODUCT')
df['CustomerID'] = df['CustomerID'].fillna('GUEST')

# Menghapus data duplikat jika ditemukan
if jumlah_duplikat > 0:
    df = df.drop_duplicates()

print("\n[2a] Cek Missing Values Setelah Ditangani:")
print(df[['Description', 'CustomerID']].isnull().sum())

# 2b. Pembersihan teks pada kolom Description
# Menghapus spasi berlebih di awal & akhir kalimat (.str.strip()),
# lalu mengubah semua teks menjadi huruf kapital (.str.upper())
df['Description'] = df['Description'].astype(str).str.strip().str.upper()

print("\n[2b] Contoh 5 Data Kolom Description Setelah Dibersihkan:")
print(df['Description'].head())

# 2c. Menyimpan DataFrame yang sudah bersih ke file CSV baru tanpa index
nama_file_bersih = "retail_bersih.csv"
df.to_csv(nama_file_bersih, index=False)
print(f"\n[2c] Data bersih berhasil disimpan ke file: '{nama_file_bersih}'")

# [Tambahan Ketentuan Pengumpulan]: Menyimpan ke database SQLite (retail.db)
nama_file_db = "retail.db"
conn = sqlite3.connect(nama_file_db)
df.to_sql("transaksi_retail", conn, if_exists="replace", index=False)
conn.close()
print(f"[Info] Data bersih juga berhasil disimpan ke database: '{nama_file_db}'")


print("\n" + "=" * 60)
print("TUGAS 3: VISUALISASI DAN EDA")
print("=" * 60)

# 3a. Bar chart 5 produk dengan jumlah unit terjual (Quantity) tertinggi
top_5_produk = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n[3a] 5 Produk dengan Jumlah Unit Terjual Tertinggi:")
print(top_5_produk)

plt.figure(figsize=(10, 5))
sns.barplot(
    x=top_5_produk.values,
    y=top_5_produk.index,
    hue=top_5_produk.index,
    palette="viridis",
    legend=False
)
plt.title("5 Produk dengan Jumlah Unit Terjual Tertinggi", fontsize=14, fontweight='bold')
plt.xlabel("Total Jumlah Unit Terjual (Quantity)")
plt.ylabel("Nama Produk (Description)")
plt.tight_layout()
plt.savefig("3a_top_5_produk.png")
plt.show()

# 3b. Histogram untuk melihat distribusi UnitPrice
plt.figure(figsize=(8, 5))
sns.histplot(df['UnitPrice'], bins=30, kde=True, color='royalblue')
plt.title("Distribusi Harga Satuan Produk (UnitPrice)", fontsize=14, fontweight='bold')
plt.xlabel("Harga Satuan (UnitPrice)")
plt.ylabel("Frekuensi Transaksi")
plt.tight_layout()
plt.savefig("3b_distribusi_unitprice.png")
plt.show()

# 3c. Menghitung total penjualan setiap negara menggunakan groupby()
# Membuat kolom TotalPenjualan (Quantity dikali UnitPrice)
df['TotalPenjualan'] = df['Quantity'] * df['UnitPrice']

# Mengelompokkan berdasarkan Country dan menjumlahkan TotalPenjualan
top_5_negara = (
    df.groupby('Country')['TotalPenjualan']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n[3c] 5 Negara dengan Total Penjualan Tertinggi:")
print(top_5_negara)

# 3d. Kesimpulan berdasarkan hasil analisis
kesimpulan = """
[3d] KESIMPULAN ANALISIS DATA:
1. Pola Penjualan Negara: Berdasarkan hasil pengelompokan (groupby), transaksi dan nilai
   penjualan tertinggi didominasi secara signifikan oleh negara United Kingdom (Inggris)
   dibandingkan negara-negara lainnya, karena perusahaan retail ini berbasis di Inggris.
2. Harga & Jumlah Pembelian: Dari grafik distribusi (Histogram), mayoritas produk yang
   terjual memiliki harga satuan (UnitPrice) yang relatif murah/terjangkau. Namun,
   terdapat beberapa produk yang dibeli dalam jumlah sangat banyak sekaligus (grosir).
3. Deteksi Outlier: Berdasarkan visualisasi Boxplot pada kolom Quantity dan UnitPrice,
   terbukti terdapat nilai ekstrem (outlier) yang berada jauh di luar batas normal,
   baik berupa pembelian dalam partai besar maupun transaksi bernilai minus (retur/pembatalan).
"""
print(kesimpulan)

# 3e. Visualisasi Boxplot menggunakan Seaborn pada kolom Quantity dan UnitPrice
plt.figure(figsize=(12, 5))

# Boxplot untuk Quantity
plt.subplot(1, 2, 1)
sns.boxplot(x=df['Quantity'], color='salmon')
plt.title("Boxplot Quantity (Deteksi Outlier Jumlah)", fontsize=12, fontweight='bold')
plt.xlabel("Jumlah Barang (Quantity)")

# Boxplot untuk UnitPrice
plt.subplot(1, 2, 2)
sns.boxplot(x=df['UnitPrice'], color='lightgreen')
plt.title("Boxplot UnitPrice (Deteksi Outlier Harga)", fontsize=12, fontweight='bold')
plt.xlabel("Harga Satuan (UnitPrice)")

plt.tight_layout()
plt.savefig("3e_boxplot_outlier.png")
plt.show()

print("\n" + "=" * 60)
print("SELESAI! Semua tugas telah berhasil dijalankan.")
print("=" * 60)
