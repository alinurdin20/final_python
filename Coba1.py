data = []
# Menentukan jumlah data yang ingin dimasukkan
n = int(input("Berapa banyak data yang ingin dimasukkan? "))
for _ in range(n):
    while True:
        try:
            dt = float(input("Masukkan data (angka): "))  # Konversi input menjadi float
            data.append(dt)
            break
        except ValueError:
            print("Masukkan nilai numerik yang valid.")

print("Data yang dimasukkan:", data)
print("=======================")


def hitung(data):  # Nama fungsi Hitung dengan parameter data

    # Proses perhitungan menggunakan nilai parameter data
    total = sum(data)
    rata_rata = total / len(data) if len(data) > 0 else 0  
    minimum = min(data) if len(data) > 0 else None
    maksimum = max(data) if len(data) > 0 else None

    # Mengembalikan hasil ke fungsi Hitung
    return {
        "total": total,
        "rata_rata": rata_rata,
        "minimum": minimum,
        "maksimum": maksimum
    }


# Memanggil fungsi hitung dan mencetak hasil
hasil = hitung(data)
print("Hasil perhitungan:")
print(f"Total: {hasil['total']}")
print(f"Rata-rata: {hasil['rata_rata']}")
print(f"Minimum: {hasil['minimum']}")
print(f"Maksimum: {hasil['maksimum']}")
