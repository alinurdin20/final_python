#Mengaktifkan Pandas
import pandas as pd
#Membuat Kelas
class datasiswa:
    #Atribut
    def __init__(self):
        #Frame data dari awal
        self.df = pd.DataFrame(
            {
                'nama':[],
                'kelas':[],
                'nilai':[]
            }
        )
    #Method
    def tambah(self):
        jml_data = int(input("Masukkan Jumlah Data ?"))
        for _ in range(jml_data):
            nama = input("Masukan Nama =")
            kelas = input("Masukan Kelas =")
            nilai = int(input("Masukan Nilai ="))
            #Tambah baris baru di Frame
            self.df.loc[len(self.df)]=[nama,kelas,nilai]
    def update(self):
            #Tambah Ranking
            self.df['Ranking']=self.df['nilai'].rank(ascending='False', method ='dense').astype(int)
            #Tambah Keterangan
            self.df['Keterangan']=self.df['nilai'].apply(lambda x: "Tuntas" if x>=80 else "Belum Tuntas")
    def tampil(self):
        print("\n Data Terbaru ")
        print(self.df.sort_values('Ranking'))
    def hitung(self):
        #Merubah data nilai Frame jadi data python
        data = self.df['nilai'].tolist()
        if not data:
                stats = {
                    'total':0,
                    'rat2':0,
                    'maks':None,
                    'mins':None
                }
        else:
                total=sum(data)
                rat2=total/len(data)
                maks= max(data)
                mins=min(data)
                stats ={
                        'total':total,
                        'rat2':rat2,
                        'maks':maks,
                        'mins':mins
                    }
            #Cetak Hasil
        print(f"\n Data Terbaru ")
        print(f"Total Nilai {stats['total']}")
        print(f"Nilai rata-rata {stats['rat2']:.2f}")
        print(f"Nilai Terbesar {stats['maks']}")
        print(f"Nilai Terkecil {stats['mins']}")
def main():
    #Obyek Baru
    baruku = datasiswa()
    baruku.tambah()
    baruku.update()
    baruku.tampil()
    baruku.hitung()
if __name__ =='__main__':
    main()



            
