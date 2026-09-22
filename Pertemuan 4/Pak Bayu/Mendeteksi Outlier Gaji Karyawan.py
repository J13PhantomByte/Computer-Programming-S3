import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Gaji dalam jutaan (Perhatikan angka 25 yang tidak wajar)
data_gaji = [4.5, 5.0, 4.8, 5.2, 4.9, 5.5, 4.7, 25.0, 5.1, 4.6]
df_gaji = pd.DataFrame({'Gaji_Juta': data_gaji})

# Membuat Boxplot dengan Seaborn
plt.figure(figsize=(8, 3))
sns.boxplot(x=df_gaji['Gaji_Juta'], color='lightgreen')

plt.title("Deteksi Outlier pada Data Gaji Karyawan")
plt.xlabel("Gaji (dalam Juta Rupiah)")

plt.show()
