# Praktek LIST
print("=====================")
# List kosong
list_kosong = []
# List dengan elemen integer
angka = [1, 2, 3, 4, 5]
# List dengan elemen string
nama = ["Ali", "Budi", "Cica"]
# List dengan elemen campuran
campuran = angka + nama 

# Mengubah data indeks 5
campuran[5]= "Ali Nurdin"
# Menambah data 10
campuran.append(10)
# Menyisipkan data Rini di indeks 4
campuran.insert(4,"Rini")
# Menghapus data Ali Nurdin
campuran.pop(6)
campuran.remove(2)
# Mengakses elemen pertama (index 0)
data1 = campuran[0]  
# Mengakses elemen terakhir (index -1)
dataN = campuran[-1] 

print("data campuran =",campuran)
print("data ke-1 = ",data1)
print("data Terakhir =",dataN)