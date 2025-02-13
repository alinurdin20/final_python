# Membuat kelas dasar
class Hewan:
    def __init__(self, nama, suara):
        self.nama = nama
        self.suara = suara

    def bersuara(self):
        print(f"{self.nama} bersuara {self.suara}")


# Pewarisan dari kelas Hewan
class Kucing(Hewan):
    def __init__(self, nama, suara, warna_bulu):
        super().__init__(nama, suara)
        self.warna_bulu = warna_bulu

    # Overriding metode bersuara
    def bersuara(self):
        print(f"{self.nama}, yang berbulu {self.warna_bulu}, bersuara {self.suara}")


# Polimorfisme dengan metode yang sama pada berbagai kelas
class Anjing(Hewan):
    def __init__(self, nama, suara, jenis):
        super().__init__(nama, suara)
        self.jenis = jenis

    def bersuara(self):
        print(f"{self.nama} adalah anjing {self.jenis} yang bersuara {self.suara}")


# Membuat objek dari kelas Kucing dan Anjing
kucing1 = Kucing("Kitty", "Meow", "Putih")
anjing1 = Anjing("Doggo", "Guk Guk", "Bulldog")

# Menjalankan metode bersuara
kucing1.bersuara()
anjing1.bersuara()
