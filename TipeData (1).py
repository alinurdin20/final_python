# Praktek Tipe Data 
print( " ==================== ")
nama = input("Masukkan Nama Anda :")
alamat = input("Masukkan Alamat Anda :")
usia = int(input("Usia Anda : "))
tinggi = float(input("Tinggi Anda (Angka Pecahan) :"))
status_menikah = input("Status Menikah? (ya/tidak): ")
menikah = status_menikah.lower() == "ya" 
print("==============")
#Mencetak isi variabel
print (" Nama Lengkap :", nama)
print (" Tipe data ( NAMA )  :", type(nama))
print("-------------------------")
print (" Alamat :", alamat)
print (" Tipe data ( ALAMAT )  :", type(alamat))
print("-------------------------")
print (" Usia :" , usia)
print (" Tipe data ( USIA )  :", type(usia))
print("-------------------------")
print (" Tinggi :", tinggi)
print (" Tipe data ( TINGGI )  :", type(tinggi))
print("-------------------------")
if(menikah):
  print ("Status : Menikah ")
  print (" Tipe data ( MENIKAH )  :", type(menikah))
  print("-------------------------")
else:
  print (" Status : Belum Menikah ")
  print (" Tipe data ( MENIKAH)  :", type(menikah))
  print("-------------------------")