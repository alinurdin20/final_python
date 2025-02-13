# Praktek Comparesion
print(" ================ ")
# Untuk mengubah Nilai jadi kreteria A, B, C, D, E
while True:
    try:
        N = int(input("Masukkan Nilai = "))
        break
    except ValueError:
        print("Harusnya Nilai Bulat")
if 90 <=N<=100:
    print("A")
elif 80<=N<90:
    print("B")
elif 70<=N<80:
    print("C")
elif 60<=N<70:
    print("D")
else:
    print("E")
print("------------------")
print(" Perbandingan Angka A = 80 & B = 75")
A=80
B=75
print("-------------------")
print(" A == B")
if A==B:
    print("Angka",A,"Sama Dengan",B)
else:
    print("Angka",A,"Tidak Sama Dengan",B)
print("-------------------")
print(" A > B")
if A>B:
    print("Angka",A,"Lebih Dari",B)
else:
    print("Angka",A,"Kurang Dari",B)
print("-------------------")
print(" A < B")
if A<B:
    print("Angka",A,"Kurang Dari",B)
else:
    print("Angka",A,"Lebih Dari",B)
print("-------------------")
print(" A != B")
if A!=B:
    print("Angka",A,"Tidak Sama Dengan",B)
else:
    print("Angka",A,"Sama Dengan",B)