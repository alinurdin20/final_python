#Looping menggunakan WHILE
print("=======================")
angka = []  # Inisialisasi list untuk menyimpan angka
while True:
    try:
        a = input("Masukkan angka (atau ketik 'ok' untuk berhenti): ")
        if a.lower() == "ok":
            break  
        angka.append(int(a))  # Konversi input ke integer dan tambahkan ke list
    except ValueError:
        print("Input tidak valid. Masukkan angka atau 'selesai'.")

# Perhitungan dan pengurutan dilakukan di luar loop
angka.sort(reverse=True)  # Urutkan dari besar ke kecil
total = sum(angka)
rate = total / len(angka) if len(angka) > 0 else 0  # Hindari pembagian nol

print("Data yang diinput:", angka)
print("Total Angka :", total)
print("Data rata2 :", rate)
print("Data Terbesar : ", angka[0] if len(angka) > 0 else "Tidak ada data")  # Handle jika list kosong
print("Data Terkecil : ", angka[-1] if len(angka) > 0 else "Tidak ada data")  # Handle jika list kosong
