# Algoritma Genetika — Evaluasi Fitness
# Evaluasi fitness menghitung seberapa baik setiap individu (kromosom)
# dalam menyelesaikan Knapsack Problem.
# Fitness = total harga barang yang dipilih, dengan syarat total bobot ≤ kapasitas tas.
# Jika total bobot melebihi kapasitas, fitness = 0 (penalti).

# 1. Data barang (nama, harga, bobot)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 70, 15)
]

kapasitas_tas = 50  # Kapasitas maksimum tas

# 2. Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            # Jika gen bernilai 1, barang ke-i dipilih
            total_harga += barang[i][1]
            total_bobot += barang[i][2]

    # Jika total bobot melebihi kapasitas, beri penalti (fitness = 0)
    if total_bobot > kapasitas_tas:
        return 0
    else:
        return total_harga

# 3. Definisi contoh populasi awal
populasi_awal = [
    [1, 0, 1, 0, 1],  # Contoh kromosom individu
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    # Tambahkan lebih banyak individu sesuai kebutuhan
]

# 4. Contoh penggunaan — hitung fitness untuk setiap individu
fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas)
                    for individu in populasi_awal]

# Menampilkan nilai fitness
print("\nNilai Fitness:")
for idx, fitness in enumerate(fitness_populasi):
    print(f"Individu {idx+1}: Fitness = {fitness}")
