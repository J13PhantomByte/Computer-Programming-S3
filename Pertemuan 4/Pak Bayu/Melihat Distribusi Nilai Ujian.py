import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Membuat 100 data nilai ujian acak (berkisar antara 50 sampai 100)
np.random.seed(42)
nilai_ujian = np.random.randint(50, 100, size=100)
df_nilai = pd.DataFrame({'Nilai': nilai_ujian})

# Membuat Historigram
plt.figure(figsize=(8, 5))
plt.hist(df_nilai['Nilai'], bins=10, color='skyblue', edgecolor='black')

plt.title("Distribusi Sebaran Nilai Ujian Mahasiswa")
plt.xlabel("Rentang Nilai")
plt.ylabel("Frekuensi (Jumlah Mahasiswa)")

plt.show()