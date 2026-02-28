import kurs
import konverter
from tabulate import tabulate

#Fungsi Menampilkan Tabel Kurs
def tampilkan_tabel():
    data_tabel = [[k, f'{v:,.0f}'.replace(',', '.')]
              for k, v in kurs.kurs_uang.items()]
    
    #Judul Program
    print("\n=== KONVERTER MATA UANG ===")

    #Tampilkan Tabel Kurs
    print (tabulate(data_tabel, headers= ['Kode', 'Kurs'], tablefmt="grid"))

#Jalankan Tabel
tampilkan_tabel()

#Input
mata_uang = input("\nDari (IDR/USD/EUR/JPY): ").upper()
konversi = input("Ke (IDR/USD/EUR/JPY): ").upper()
jumlah = float(input("Jumlah: "))

#Koversi
if mata_uang == "IDR":
    hasil = konverter.konversi_dari_IDR(jumlah, konversi)
    print()
    print(f"Rp {jumlah} = {round(hasil,2)} {konversi}")

elif konversi == "IDR":
    hasil = konverter.konversi_ke_IDR(jumlah, mata_uang)
    print()
    print(f"{jumlah} {mata_uang} = Rp {int(hasil):,}".replace(',', '.'))

else:
    print("Mata Uang Tidak Ditemukan!")
    