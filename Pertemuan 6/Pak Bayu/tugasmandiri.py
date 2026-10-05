import sqlite3
import pandas as pd

conn_toko = sqlite3.connect("toko.db")
kursor = conn_toko.cursor()

kursor.execute('''
CREATE TABLE IF NOT EXISTS Penjualan(
    ID_Trx INTEGER PRIMARY KEY, 
    Produk TEXT, 
    Kategori TEXT, 
    Harga INTEGER,
    Terjual INTEGER
)
''')

kursor.execute('DELETE FROM Penjualan') # Bersihkan data lama

data_trx = [
    (1, 'Laptop', 'Elektronik', 7500000, 2),
    (2, 'Meja', 'Furniture', 1200000, 5), 
    (3, 'Mouse', 'Elektronik', 150000, 10), 
    (4, 'Kursi', 'Furniture', 800000, 8),
    (5, 'Monitor', 'Elektronik', 2000000, 3) 
]

kursor.executemany('INSERT INTO Penjualan VALUES(?,?,?,?,?)', data_trx)
conn_toko.commit()
print("Database 'toko.db' dan tabel Penjualan berhasil di-setup!\n")

print("--- Soal 1: Filter Elektronik & Order By ---")
query_1 = """
SELECT * 
FROM Penjualan 
WHERE Kategori = 'Elektronik' 
ORDER BY Terjual DESC
"""
hasil_1 = pd.read_sql_query(query_1, conn_toko)
print(hasil_1)
print("\n")

print("--- Soal 2: Total Terjual per Kategori (GROUP BY) ---")
query_2 = """
SELECT Kategori, SUM(Terjual) AS Total_Terjual
FROM Penjualan
GROUP BY Kategori
"""
hasil_2 = pd.read_sql_query(query_2, conn_toko)
print(hasil_2)
print("\n")

print("--- Soal 3: Filter Kategori dengan Total Terjual > 10 (HAVING) ---")
query_3 = """
SELECT Kategori, SUM(Terjual) AS Total_Terjual
FROM Penjualan
GROUP BY Kategori
HAVING Total_Terjual > 10
"""
hasil_3 = pd.read_sql_query(query_3, conn_toko)
print(hasil_3)

conn_toko.close()
print("\nKoneksi database toko ditutup.")