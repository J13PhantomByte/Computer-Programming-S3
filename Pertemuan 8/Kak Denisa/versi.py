# 1. FAKTA AWAL

facts = {"membawa_payung"}

#Rules
rules = [
({"hujan"}, "membawa_payung"),
({"membawa_payung"}, "siap_bepergian"),
({"cuaca_cerah"}, "beraktivitas_di_luar")
]

# 3. FUNGSI FORWARD CHAINING
# Fakta -> Aturan -> Kesimpulan


def forward_chaining(initial_facts, rules):
   known_facts = set(initial_facts)


   print("\n================================")
   print("       FORWARD CHAINING")
   print("================================")


   print("\nFakta awal:")
   for fact in sorted(known_facts):
       print(f"- {fact}")


   step = 1


   while True:
       new_fact_found = False


       for conditions, conclusion in rules:


           # Periksa apakah semua kondisi terpenuhi
           if conditions.issubset(known_facts):


               # Kesimpulan belum diketahui
               if conclusion not in known_facts:
                   print(f"\nLangkah {step}:")
                   print(f"Kondisi terpenuhi: {conditions}")
                   print(f"Aturan aktif: IF {conditions} THEN {conclusion}")
                   print(f"Kesimpulan baru: {conclusion}")


                   known_facts.add(conclusion)
                   new_fact_found = True
                   step += 1


       # Berhenti jika tidak ada fakta baru
       if not new_fact_found:
           break


   print("\nFakta yang diketahui setelah proses:")
   for fact in sorted(known_facts):
       print(f"- {fact}")


   return known_facts


# 4. FUNGSI BACKWARD CHAINING
# Tujuan -> Aturan -> Fakta


def backward_chaining(goal, initial_facts, rules, depth=0):
    indent = "  " * depth

    print(f"{indent}Memeriksa tujuan: {goal}")

    # Basis: tujuan sudah menjadi fakta awal
    if goal in initial_facts:
        print(f"{indent}[BERHASIL] {goal} adalah fakta awal.")
        return True

    # Cari aturan yang menghasilkan tujuan
    for conditions, conclusion in rules:

        if conclusion == goal:
            print(
                f"{indent}Menemukan aturan: "
                f"IF {conditions} THEN {conclusion}"
            )

            # Semua kondisi harus dapat dibuktikan
            all_conditions_proven = True

            for condition in sorted(conditions):
                result = backward_chaining(
                    condition,
                    initial_facts,
                    rules,
                    depth + 1
                )

                if not result:
                    all_conditions_proven = False
                    break

            if all_conditions_proven:
                print(
                    f"{indent}[BERHASIL] "
                    f"Tujuan {goal} dapat dibuktikan."
                )
                return True

    # Tidak ada aturan yang dapat membuktikan tujuan
    print(f"{indent}[GAGAL] Tujuan {goal} tidak dapat dibuktikan.")
    return False



# 5. PROGRAM UTAMA

def main():
    print("========================================")
    print(" RULE-BASED SYSTEM")
    print(" Forward & Backward Chaining")
    print("========================================")

    # A. Jalankan Forward Chaining
    final_facts = forward_chaining(facts, rules)

    # B. Jalankan Backward Chaining
    goal = "beraktivitas_di_luar"

    print("\n================================")
    print("       BACKWARD CHAINING")
    print("================================")

    print(f"\nTujuan yang ingin dibuktikan: {goal}")

    result = backward_chaining(goal, facts, rules)

    print("\nHasil Backward Chaining:")
    if result:
        print(f"TUJUAN TERCAPAI: {goal}")
    else:
        print(f"TUJUAN TIDAK TERCAPAI: {goal}")

    # C. Uji tujuan yang tidak dapat dibuktikan
    second_goal = "beraktivitas_di_luar"

    print("\n================================")
    print("       PENGUJIAN KEDUA")
    print("================================")

    print(f"\nTujuan yang ingin dibuktikan: {second_goal}")

    second_result = backward_chaining(
        second_goal,
        facts,
        rules
    )

    print("\nHasil Pengujian Kedua:")
    if second_result:
        print(f"TUJUAN TERCAPAI: {second_goal}")
    else:
        print(f"TUJUAN TIDAK TERCAPAI: {second_goal}")

    # D. Perbandingan hasil
    print("\n================================")
    print("       KESIMPULAN")
    print("================================")

    print("Forward Chaining:")
    print("Sistem memulai dari fakta awal dan mencari kesimpulan.")

    print("\nBackward Chaining:")
    print("Sistem memulai dari tujuan dan mencari fakta pendukung.")

    print("\nFakta hasil Forward Chaining:")
    for fact in sorted(final_facts):
        print(f"- {fact}")


# Jalankan program
if __name__ == "__main__":
    main()