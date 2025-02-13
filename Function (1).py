#Function
print("=======================")
def hitung(data):  # Nama fungsi Hitung dengan parameter data

    # Proses perhitungan menggunakan  nilai parameter data
    total = sum(data)
    rata_rata = total / len(data) if len(data) > 0 else 0  
    minimum = min(data) if len(data) > 0 else None
    maksimum = max(data) if len(data) > 0 else None
    # Mengembalikan ke fungsi Hitung
    return {
        "total": total,
        "rata_rata": rata_rata,
        "minimum": minimum,
        "maksimum": maksimum
    }
# Contoh penggunaan:
angka = [10, 20, 30, 40, 50] # Nilai Parameter
hasil = hitung(angka) # Memasukkan Fungsi Hitung ke Hasil

print("Data Angka :", angka)
print("Hasilnya ...:", hasil)