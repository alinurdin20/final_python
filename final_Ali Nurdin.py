# Mengaktifkan database python
import pandas as pd

# Membuat KELAS DataFrameOOP
class DataFrameOOP :
	# Atribut Kelas
	def __init__(self):
	# Inisialisasi DataFrame Awal
		self.df=pd.DataFrame(
			{ 'Nama' : [],
			  'Kelas' : [],
			  'Nilai' : []
			})
	# Method Kelas
	def tambah(self):
		jml_data = int(input("Berapa jumlah data yang ingin dimasukkan ? "))
		for _ in range(jml_data):
			Nama = input("Masukkan Nama : ")
			Kelas = input("Masukkan Kelas : ")
			Nilai = int(input("Masukkan Nilai : "))
			# Menambah baris baru ke DataFrame
			self.df.loc[len(self.df)] = [Nama,Kelas,Nilai]
	def update(self):
        # Membuat Kolom Ranking Nilai Tertinggi Ranking 1
            self.df['Ranking'] = self.df['Nilai'].rank(ascending=False, method='dense').astype(int)
        # Membuat Kolom Keterangan
            self.df['Keterangan'] = self.df['Nilai'].apply(lambda x: "Tuntas" if x >= 80 else "Belum Tuntas")
	def display_DataFrame(self):
		# Menampikan Data Baru di DataFrame
		print(" Data Terbaru ...")
		print(self.df.sort_values('Ranking'))
	def statistik(self):
    # Mengambil data dari kolom 'Nilai' dan mengonversinya menjadi list.
    # Pastikan nama kolom sesuai dengan yang ada di DataFrame (misalnya 'Nilai' dengan huruf kapital).
            data = self.df['Nilai'].tolist()

    # Jika list data kosong, tetapkan nilai default.
            if not data:
                    stats = {
                        "total": 0,
                        "rata_rata": 0,
                        "maks": None,
                        "min": None
                     }
            else:
                    total = sum(data)
                    rata_rata = total / len(data)
                    maksimum = max(data)
                    minimum = min(data)
                    stats = {
                        "total": total,
                        "rata_rata": rata_rata,
                        "maks": maksimum,
                        "min": minimum
                    }
    
    # Menampilkan hasil perhitungan statistik.
            print("\nHasil Terbaru")
            print(f"Jumlah Nilai    = {stats['total']}")
            print(f"Rata-Rata Nilai = {stats['rata_rata']:.2f}")
            print(f"Nilai Maksimum  = {stats['maks']}")
            print(f"Nilai Minimum   = {stats['min']}")

def main():
	# Membuat Objek baru
	df_baru = DataFrameOOP()
	# Tambah Data
	df_baru.tambah()
	# Update Data
	df_baru.update()
	# Tampilkan DataFrame
	df_baru.display_DataFrame()
	# Statistik
	df_baru.statistik()

if __name__=='__main__':
	main()

