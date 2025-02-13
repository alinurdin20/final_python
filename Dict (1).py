#Dictionary
print("=======================")
Sekolah = {
    "NPSN" : 20229763,
    "Nama" : "SMP Negeri  2 Tambun Selatan",
    "Alamat" :"Jalan Kebon Kelapa 128 Tambun",
    "No_Tlp" : "02188326407",
    "Kab" : "Kabupaten Bekasi",
    "Prop" : "Jawa Barat",
    "Kode_Pos" : 17510
}
print(Sekolah) #Cetak Semua Key & Value
Sekolah["Kab"]= " Kab Bekasi" #Ganti Value menjadi Kab Bekasi
print()
print(Sekolah.keys()) #Cetak Data Kunci
print(Sekolah.values()) #Cetak Data Nilai
print(Sekolah.items()) #Cetak Kelompok Kunci & Value

