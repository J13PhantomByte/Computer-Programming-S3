
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Data Eksperimen Iklan Instagram
jumlah_pembeli = np.array([450, 380])  # [Pembeli Video, Pembeli Gambar]
jumlah_pengunjung = np.array([5000, 5000])

# 1. Menghitung Probabilitas Pembelian (Conversion Rate)
conversion_rate_video = (450 / 5000) * 100
conversion_rate_gambar = (380 / 5000) * 100

print(f"Conversion Rate Iklan Video: {conversion_rate_video:.2f}%")
print(f"Conversion Rate Iklan Gambar: {conversion_rate_gambar:.2f}%")

# 2. Melakukan A/B Testing (Z-Test)
z_stat, p_value = proportions_ztest(
    jumlah_pembeli,
    jumlah_pengunjung
)

print(f"\nNilai Z-Statistic: {z_stat:.2f}")
print(f"Nilai p-value: {p_value:.5f}")

# 3. Kesimpulan Bisnis
if p_value < 0.05:
    print("Kesimpulan: Fokuskan anggaran pada Iklan Video!")
else:
    print("Kesimpulan: Performa kedua iklan sama saja.")
