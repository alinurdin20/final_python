#Memasukkan  Pandas
import pandas as pd
#Membuat kelas
class datasiswa:
    #Atribut Kelas
    def __init__(self):
        #Membuat Tabel Data Frame dari Kosong
        self.df = pd.DataFrame(
            {
                'nama':[],
                'kelas':[],
                'nilai':[]
            }
        )
    #Method Kelas
    def tambah(self):
        jml_data = int(input("Maasukkan Jumlah Data :"))
        for _ in range(jml_data):
            nama = input("Masukkan Nama :")
            kelas = input("Masukkan Kelas :")
            nilai = int(input("Masukkan Nilai :"))
            #Buat baris di dataFrame
            self.df.loc[len(self.df)]=[nama,kelas,nilai]
    def update(self):
        #Membuat Kolom Ranking
        self.df['Ranking'] = self.df['nilai'].rank(ascending = False, method ='dense').astype(int)
        #Membuat Kolom keterangan
        self.df['Keterangan'] = self.df['nilai'].apply(lambda x: "Tuntas" if x>=80 else "Belum Tuntas")
    #Menampilkan Data Terbaru
    def terbaru(self):
        print("Data Terbaru")
        print(self.df.sort_values('Ranking'))
    #statistik
    def statistik(self):
        #Mengambil data Nilai menjadi List Python
        data = self.df['nilai'].tolist()
        #Logika data
        if not data :
                stats=  {
                    "total" : 0,
                    "rata_rata":0,
                    "maks": None,
                    "mins": None
                }  
        else :
                total = sum(data)  
                rata_rata = total / len(data)
                maks = max(data)
                mins = min(data)
                stats = {
                    "total": total,
                    "rata_rata" : rata_rata,
                    "maks": maks,
                    "mins": mins
                }
    #Menampilkan hasil
        print("\nHasil Terbaru")
        print(f"Jumlah Nilai = {stats['total']}")
        print(f"Rata-Rata Nilai = {stats['rata_rata']:.2f}")
        print(f"Nilai Terbesar = {stats['maks']}")
        print(f"Nilai Terkecil = {stats['mins']}")

def main():
    #obyek baru
    df_baru = datasiswa()
    #tambah data
    df_baru.tambah()
    #update data
    df_baru.update()
    #Tampilkan Data Terbaru
    df_baru.terbaru()
    #Tampilkan Hitung
    df_baru.statistik()
if __name__=='__main__':
        main()