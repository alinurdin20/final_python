# Praktek Variabel
print("=====================")
while True:
    try:
        masuk_angka = int(input("Masukkan anggka bulat ? "))
        break
    except ValueError:
        print("Yang Anda Masukkan Bukan  Bilangan Bulat")
        
if masuk_angka < 0:
    print("Angkanya bilangan negatif")
else :
    print("Yang Anda masukkan = ", masuk_angka)
