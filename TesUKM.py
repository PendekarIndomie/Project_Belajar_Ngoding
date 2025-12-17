'''Soal 1.1:
Buatlah program yang meminta pengguna untuk memasukkan 5 nilai suhu (dalam derajat Celcius). Program kemudian menampilkan suhu tertinggi dari kelima input tersebut.

Soal 1.2:
Buatlah program yang meminta pengguna untuk memasukkan 4 angka bilangan bulat. Program kemudian menampilkan angka terkecil dari keempat angka yang dimasukkan.

Soal 2.1:
Buatlah program untuk menghitung luas dan keliling persegi panjang berdasarkan panjang dan lebar yang diinput oleh pengguna.

Soal 2.2:
Buatlah program yang menghitung luas lingkaran berdasarkan jari-jari yang diinput pengguna. Gunakan nilai π = 3.14, dan tampilkan hasil dengan 2 angka di belakang koma.

Soal 3.1:
Buatlah program yang meminta pengguna memasukkan dua angka bertipe float. Program menghitung hasil pembagian angka pertama dengan angka kedua,
dan mengecek apakah hasilnya lebih besar dari 10 atau tidak, lalu tampilkan pesan yang sesuai.

Soal 3.2:
Buatlah program yang menghitung diskon harga barang.
Input: harga barang dan persen diskon (float).
Output: total harga setelah diskon.
Tambahkan percabangan:

Jika total harga > 100000 → tampilkan “Pembelian besar”.

Jika tidak → tampilkan “Pembelian kecil”.

Soal 4.1:
Buatlah program yang menampilkan angka dari 1 hingga 20,
tapi hanya menampilkan angka ganjil saja.

Soal 4.2:
Buatlah program yang meminta pengguna memasukkan 5 nilai ujian.
Program akan menghitung rata-rata nilai dan menampilkan kategori:Buatlah program menggunakan nested loop (perulangan bersarang) untuk mencetak pola segitiga bintang berikut: 

Soal 5.1:
Buatlah program menggunakan for loop untuk menampilkan deret bilangan kelipatan 3 dari 3 sampai 30.

Soal 5.2:
Buatlah program menggunakan nested loop (perulangan bersarang) untuk mencetak pola segitiga bintang berikut: (untuk contoh liat ChatGPT)'''

'''#Jawaban soal :
# Soal 1.1
suhu=[]
for i in range(5):
    nilai=float(input(f"Masukkan nilai suhu ke {i+1}: "))
    suhu.append(nilai)
print("Suhu tertinggi adalah:", max(suhu))
print("\n")\

# Soal 1.2
angka=[]
for i in range(4):
    nilai=int(input(f"Masukkan angka ke {i+1}: "))
    angka.append(nilai)
print(f"Bilangan bulat yang terkecil adalah: {min(angka)}")
print("\n")

# Soal 2.1
panjang=float(input(f"Masukkan panjang persegi panjang :"))
lebar=float(input(f"Masukkan lebar persegi panjang :"))
#Rumus luas dan keliling persegi panjang
luas=panjang*lebar
keliling=2*(panjang+lebar)
print(f"Luas persegi panjang adalah : {luas}")
print(f"Keliling persegi panjang adalah : {keliling}")
print("\n")

# Soal 2.2
jari=float(input("Masukkan jari-jari lingkaran :"))
pi=3.14
luas_lingkaran=pi*jari**2
print(f"Luas lingkaran adalah : {luas_lingkaran:.2f}")
print("\n")

# Soal 3.1
angka1=float(input("Masukkan angka pertama (float): "))
angka2=float(input("Masukkan angka kedua (float): "))
hasil=angka1/angka2
if hasil > 10:
    print("Hasil pembagian lebih besar dari 10.")
else:
    print("Hasil pembagian tidak lebih besar dari 10.")
print("\n")

# Soal 3.2
harga_barang=float(input("Masukkan harga barang: "))
persen_diskon=float(input("Masukkan persen diskon: "))/100
diskon=persen_diskon*harga_barang
total_harga=harga_barang-diskon

if total_harga > 100000: 
    print("Pembelian besar")
else: 
    print("Pembelian kecil")
print(f"Total harga setelah diskon adalah: {total_harga}")
print("\n")

#soal 4.1
for i in range(1, 21):
    if i%2!=0 :
        print(f"Berikut adalah bilangan ganjil : {i} ")

#Soal 4.2
nilai_ujian=[]
for i in range(5):
    n=float(input(f"Masukkan nilai {i+1} : "))
    nilai_ujian.append(n)

rata=sum(nilai_ujian)/len(nilai_ujian)

print(f"\n Nilai rata-rata : {rata:.2f}")

if rata >= 85 :
    kategori="Sangat baik"
elif rata >=70 and rata <=84 :
    kategori="Baik"
elif rata >= 60 and rata <= 69 :
    kategori="Cukup baik"
else :
    kategori="Kurang baik"

print(f"\nKategori : {kategori}")

#Soal 5.1
for i in range(3, 31, 3):
    print(f"Angka kelipatan 3 : {i}")

#Saol 5.2
for i in range(1, 6):          # loop luar: baris
    for j in range(i):          # loop dalam: jumlah bintang per baris
        print("*", end="")      # cetak bintang tanpa ganti baris
    print()                     # buat baris baru setelah satu baris selesai'''


#TES LATIHAN  SOAL LEVEL UAS
'''Buatlah program yang meminta pengguna memasukkan panjang dan lebar sebuah taman (dalam meter), lalu hitung:
Luas taman
Keliling taman
Tentukan kategori taman tersebut:
Jika luas > 500 → “Taman Besar”
Jika 200 ≤ luas ≤ 500 → “Taman Sedang”
Jika < 200 → “Taman Kecil”

panjang_taman=float(input("Masukkan panjang taman anda : "))
lebar_taman=float(input("Masukkan lebar taman anda :"))

luas=panjang_taman*lebar_taman
keliling=2*(panjang_taman+lebar_taman)

if luas>500 :
    kategori="Taman besar"
elif 200<=luas<=500:
    kategori="Taman sedang"
else :
    kategori="Taman kecil"

print(f"Luas taman anda \t: {luas:.2f} meter persegi")
print(f"Keliling taman anda\t: {keliling:.2f} meter persegi")
print(f"Kategori taman anda \t: {kategori}")'''

#Soal UTS BARU 
'''Soal 1 (Kisi-kisi 1 – Variabel, Input, Output)

Buatlah program untuk menghitung luas segitiga.
User memasukkan alas dan tinggi, lalu program menampilkan hasil luas segitiga dengan dua angka di belakang koma.
(Gunakan rumus: ½ × alas × tinggi)

Soal 2 (Kisi-kisi 2 – Percabangan / If-Else)

Buat program yang meminta input umur seseorang, lalu tampilkan kategori berikut:

Umur < 13 → “Anak-anak”

Umur 13–17 → “Remaja”

Umur 18–59 → “Dewasa”

Umur ≥ 60 → “Lansia”

Soal 3 (Kisi-kisi 3 – Perulangan / Looping)

Buat program yang menampilkan bilangan kelipatan 3 dari 1 sampai 30 menggunakan perulangan for.
Setelah ditampilkan, tampilkan juga jumlah total bilangan tersebut.

Soal 4 (Kisi-kisi 4 – List dan Manipulasi Data)

Buat program yang meminta user memasukkan 5 nilai ujian mahasiswa, lalu:

Simpan semua nilai ke dalam list,

Hitung dan tampilkan rata-rata nilai,

Tampilkan kategori:

≥ 80 = “Sangat Baik”

60–79 = “Cukup”

< 60 = “Kurang”

Soal 5 (Kisi-kisi 5 – Kombinasi dan Format Output)

Buat program untuk menghitung biaya parkir kendaraan:

2 jam pertama: Rp 5.000

Setiap jam berikutnya: Rp 2.000 per jam
Program harus meminta user memasukkan lama parkir (jam), lalu menampilkan total biaya parkir dengan format uang (Rp dan dua angka di belakang nol).

#NO 1
alas=float(input("Masukkan alas: "))
tinggi=float(input("Masukkan tinggi: "))

luas=1/2*alas*tinggi
print(f"Luas segitiga anda adalah : {luas:.2f} ")

#NO 2
umur=int(input("Berapakah umur anda :"))

print("\n")
if umur<13 :
    kategori="anak-anak"
elif 13<=umur<=17 :
    kategori="Remaja"
elif 18<=umur<=59 :
    kategori="Dewasa"
else :
    kategori="Lansia"

print(f"Anda sudah menginjak di usia {kategori}")

#Nomor 3
for i in range(3, 31, 3):
    print(i)
    total=+i
print("jumlah bilangan total: ", total)

#soal 4
nilai=[]
for i in range(5):
    n=float(input(f"Masukan nilai anda ke-{i+1} :"))
    nilai.append(n)

rata=sum(nilai)/len(nilai)

if rata>=80:
    kategori="Sangat baik"
elif 60<=rata<=79 :
    kategori="baik"
else:
    kategori="kurang baik"

print(f"Rata-rata nilai :{rata:.2f}, dengan kategori : {kategori}")

#Nomor 5
lama_parkir = int(input("Masukkan lama parkir (jam): "))

# Logika perhitungan biaya
if lama_parkir <= 2:
    total = 5000
else:
    total = 5000 + (lama_parkir - 2) * 2000

# Menampilkan hasil dengan format uang
print(f"Total biaya parkir adalah: Rp {total:,.0f}")'''





                  







