# Algoritma Genetika — Proses Mutasi
# Mutasi melakukan perubahan kecil pada kromosom untuk mempertahankan
# keragaman genetik dalam populasi dan mencegah konvergensi prematur.
# Tiga metode mutasi yang diimplementasikan:
# - Swap Mutation      : menukar posisi dua gen dalam kromosom
# - Inversion Mutation : membalik urutan gen dalam segmen tertentu
# - Uniform Mutation   : mengubah nilai gen dengan probabilitas tertentu

# 1. Import Library
import random

# 2. Swap Mutation
# Memilih dua posisi gen secara acak, lalu menukar nilainya
def swap_mutation(kromosom):
    kromosom = list(kromosom)  # Konversi ke list jika perlu
    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)
    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
    return kromosom

# 3. Inversion Mutation
# Memilih dua titik secara acak, lalu membalik urutan gen dalam segmen tersebut
def inversion_mutation(kromosom):
    kromosom = list(kromosom)  # Konversi ke list jika perlu
    posisi1  = random.randint(0, len(kromosom) - 2)
    posisi2  = random.randint(posisi1 + 1, len(kromosom) - 1)
    kromosom[posisi1:posisi2] = list(reversed(kromosom[posisi1:posisi2]))
    return kromosom

# 4. Uniform Mutation
# Untuk setiap gen, dengan probabilitas mutation_rate, balik nilai gen tersebut
# (dari 0 menjadi 1 atau sebaliknya)
def uniform_mutation(kromosom, mutation_rate=0.1):
    kromosom = list(kromosom)  # Konversi ke list jika perlu
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]  # Membalik nilai gen
    return kromosom

# 5. Contoh penggunaan
anak1 = [0, 1, 1, 0, 1]  # Contoh kromosom

mutasi_anak1 = swap_mutation(anak1.copy())       # Swap Mutation
mutasi_anak2 = inversion_mutation(anak1.copy())  # Inversion Mutation
mutasi_anak3 = uniform_mutation(anak1.copy())    # Uniform Mutation

print("\nAnak Setelah Mutasi:")
print(f"Anak 1 (Swap Mutation)      : {mutasi_anak1}")
print(f"Anak 2 (Inversion Mutation) : {mutasi_anak2}")
print(f"Anak 3 (Uniform Mutation)   : {mutasi_anak3}")
