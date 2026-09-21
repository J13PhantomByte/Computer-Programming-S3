import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset Pengunjung Mall
data_pengunjung = {
    "Umur": [18, 22, 25, 22, 24, 19, 21, 23, 22, 65, 28, 22, 19, 24, 70, 21]
}
df_mall = pd.DataFrame(data_pengunjung)

# =====================================================================
# 1. Analisis Teks (Skor 30)
# =====================================================================
print("--- Hasil Analisis Teks (.describe()) ---")
print(df_mall.describe())
print("\n" + "="*50 + "\n")

# =====================================================================
# 2. Visualisasi Histogram (Skor 35)
# =====================================================================
plt.figure(figsize=(8, 5))
plt.hist(df_mall['Umur'], bins=5, edgecolor='black', color='skyblue')
plt.title("Distribusi Umur Pengunjung")
plt.xlabel("Umur")
plt.ylabel("Jumlah Pengunjung")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# =====================================================================
# 3. Visualisasi Boxplot (Skor 35)
# =====================================================================
plt.figure(figsize=(8, 4))
sns.boxplot(x=df_mall['Umur'], color='lightgreen')
plt.title("Boxplot Umur Pengunjung (Deteksi Outlier)")
plt.xlabel("Umur")
plt.show()
