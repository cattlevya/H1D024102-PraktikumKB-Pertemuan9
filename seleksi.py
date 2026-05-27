# Algoritma Genetika — Proses Seleksi
# Seleksi memilih individu-individu terbaik sebagai orang tua (parent)
# untuk menghasilkan generasi berikutnya melalui crossover dan mutasi.
# Dua metode seleksi yang diimplementasikan:
# - Roulette Wheel Selection: probabilistik berdasarkan proporsi fitness
# - Tournament Selection: memilih pemenang dari sejumlah peserta acak

# 1. Import Library
import random

# 2. Fungsi untuk Roulette Wheel Selection
# Individu dengan fitness lebih tinggi memiliki peluang lebih besar untuk dipilih
def roulette_wheel_selection(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)

    # Jika semua fitness = 0, pilih individu secara acak
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx

    # Hitung probabilitas seleksi setiap individu
    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]

    # Hitung probabilitas kumulatif
    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    # Bangkitkan bilangan acak dan tentukan individu yang terpilih
    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i

    # Fallback: kembalikan individu terakhir jika tidak ada yang memenuhi
    return populasi[-1], len(populasi) - 1

# 3. Fungsi untuk Tournament Selection
# Memilih k individu secara acak, lalu pilih yang memiliki fitness tertinggi
def tournament_selection(populasi, fitness_populasi, k=3):
    # Pastikan k tidak melebihi ukuran populasi
    if len(populasi) < k:
        k = len(populasi)

    # Pilih k peserta secara acak
    peserta_indices = random.sample(range(len(populasi)), k)
    peserta = [(populasi[i], fitness_populasi[i], i) for i in peserta_indices]

    # Urutkan berdasarkan fitness secara menurun, pilih yang tertinggi
    peserta.sort(key=lambda x: x[1], reverse=True)
    return peserta[0][0], peserta[0][2]

# 4. Contoh penggunaan
# Definisikan populasi awal dan fitness_populasi
populasi_awal    = ['individu1', 'individu2', 'individu3', 'individu4']
fitness_populasi = [10, 20, 30, 40]

# Membuat salinan populasi dan fitness untuk dimodifikasi
available_populasi = populasi_awal.copy()
available_fitness  = fitness_populasi.copy()

# Memilih Parent 1 menggunakan Roulette Wheel Selection
parent1, idx1 = roulette_wheel_selection(available_populasi, available_fitness)

# Hapus parent1 dari daftar agar parent2 berbeda
del available_populasi[idx1]
del available_fitness[idx1]

# Memilih Parent 2 menggunakan Tournament Selection
parent2, idx2 = tournament_selection(available_populasi, available_fitness)

# Hapus parent2 dari daftar
del available_populasi[idx2]
del available_fitness[idx2]

print("\nParent Terpilih:")
print(f"Parent 1: {parent1}")
print(f"Parent 2: {parent2}")
