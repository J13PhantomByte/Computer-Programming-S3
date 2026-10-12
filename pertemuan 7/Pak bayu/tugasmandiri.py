
import pandas as pd
from sqlalchemy import create_engine

engine_toko = create_engine('sqlite:///ecommerce.db')

df_pelanggan = pd.DataFrame({
    'ID_Pel': ['P1', 'P2', 'P3', 'P4'],
    'Nama_Pel': ['Fahmi', 'Gina', 'Hadi', 'Intan']
})

df_pesanan = pd.DataFrame({
    'ID_Order': [101, 102, 103, 104, 105],
    'ID_Pel': ['P1', 'P1', 'P3', 'P99', 'P2'],
    'Total_Belanja': [250000, 150000, 400000, 50000, 800000]
})

df_pelanggan.to_sql(
    'Pelanggan', engine_toko,
    if_exists='replace', index=False
)

df_pesanan.to_sql(
    'Pesanan', engine_toko,
    if_exists='replace', index=False
)

print("Database ecommerce.db berhasil dibuat!")
print("\n")


print("--- 1. LEFT JOIN: Pelanggan dan Total Belanja ---")

query_join = """
SELECT
    Pelanggan.Nama_Pel,
    Pesanan.Total_Belanja
FROM Pelanggan
LEFT JOIN Pesanan
    ON Pelanggan.ID_Pel = Pesanan.ID_Pel
"""

hasil_join = pd.read_sql(query_join, engine_toko)
print(hasil_join)
print("\n")


print("--- 2. SUBQUERY: Pesanan di Atas Rata-rata ---")

query_subquery = """
SELECT
    ID_Order,
    Total_Belanja
FROM Pesanan
WHERE Total_Belanja > (
    SELECT AVG(Total_Belanja)
    FROM Pesanan
)
"""

hasil_subquery = pd.read_sql(query_subquery, engine_toko)
print(hasil_subquery)
print("\n")


print("--- 3. WINDOW FUNCTION: Peringkat Pesanan ---")

query_window = """
SELECT
    ID_Order,
    Total_Belanja,
    RANK() OVER (
        ORDER BY Total_Belanja DESC
    ) AS Peringkat
FROM Pesanan
"""

hasil_window = pd.read_sql(query_window, engine_toko)
print(hasil_window)

engine_toko.dispose()
