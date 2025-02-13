# Membuat Kelas Dasar
class Sekolah:
    def __init__(self, nama, luas):
        self.nama = nama
        self.luas = luas

    def atribut(self):
        print(f"Nama Ruang : {self.nama} Luas Bangunan : {self.luas}")

# Pewarisan dari kelas Sekolah
class RuangKelas(Sekolah):
    def __init__(self, nama, luas, fungsi):
        super().__init__(nama, luas)
        self.fungsi = fungsi
    def atribut(self):
        print(f"Nama Gedung = {self.nama} Luas Gedung = {self.luas} Fungsi Gedung = {self.fungsi}")

# Membuat Obyek
RuangKelas1 = RuangKelas("Kelas 7A","9m x 7 m", "KBM Kelas")

# Menjalankan Metode
RuangKelas1.atribut()
