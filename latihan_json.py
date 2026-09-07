import json

profil_user = {
    "id": 101,
    "nama": "Juan",
    "hobi": ["Ngoprek", "Olahraga"],
    "aktif": True
}

with open("profil.json", mode="w") as file:
    json.dump(profil_user, file, indent=4)

print("File JSON berhasil dibuat!")