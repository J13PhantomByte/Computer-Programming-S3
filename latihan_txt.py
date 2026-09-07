# Mode "w" untuk membuat file baru dan mengisinya
# Mode "a" untuk menambahkan data ke file yang sudah ada
# Mode "r" untuk membaca file yang sudah ada

with open("laporan.txt", mode="w") as file:
    file.write("Ini adalah baris pertama.\n")
    file.write("Nasi goreng sangat enak. \n")

print("File teks berhasil dibuat!")