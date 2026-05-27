# H1D024102-PraktikumKB-Pertemuan9

Pengumpulan tugas praktikum Kecerdasan Buatan pertemuan 9.

## Implementasi Algoritma Genetika untuk Knapsack Problem

Program ini mengimplementasikan **Algoritma Genetika (AG)** menggunakan bahasa pemrograman Python untuk menyelesaikan **Knapsack Problem**, yaitu masalah optimasi memilih kombinasi barang dengan nilai terbaik tanpa melebihi kapasitas tas.

---

### 1. Library yang Digunakan

**a. `random`**
Digunakan untuk membangkitkan angka acak dalam seluruh proses Algoritma Genetika, meliputi inisialisasi populasi, seleksi, crossover, dan mutasi.

**b. `matplotlib`**
Digunakan untuk menampilkan grafik perkembangan nilai fitness (terbaik, terburuk, dan rata-rata) dari generasi ke generasi.

**c. `numpy`**
Digunakan sebagai dependensi pendukung dalam operasi numerik.

---

### 2. Struktur Program

Program dibagi menjadi 5 modul terpisah yang saling diimpor oleh `main.py`:

| File | Deskripsi |
|---|---|
| `InisiasiPopulasi.py` | Membangkitkan populasi awal secara acak |
| `EvaluasiFitness.py` | Menghitung nilai fitness setiap individu |
| `selection.py` | Proses seleksi parent (Roulette Wheel & Tournament) |
| `crossover.py` | Proses crossover untuk menghasilkan anak baru |
| `mutation.py` | Proses mutasi untuk menjaga keragaman genetik |
| `main.py` | File utama — menjalankan keseluruhan Algoritma Genetika |

---

### 3. Studi Kasus — Knapsack Problem

Dalam Knapsack Problem, terdapat sejumlah barang dengan nilai dan bobot tertentu. Tujuannya adalah memilih kombinasi barang yang dapat dimasukkan ke dalam tas dengan kapasitas terbatas untuk **memaksimalkan total nilai** tanpa melebihi kapasitas tas.

#### Data Barang

| Barang | Nilai | Bobot |
|---|---|---|
| Barang1 | 60 | 10 |
| Barang2 | 100 | 20 |
| Barang3 | 120 | 30 |
| Barang4 | 90 | 25 |
| Barang5 | 69 | 11 |
| Barang6 | 70 | 9 |
| Barang7 | 80 | 15 |
| Barang8 | 90 | 10 |
| Barang9 | 25 | 3 |

**Kapasitas tas: 50**

#### Representasi Kromosom

Setiap individu direpresentasikan sebagai array biner dengan panjang N (jumlah barang):
- Gen = `1` → barang dipilih
- Gen = `0` → barang tidak dipilih

Contoh: `[1, 0, 1, 0, 1]` → Barang1, Barang3, dan Barang5 dipilih.

---

### 4. Langkah-langkah Algoritma Genetika

#### a. Inisialisasi Populasi (`InisiasiPopulasi.py`)

Populasi awal dibangkitkan secara acak. Setiap individu (kromosom) memiliki gen biner yang dibangkitkan menggunakan `random.randint(0, 1)`.

| Parameter | Nilai |
|---|---|
| `jumlah_populasi` | 20 individu |
| `jumlah_gen` | 9 (sesuai jumlah barang) |

#### b. Evaluasi Fitness (`EvaluasiFitness.py`)

Nilai fitness setiap individu dihitung berdasarkan total nilai barang yang dipilih, dengan syarat total bobot tidak melebihi kapasitas tas.

- Jika total bobot ≤ kapasitas → fitness = total nilai barang
- Jika total bobot > kapasitas → fitness = 0 (penalti)

#### c. Seleksi (`selection.py`)

Dua metode seleksi diimplementasikan:

| Metode | Cara Kerja |
|---|---|
| **Roulette Wheel Selection** | Individu dipilih secara probabilistik berdasarkan proporsi fitness terhadap total fitness populasi |
| **Tournament Selection** | Memilih k individu secara acak, lalu individu dengan fitness tertinggi di antara mereka dipilih sebagai parent |

Pada `main.py`, **Roulette Wheel Selection** digunakan untuk memilih kedua parent.

#### d. Crossover (`crossover.py`)

Tiga metode crossover diimplementasikan:

| Metode | Cara Kerja |
|---|---|
| **One-Point Crossover** | Memotong kromosom di satu titik acak, menukar bagian setelah titik tersebut |
| **Two-Point Crossover** | Memotong di dua titik acak, menukar segmen di antara kedua titik |
| **Uniform Crossover** | Setiap gen dipilih dari salah satu parent berdasarkan mask acak (1 = tukar, 0 = tidak) |

Pada `main.py`, **One-Point Crossover** digunakan dengan probabilitas `prob_crossover = 0.5`.

#### e. Mutasi (`mutation.py`)

Tiga metode mutasi diimplementasikan:

| Metode | Cara Kerja |
|---|---|
| **Swap Mutation** | Menukar posisi dua gen yang dipilih secara acak |
| **Inversion Mutation** | Membalik urutan gen dalam segmen yang dipilih secara acak |
| **Uniform Mutation** | Membalik nilai setiap gen dengan probabilitas `mutation_rate` |

Pada `main.py`, **Swap Mutation** digunakan dengan probabilitas `prob_mutasi = 0.1`.

---

### 5. Parameter Algoritma Genetika (`main.py`)

| Parameter | Nilai |
|---|---|
| `jumlah_generasi` | 50 |
| `jumlah_populasi` | 20 |
| `prob_crossover` | 0.5 |
| `prob_mutasi` | 0.1 |
| `kapasitas_tas` | 50 |

---

### 6. Output Program

**a. Grafik Perkembangan Nilai Fitness**

Grafik menampilkan perkembangan nilai fitness dari generasi ke generasi dengan 3 garis utama:
- **Biru** — Fitness Tertinggi
- **Kuning** — Fitness Terendah
- **Merah** — Fitness Rata-rata

Titik abu-abu menunjukkan nilai fitness seluruh individu di setiap generasi. Nilai yang acak dan tidak rata menunjukkan bahwa Algoritma Genetika memiliki sifat variatif yang tinggi.

**b. Hasil Knapsack Terbaik**

Program menampilkan kombinasi barang terpilih dengan nilai fitness terbaik yang ditemukan selama proses evolusi.

```
Nilai Fitness Terbaik: 329
Total Bobot: 50
Barang Terpilih:
- Barang2
- Barang5
- Barang6
- Barang8
```

---

### 7. Cara Menjalankan Program

```bash
# Install dependencies
pip install matplotlib numpy

# Jalankan setiap modul secara terpisah untuk melihat output masing-masing
python InisiasiPopulasi.py
python EvaluasiFitness.py
python selection.py
python crossover.py
python mutation.py

# Jalankan program utama — menjalankan keseluruhan Algoritma Genetika
python main.py
```
