import json
import csv
import pandas as pd

# Dataset Mentah
data_produk = [
    {"id": "P01", "nama": "Laptop", "kategori": "Elektronik", "stok": 50},
    {"id": "P02", "nama": "Meja", "kategori": "Furniture", "stok": 5},
    {"id": "P03", "nama": "Mouse", "kategori": "Elektronik", "stok": 120},
    {"id": "P04", "nama": "Kursi", "kategori": "Furniture", "stok": 2}
]

# ---------------------------------------------------------
# 1. Buat File JSON (inventory.json)
# ---------------------------------------------------------
with open('inventory.json', 'w') as file_json:
    json.dump(data_produk, file_json, indent=4)

# ---------------------------------------------------------
# 2. Filter & Export ke CSV (stok_kritis.csv)
# ---------------------------------------------------------
# Baca kembali file inventory.json
with open('inventory.json', 'r') as file_json:
    loaded_data = json.load(file_json)

# Filter data dengan stok < 10 menggunakan perulangan (looping)
stok_kritis = []
for item in loaded_data:
    if item['stok'] < 10:
        stok_kritis.append({
            'Nama': item['nama'],
            'Kategori': item['kategori'],
            'Stok': item['stok']
        })

# Simpan ke file CSV lengkap dengan Header (Nama, Kategori, Stok)
with open('stok_kritis.csv', 'w', newline='', encoding='utf-8') as file_csv:
    fieldnames = ['Nama', 'Kategori', 'Stok']
    writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(stok_kritis)

# ---------------------------------------------------------
# 3. Verifikasi Pandas
# ---------------------------------------------------------
df = pd.read_csv('stok_kritis.csv')

print("=== Dimensi Data (.shape) ===")
print(df.shape)

print("\n=== Tipe Data & Informasi (.info()) ===")
df.info()