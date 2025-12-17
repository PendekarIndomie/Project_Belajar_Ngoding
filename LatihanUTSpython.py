#Ini adalah latihan coding buat uts python

'''Nomor 1 Buat sebuah program untuk menginput NIM.
Apabila yang diinput bukan NIM anda maka tampilkan pada layar tulisan MOHON PERIKSA
KEMBALI NIM ANDA
Apabila yang diinput adalah NIM anda maka tampilkan pada layar tulisan:
INI ADALAH NIM SAYA
NIM: 0123456789
NAMA: RYO OWATARI
FAKULTAS : FTI
*
NIM dan nama sesuai dengan identitas masing-masing, diatas hanya contoh*'''

#Jawaban nomor 1
'''nim="2512500766"
nama="Fitra"
Fakultas="FTI"

while True :
    Nim_input=input("Masukkan NIM anda\t:")
    if Nim_input==nim :
        print("Ini adalah NIM Saya")
        print(f"NIM\t:{nim}")
        print(f"Nama\t:{nama}")
        print(f"Fakultas:{Fakultas}")
        print("\n")
        print("Selamat datang")
        break
    else :
        print("Mohon periksa kembali NIM Anda!")'''


'''Buat sebuah program untuk melakukan input bilangan bulat
Jika bilangan tersebut kurang dari 200 maka tampilkan pada layar tulisan KURANG DARI 200
Jika bilangan tersebut adalah 170 maka tampilkan pada layar tulisan SAMA DENGAN 180
Jika bilangan tersebut adalah 100 maka tampilkan pada layar tulisan SAMA DENGAN 90
Jika bilangan tersebut adalah 50 maka tampilkan pada layar tulisan SAMA DENGAN 55
Jika bilangan tersebut adalah 50 maka tampilkan pada layar tulisan SAMA DENGAN 55
Jika bilangan tersebut kurang dari 55 maka tampilkan pada layar tulisan KURANG DARI 55'''

#Jawaban nomor 2
'''b=int(input("Masukkan bilangan bulat :"))

if b==170:
    print("Angka Anda SAMA DENGAN 180")
elif b==100:
    print("Angka Anda SAMA DENGAN 90")
elif b==50:
    print("Angka Anda SAMA DENGAN 55")
elif b<55: 
    print("Angka Anda KURANG DARI 55")
elif b<200 :
    print("Angka Anda KURANG DARI 200")
else :
    print("BILANGAN TIDAK SESUAI KONDISI")'''

'''Buat sebuah proram untuk melakukan input bilangan bulat
Jika bilangan tersebut genap maka tampilkan pada layar tulisan BILANGAN GENAP
Jika bilangan tersebut ganjil maka tampilkan pada layar tulisan BILANGAN GANJIL'''

#Jawaban nomor 3
#while True: #Cuma iseng nambah kalo perlu gak usah di tambah
bil=int(input("Masukkan bilangan anda\t:"))
if bil==0:
    print("Bilangan Nol")
elif bil%2==0:
    print("Bilangan Genap")
else:
    print("Bilangan Ganjil")
print("\n")
print("Mantap")

'''Buat sebuah program untuk melakukan input Nim, Nama, nilai presensi, nilai tugas, nilai UTS dan nilai
UAS
Tampilkan pada layar nilai tugas, nilai UTS, nilai UAS dan NILAI FINAL
Sebagai catatan, formula untuk mendapatkan nilai akhir adalah
30% nilai_tugas + 30% nilai_uts + 40% nilai_uas
*
NIM dan nama sesuai dengan identitas masing-masing*'''

#Jawaban nomor 4
