# Praktek Operator
print(" =================== " )   
while True:     
    try:
        A = int(input("Masukkan angka Ke-1 ?"))
        break
    except ValueError:
        print("Yang dimasukkan bukan angka bulat")
while True:
    try:
        B = int(input("Masukkan angka Ke-2 ?"))
        break
    except ValueError:
        print("Yang dimasukkan bukan angka bulat")    
penjumlahan = A+B 
perkalian = A*B
pembagian = A/B
perpangkatan = A**B
pengurangan = A-B
modulus = A%B
print("Hasil Penjumlahan  ",A,"+",B,"=",penjumlahan)
print("Hasil Pengurangan ",A,"-",B,"=",pengurangan)
print("Hasil Perkalian  ",A,"x",B,"=",perkalian)
print("Hasil Pembagian  ",A,":",B,"=",pembagian)
print("Hasil Perpangkatan  ",A,"^",B,"=",perpangkatan)
print("Hasil Sisa Pembagian ",A,"%",B,"=", modulus)