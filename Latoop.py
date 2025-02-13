class AnggotaPerpustakaan:
    def __init__(self, ID, Nama, Alamat):
        self.ID = ID
        self.Nama = Nama
        self.Alamat = Alamat
        self.DaftarBukuYangDipinjam = []

    def PinjamBuku(self, buku):
        if buku.StatusKetersediaan == "Tersedia":
            self.DaftarBukuYangDipinjam.append(buku)
            buku.Dipinjam()
            print(f"{self.Nama} berhasil meminjam {buku.Judul}")
        else:
            print(f"{buku.Judul} sedang tidak tersedia")

    def KembalikanBuku(self, buku):
        if buku in self.DaftarBukuYangDipinjam:
            self.DaftarBukuYangDipinjam.remove(buku)
            buku.Dikembalikan()
            print(f"{self.Nama} berhasil mengembalikan {buku.Judul}")
        else:
            print(f"{buku.Judul} tidak dipinjam oleh {self.Nama}")

    def LihatDaftarPinjaman(self):
        print("Daftar buku yang dipinjam:")
        for buku in self.DaftarBukuYangDipinjam:
            print(f"- {buku.Judul}")

class Buku:
    def __init__(self, ISBN, Judul, Pengarang, Penerbit, TahunTerbit):
        self.ISBN = ISBN
        self.Judul = Judul
        self.Pengarang = Pengarang
        self.Penerbit = Penerbit
        self.TahunTerbit = TahunTerbit
        self.StatusKetersediaan = "Tersedia"

    def Dipinjam(self):
        self.StatusKetersediaan = "Dipinjam"

    def Dikembalikan(self):
        self.StatusKetersediaan = "Tersedia"

class Katalog:
    def __init__(self):
        self.DaftarBuku = []

    def CariBuku(self, judul):
        for buku in self.DaftarBuku:
            if buku.Judul == judul:
                return buku
        return None

    def TambahBuku(self, buku):
        self.DaftarBuku.append(buku)

    def HapusBuku(self, buku):
        if buku in self.DaftarBuku:
            self.DaftarBuku.remove(buku)

# Contoh Penggunaan
katalog = Katalog()
buku1 = Buku("978-0321765723", "The Lord of the Rings", "J.R.R. Tolkien", "Allen & Unwin", 1954)
buku2 = Buku("978-0743273565", "Pride and Prejudice", "Jane Austen", "Penguin Classics", 1813)
katalog.TambahBuku(buku1)
katalog.TambahBuku(buku2)

anggota1 = AnggotaPerpustakaan("A001", "Budi", "Jakarta")
anggota1.PinjamBuku(buku1)
anggota1.KembalikanBuku(buku1)
anggota1.LihatDaftarPinjaman()