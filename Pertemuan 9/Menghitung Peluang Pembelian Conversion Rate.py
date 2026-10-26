import pandas as pd
import numpy as np

# Data Pengunjung Website (Beli = 1, Tidak Beli = 0)
data_pengunjung = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'Status_Beli': ['Ya', 'Tidak', 'Tidak', 'Ya',
                                    'Ya', 'Tidak', 'Tidak', 'Tidak' 'Ya', 'Tidak']}
df_web = pd.DataFrame(data_pengunjung)

# Menghitung probabilitas
total_pengunjung = len(df_web)
total_pembeli = len(df_web[df_web['Status_Beli'] == 'Ya'])

probabilitas = (total_pembeli / total_pengunjung) * 100

print(f"Total Pengunjung: {total_pengunjung} orang")
print(f"Total Pembeli : {total_pembeli} orang")
print(f"Probabilitas Pembelian (Conversion Rate): {probabilitas}%")