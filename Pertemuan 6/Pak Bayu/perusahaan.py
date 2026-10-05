import sqlite3
import pandas as pd

# 1. Membuat & Membuka koneksi ke file database SQLite
# Jika file belum ada, Python akan otomatis membuatnya di folder yang sama
conn = sqlite3.connect("perusahaan.db")
kursor = conn.cursor()

# 2. Membuat tabel Karyawan (Konsep Database Relasional)
kursor.execute('''
CREATE TABLE IF NOT EXISTS Karyawan (
ID INTEGER PRIMARY KEY,
Nama TEXT,
Departemen TEXT,
Gaji INTEGER
)
''')

# 3. Membersihkan data lama (jika di-run berulang) agar tidak ganda
kursor.execute('DELETE FROM Karyawan')

# 4. Memasukkan (Insert) data dummy
data_karyawan = [
(101, 'Andi', 'IT', 6000000),
(102, 'Budi', 'HR', 4500000),
(103, 'Citra', 'IT', 7500000),
(104, 'Diana', 'Finance', 8000000),
(105, 'Eka', 'IT', 5500000),
(106, 'Fajar', 'HR', 5000000)
]

kursor.executemany('INSERT INTO Karyawan VALUES (?, ?, ?, ?)', data_karyawan)
conn.commit() # Simpan permanen ke database

print("Database 'perusahaan.db' dan tabel Karyawan berhasil dibuat!")

# Pastikan koneksi conn (dari Praktik 1) masih terbuka!
print("--- 1. SELECT & LIMIT (Menampilkan 3 Data Teratas) ---")
query_1 = "SELECT * FROM Karyawan LIMIT 3"
hasil_1 = pd.read_sql_query(query_1, conn)
print(hasil_1)
print("\n")

print("--- 2. SELECT Kolom Tertentu ---")
# Hanya mengambil kolom Nama dan Departemen
query_2 = "SELECT Nama, Departemen FROM Karyawan"
hasil_2 = pd.read_sql_query(query_2, conn)
print(hasil_2)
print("\n")

print("--- 3. WHERE & ORDER BY (Filter & Urutkan) ---")
# Cari anak IT yang gajinya di atas 5.5 juta, urutkan dari gaji tertinggi (DESC)
query_3 = '''
SELECT Nama, Departemen, Gaji
FROM Karyawan
WHERE Departemen = 'IT' AND Gaji > 5500000
ORDER BY Gaji DESC
'''
...
hasil_3 = pd.read_sql_query(query_3, conn)
print(hasil_3)

print("--- 4. GROUP BY (Rata-rata Gaji per Departemen) ---")
# Menghitung total orang (COUNT) dan rata-rata (AVG) per kelompok departemen
query_4 = """
SELECT
Departemen,
COUNT(ID) AS Jumlah_Orang,
AVG(Gaji) AS Rata_Gaji
FROM Karyawan
GROUP BY Departemen
"""
...
hasil_4 = pd.read_sql_query(query_4, conn)
print(hasil_4)
print("\n")

print("--- 5. HAVING (Filter Hasil Agregasi) ---")
# Cari departemen mana saja yang Rata-rata Gajinya di atas 5 juta rupiah
# INGAT: Untuk filter hasil hitungan matematika (AVG/COUNT), kita WAJIB pakai HAVING
query_5 = """
SELECT
Departemen,
AVG(Gaji) AS Rata_Gaji
FROM Karyawan
GROUP BY Departemen
HAVING Rata_Gaji > 5000000
"""
...
hasil_5 = pd.read_sql_query(query_5, conn)
print(hasil_5)

# Tahap Akhir: Selalu tutup koneksi database jika sudah selesai!
conn.close()
print("\nKoneksi database ditutup.")