# Algoritma Genetika — Proses Crossover
# Crossover (rekombinasi/kawin silang) menggabungkan dua kromosom parent
# untuk menghasilkan dua kromosom anak (offspring) yang baru.
# Tiga metode crossover yang diimplementasikan:
# - One-Point Crossover : memotong di satu titik, menukar bagian setelah titik
# - Two-Point Crossover : memotong di dua titik, menukar segmen di antaranya
# - Uniform Crossover   : setiap gen dipilih dari salah satu parent berdasarkan mask

# 1. Import Library
import random

# 2. One-Point Crossover
# Memilih satu titik potong secara acak, lalu menukar bagian setelah titik tersebut
def one_point_crossover(parent1, parent2):
    titik_potong = random.randint(1, len(parent1) - 1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2

# 3. Two-Point Crossover
# Memilih dua titik potong secara acak, lalu menukar segmen di antara kedua titik
def two_point_crossover(parent1, parent2):
    titik1 = random.randint(1, len(parent1) - 2)
    titik2 = random.randint(titik1 + 1, len(parent1) - 1)
    anak1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    anak2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]
    return anak1, anak2

# 4. Uniform Crossover
# Membuat mask acak — gen mask 1 → tukar, gen mask 0 → tidak ditukar
# Jika mask[i] = 0: anak1 ambil dari parent1, anak2 ambil dari parent2
# Jika mask[i] = 1: anak1 ambil dari parent2, anak2 ambil dari parent1
def uniform_crossover(parent1, parent2):
    mask  = [random.randint(0, 1) for _ in range(len(parent1))]
    anak1 = []
    anak2 = []
    for i in range(len(parent1)):
        if mask[i] == 0:
            anak1.append(parent1[i])
            anak2.append(parent2[i])
        else:
            anak1.append(parent2[i])
            anak2.append(parent1[i])
    return anak1, anak2

# 5. Contoh penggunaan
parent1 = [1, 0, 1, 1, 0]  # Contoh parent1
parent2 = [0, 1, 0, 0, 1]  # Contoh parent2

anak1, anak2 = one_point_crossover(parent1, parent2)

print("\nAnak Hasil Crossover:")
print(f"Anak 1: {anak1}")
print(f"Anak 2: {anak2}")
