import pandas as pd
from sqlalchemy import create_engine

# 1. Membuat Koneksi (Engine) menggunakan SQLAlchemy
# Format: 'jenis_db://nama_file.db'
engine = create_engine('sqlite:///kantor.db')

# 2. Menyiapkan Data Dummy
data_dept = pd.DataFrame({
'ID_Dept': ['D01', 'D02', 'D03', 'D04'],
'Nama_Dept': ['IT', 'HR', 'Finance', 'Marketing']
})

data_karyawan = pd.DataFrame({
'ID_Emp': [1, 2, 3, 4, 5],
'Nama': ['Andi', 'Budi', 'Citra', 'Diana', 'Eka'],
'Gaji': [700, 450, 800, 500, 900],
'ID_Dept': ['D01', 'D02', 'D01', None, 'D03']
})
# Perhatikan: Diana tidak punya Departemen (None), dan Marketing tidak punya karyawan

# 3. Export DataFrame Pandas langsung ke Database SQL (Otomatis membuat tabel)
data_dept.to_sql('Departemen', engine, if_exists='replace', index=False)
data_karyawan.to_sql('Karyawan', engine, if_exists='replace', index=False)

print("Database 'kantor.db' dan tabel relasional berhasil disiapkan dengan SQLAlchemy!")

print("--- 1. INNER JOIN (Hanya data yang saling beririsan) ---")# Menampilkan karyawan yang PASTI memiliki departemenquery_inner = """SELECT Karyawan.Nama, Karyawan.Gaji, Departemen.Nama_DeptFROM KaryawanINNER JOIN Departemen ON Karyawan.ID_Dept = Departemen.ID_Dept"""hasil_inner = pd.read_sql(query_inner, engine)print(hasil_inner)print("\n")print("--- 2. LEFT JOIN (Semua Karyawan masuk, meski tak punya departemen) ---")# Diana akan masuk di sini, dengan nama departemen bernilai NaN (Kosong)query_left = """SELECT Karyawan.Nama, Karyawan.Gaji, Departemen.Nama_DeptFROM KaryawanLEFT JOIN Departemen ON Karyawan.ID_Dept = Departemen.ID_Dept"""hasil_left = pd.read_sql(query_left, engine)print(hasil_left)print("\n")print("--- 3. RIGHT JOIN LOGIC (Semua Departemen masuk, meski tak ada karyawan) ---")# Catatan: SQLite tidak memiliki perintah RIGHT JOIN asli.# Triknya: Kita balik posisinya menjadi Departemen LEFT JOIN Karyawanquery_right = """SELECT Departemen.Nama_Dept, Karyawan.NamaFROM DepartemenLEFT JOIN Karyawan ON Departemen.ID_Dept = Karyawan.ID_Dept"""hasil_right = pd.read_sql(query_right, engine)print(hasil_right)

print("--- Subquery: Karyawan Bergaji di Atas Rata-rata ---")
query_sub = """
SELECT Nama, Gaji
FROM Karyawan
WHERE Gaji > (
SELECT AVG(Gaji) FROM Karyawan
)
"""
hasil_sub = pd.read_sql(query_sub, engine)
print(hasil_sub)

print("--- Window Function: Peringkat Gaji Tertinggi per Departemen ---")
# PARTITION BY: me-reset ranking setiap kali departemen berganti
# ORDER BY Gaji DESC: mengurutkan ranking berdasarkan gaji terbesar
query_window = """
SELECT
Nama,
ID_Dept,
Gaji,
RANK() OVER (
PARTITION BY ID_Dept
ORDER BY Gaji DESC
) AS Peringkat_Gaji
FROM Karyawan
WHERE ID_Dept IS NOT NULL
"""
hasil_window = pd.read_sql(query_window, engine)
print(hasil_window)