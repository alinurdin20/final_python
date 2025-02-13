import pandas as pd

# Data awal di DataFrame
df = pd.DataFrame({
    'Nama': ['Ali', 'Budi', 'Citra', 'Dian'],
    'Kelas': ['7A', '7B', '7C', '7D'],
    'Nilai': ['80', '90', '78', '68']
})

# Konversi kolom Nilai menjadi integer
df['Nilai'] = df['Nilai'].astype(int)

# Menambahkan data baru secara dinamis
jumlah_data = int(input("Berapa data tambahan yang ingin dimasukkan? "))

for _ in range(jumlah_data):
    nama = input("Masukkan nama: ")
    kelas = input("Masukkan kelas: ")
    nilai = int(input("Masukkan nilai: "))

    # Tambahkan data baru ke DataFrame
    df.loc[len(df)] = [nama, kelas, nilai]

# Tambahkan kolom ranking berdasarkan nilai
df['Ranking'] = df['Nilai'].rank(ascending=False, method='dense').astype(int)

# Tambahkan kolom Keterangan (TUNTAS jika nilai >= 80)
df['Keterangan'] = df['Nilai'].apply(lambda x: "TUNTAS" if x >= 80 else "BELUM TUNTAS")

print("\nDataFrame dengan Data Baru, Peringkat, dan Keterangan:")
print("========================================================")
print(df.sort_values('Ranking'))

# Menghitung statistik nilai
def hitung(data):
    if len(data) == 0:
        return {
            "total": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None
        }

    total = sum(data)
    rata_rata = total / len(data)
    minimum = min(data)
    maksimum = max(data)

    return {
        "total": total,
        "rata_rata": rata_rata,
        "minimum": minimum,
        "maksimum": maksimum
    }

# Memanggil fungsi hitung
nilai_list = df['Nilai'].tolist()
hasil = hitung(nilai_list)

print("\nHasil perhitungan:")
print(f"Jumlah Nilai : {hasil['total']}")
print(f"Rata-rata : {hasil['rata_rata']:.2f}")
print(f"Nilai Terkecil : {hasil['minimum']}")
print(f"Nilai Terbesar: {hasil['maksimum']}")
