import pandas as pd
import matplotlib.pyplot as plt

# 1. Membuat data mentah
data = {'Departemen': ['IT', 'HR', 'Finance', 'Marketing', 'IT', 'IT', 'Finance']}
df = pd.DataFrame(data)

# 2. Menghitung jumlah data per kategori (Value Counts)
jumlah_per_dept = df['Departemen'].value_counts()
print("--- Data Numerik Sebelum Divvisualisasikan ---")
print(jumlah_per_dept)

# 3. Membuat Bar Chart
plt.figure(figsize=(8, 5))
jumlah_per_dept.plot(kind='bar', color=['blue', 'green', 'orange', 'red'])

# 4. Menambahkan judul dan label
plt.title("Sebaran Jumlah Karyawan per Departemen", fontsize=14)
plt.xlabel("Departemen")
plt.ylabel("Jumlah Karyawan")
plt.xticks(rotation=0) # Agar teks di sumbu X tidak miring

# 5. Menampilkan grafik ke layar
plt.show()