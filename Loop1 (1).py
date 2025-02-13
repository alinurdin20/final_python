#Looping menggunakan FOR
print("=======================")
jml = int(input("Masukkan jumlah data yang ingin diinput: "))
angka = []  # Membuat list kosong untuk menyimpan angka
for i in range(jml):
  data = int(input(f"Masukkan data ke-{i}: "))
  i += 1
  angka.append(data) 
  angka.sort(reverse=True)
  total = sum(angka)
  rate = total / len(angka)
print("Data yang diinput:", angka) 
print("Total Angka :", total)
print("Data rata2 :", rate)
print("Data Terbesar : ", angka[0])
print("Data Terkecil : ", angka[-1])




