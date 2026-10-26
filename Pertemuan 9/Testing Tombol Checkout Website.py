import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Data Hasil Eksperimen
jumlah_klik = np.array([150, 200]) # [Klik A, Klik B]
jumlah_pengunjung = np.array([1000, 1000]) # [Pengunjung A, Pengunjung B]

# Melakukan Z-Test
z_stat, p_value = proportions_ztest(jumlah_klik, jumlah_pengunjung)

print(f"Conversion Rate Desain A: {((150/1000)*100)}%")
print(f"Conversion Rate Desain B: {((200/1000)*100)}%")
print(f"\nNilai p-value A/B Test: {p_value:.5f}")

if p_value < 0.05:
    print("Kesimpulan: Desain B secara ilmiah LEBIH BAIK dari Desain A. Terapkan Desain B!")
else:
    print("Kesimpulan: Perbedaan tidak signifikan. Jangan buang biaya untuk mengubah desain.")