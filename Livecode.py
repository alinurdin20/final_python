#Aktifkan Pandas
import pandas as pd
#Buat Kelas
class datasiswa:
    #Atribut
    def __init__(self):
    #Membuat Data Frame awal
        self.df = pd.DataFrame(
            {
            'nama':[],
            'kelas':[],
            'nilai':[]
            }
        )
    #Method
    def tambah(self):
        jml_data = int(input("Masukkan Jumlah data ?"))
        for _ in range(jml_data):
            nama = input("Masukkan Nama = ")
            kelas = input("Masukkan kelas = ")
            nilai = int(input("Masukkan Nilai = "))
            #Data baris baru di Frame
            self.df.loc[len(self.df)]=[nama,kelas,nilai]
    
    def update(self):
        #Tambah Ranking
        self.df['Ranking']=self.df['nilai'].rank(ascending='False', method='dense').astype(int)
        #Tambah Keterangan
        self.df['Keterangan']=self.df['nilai'].apply( lambda x: "Tuntas" if x>=80 else "Belum Tuntas")
    def tampil(self):
        print("\n Data Terbaru")
        print(self.df.sort_values('Ranking'))
    def hitung(self):
        data = self.df['nilai'].tolist()
        #Logika 
        if not data:
                stats = {
                    'total':0,
                    'rat2':0,
                    'maks':None,
                    'mins':None
                }
        else:
                total = sum(data)
                rat2 = total/len(data)
                maks = max(data)
                mins = min(data)
        stats = {
                        'total':total,
                        'rat2':rat2,
                        'maks':maks,
                        'mins':mins
                    }
        #Tampilan
        print(f"\n Data Terbaru ")
        print(f"Total Nilai {stats['total']}")
        print(f"Rata-Rata Nilai {stats['rat2']:.2f}")
        print(f"Maksimum {stats['maks']}")
        print(f"Minimum {stats['mins']}")
def main():
    #Obyek baru 
    baruku = datasiswa()
    baruku.tambah()
    baruku.update()
    baruku.tampil()
    baruku.hitung()
if __name__ =='__main__':
    main()