class Kendaraan:
    def __init__(self, merk, jenis, tahun, kecepatan=0):
        self.merk = merk
        self.jenis = jenis
        self.tahun = tahun
        self.kecepatan = kecepatan

    def ON_mesin(self):
        print(f"{self.merk} {self.jenis} mesin dinyalakan.")

    def OFF_mesin(self):
        print(f"{self.merk} {self.jenis} mesin dimatikan.")

    def tambah_kecepatan(self, tambahan):
        self.kecepatan += tambahan
        print(f"Kecepatan {self.merk} sekarang: {self.kecepatan} km/jam")

    def rem(self):
        self.kecepatan = 0
        print(f"{self.merk} telah berhenti.")

# Membuat objek dari kelas Kendaraan
mobil = Kendaraan("Toyota", "SUV", 2020)
motor = Kendaraan("Yamaha", "Sport", 2021)

# Menggunakan metode pada objek mobil
mobil.ON_mesin()
mobil.tambah_kecepatan(40)
mobil.rem()
mobil.OFF_mesin()

print("\n")

# Menggunakan metode pada objek motor
motor.ON_mesin()
motor.tambah_kecepatan(60)
motor.OFF_mesin()
