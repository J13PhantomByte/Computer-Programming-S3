import csv

# Ini adalah data mentah kita (List di dalam list)
data_nilai = [
    ["Nama", "Mata Kuliah", "Nilai"],   # Ini Header / Judul Kolom
    ["Ridho", "Python", 95],            # Ini baris data 1
    ["Gilang", "Cloud Computing", 95],  # Ini baris data 2
]

# newline="" mencegah terjadinya beris kosong (enter ganda) di sistem windows
with open("data_mahasiswa.csv", mode="w", newline="") as file:
    penulis = csv.writer(file)
    penulis.writerows(data_nilai)       

print("File CSV berhasil dibuat! Silahkan buat folder anda.")