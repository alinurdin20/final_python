import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import io
import os
import re
from tabulate import tabulate

class DataSiswa:
    FILE_PATH = os.path.join('D:\\python_Ali\\barCSV', 'dat1.csv')  
    # Gunakan double backslash atau raw string (r'...')

    def __init__(self):
        self.df = self.load_data()  # Inisialisasi DataFrame
        
    def tambah(self):
        try:
            jml_data = int(input("Masukkan jumlah data: "))
        except ValueError:
            print("Input jumlah data harus berupa angka.")
            return

        for _ in range(jml_data):
            nama = self.validasi_input("Masukkan Nama: ", r'^[a-zA-Z\s]+$')
            kelas = self.validasi_input("Masukkan Kelas: ", r'^[a-zA-Z\s]+$')
            nilai = self.validasi_nilai("Masukkan nilai siswa (0-100): ")

            new_data = pd.DataFrame({'nama': [nama], 'kelas': [kelas], 'nilai': [nilai]})
            self.df = pd.concat([self.df, new_data], ignore_index=True)

        self.simpan_data()

    def load_data(self):
        try:
            df = pd.read_csv(self.FILE_PATH)
            # Tangani NaN secara konsisten di load_data
            df['nilai'].fillna(0, inplace=True)
            return df
        except FileNotFoundError:
            print("File CSV tidak ditemukan. Membuat file baru.")
            return pd.DataFrame(columns=['nama', 'kelas', 'nilai'])  # Mengembalikan DataFrame kosong
        except pd.errors.EmptyDataError:
            print("File CSV kosong. Membuat file baru.")
            return pd.DataFrame(columns=['nama', 'kelas', 'nilai'])  # Mengembalikan DataFrame kosong
        except Exception as e:  # Menangkap error umum
            print(f"Terjadi kesalahan saat membaca file CSV: {e}")
            return pd.DataFrame(columns=['nama', 'kelas', 'nilai'])  # Mengembalikan DataFrame kosong


    def validasi_input(self, prompt, regex):
        while True:
            data = input(prompt)
            if re.match(regex, data):
                return data
            else:
                print("Input tidak valid. Silakan coba lagi.")

    def validasi_nilai(self, prompt):
        while True:
            try:
                nilai = float(input(prompt))
                if 0 <= nilai <= 100:
                    return nilai
                else:
                    print("Nilai harus antara 0 dan 100.")
            except ValueError:
                print("Input harus berupa angka.")

    
    def update(self):
        if not self.df.empty:
            # Opsi 1: Mengisi NaN dengan 0
            self.df['nilai'].fillna(0, inplace=True)
            self.df['Ranking'] = self.df['nilai'].rank(ascending=False, method='dense').astype(int)

            # Opsi 2: Menggunakan pd.Int64Dtype() (pilih salah satu)
            # self.df['Ranking'] = self.df['nilai'].rank(ascending=False, method='dense').astype('Int64')

            self.df['Keterangan'] = self.df['nilai'].apply(lambda x: "Tuntas" if x >= 80 else "Belum Tuntas")
            self.simpan_data()

    def tampilkan_data(self):
        if not self.df.empty:
            print("\nData Siswa:")
            print(tabulate(self.df.sort_values('Ranking'), headers='keys', tablefmt='fancy_grid'))
        else:
            print("Tidak ada data yang tersedia.")

    def statistik(self):
        if self.df.empty:
            print("\nTidak ada data untuk dihitung statistiknya.")
            return

        stats = {
            "total": self.df['nilai'].sum(),
            "rata_rata": self.df['nilai'].mean(),
            "maks": self.df['nilai'].max(),
            "mins": self.df['nilai'].min(),
            "median": self.df['nilai'].median(),
            "std": self.df['nilai'].std(),
            "var": self.df['nilai'].var()
        }

        print("\nHasil Statistik:")
        for key, value in stats.items():
            print(f"{key.capitalize()}: {value:.2f}")

    def simpan_data(self):
        self.df.to_csv(self.FILE_PATH, index=False)
        print("Data telah disimpan ke dalam CSV.")

    def buat_pdf(self, nama_file):
        if self.df.empty:
            print("Tidak ada data untuk dibuat PDF.")
            return

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=self.df.values, colLabels=self.df.columns, loc='center')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        im = Image.open(buf)
        im.save(nama_file, "PDF", resolution=100.0)
        buf.close()
        im.close()
        print(f"File PDF telah dibuat: {nama_file}")

def main():
    data_siswa = DataSiswa()

    while True:
        pilihan = input("\nPilih operasi (tambah/lihat/statistik/pdf/keluar): ").lower()

        if pilihan == 'tambah':
            data_siswa.tambah()
            data_siswa.update()
        elif pilihan == 'lihat':
            data_siswa.tampilkan_data()
        elif pilihan == 'statistik':
            data_siswa.statistik()
        elif pilihan == 'pdf':
            data_siswa.buat_pdf("data_siswa.pdf")
        elif pilihan == 'keluar':
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()