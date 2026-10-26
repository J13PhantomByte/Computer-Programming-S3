import pandas as pd
import numpy as np
from scipy import stats

# Data penjualan harian selama 1 minggu
penjualan_A = [20, 22, 19, 24, 21, 23, 20]
penjualan_B = [15, 14, 16, 15, 17, 14, 16]

print(f"Rata-rata Cabang A: {np.mean(penjualan_A):.2f}")
print(f"Rata-rata Cabang B: {np.mean(penjualan_B):.2f}")

# Melakukan T-Test (Independent 2-sample)
t_stat, p_value = stats.ttest_ind(penjualan_A, penjualan_B)

print(f"\nNilai T-Statistic: {t_stat:.2f}")
print(f"Nilai p-value : {p_value:.5f}")

if p_value < 0.05:
    print("Kesimpulan: Terdapat perbedaan penjualan yang SIGNIFIKAN antara Cabang A dan B.")
else:
    print("Kesimpulan: TIDAK ADA perbedaan yang signifikan (hanya kebetulan).")