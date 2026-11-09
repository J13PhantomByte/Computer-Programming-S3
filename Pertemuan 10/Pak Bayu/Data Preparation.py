import pandas as pd
import numpy as np
import random
# 1. Men-generate 200 data transaksi buatan secara acak
np.random.seed(42)
tanggal = pd.date_range(start='2026-01-01', periods=200, freq='D')
kategori = ['Elektronik', 'Pakaian', 'Makanan', 'Kosmetik']
kota = ['Jakarta', 'Bandung', 'Surabaya', 'Medan']
data = {
'Tanggal_Trx': tanggal,
'Kategori_Produk': [random.choice(kategori) for _ in range(200)],
'Kota_Cabang': [random.choice(kota) for _ in range(200)],
'Jumlah_Beli': np.random.randint(1, 10, 200),
'Harga_Satuan': np.random.randint(50, 500, 200) * 1000
}
df_bi = pd.DataFrame(data)
# 2. Menambahkan Kolom Kalkulasi
df_bi['Total_Pendapatan'] = df_bi['Jumlah_Beli'] * df_bi['Harga_Satuan']
# 3. PENYESUAIAN FORMAT TANGGAL (Penting)
# Looker Studio sering error ('Invalid Dimension') membaca tanggal ber-strip.
# Kita ubah ke format rapat (YYYYMMDD) agar otomatis terbaca sebagai kalender.
df_bi['Tanggal_Trx'] = df_bi['Tanggal_Trx'].dt.strftime('%Y%m%d')
# 4. Ekspor ke CSV
df_bi.to_csv('data_penjualan_bi.csv', index=False)
print("File berhasil dibuat!")
