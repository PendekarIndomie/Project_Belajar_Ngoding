#Nama : Muhammad Fitra Ramadhan 
#NIM : 2512500766
#Kelas : XF 
#Program Studi : Sistem Informasi

#Jawaban soal latihan di pertemuan 11 
# FUNGSI UNTUK VALIDASI INPUT ANGKA
def input_integer(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            return nilai
        except ValueError:
            print("Data yang anda input salah, silakan dicoba lagi\n")



# FUNGSI MENGHITUNG RATA-RATA TUGAS

def rata_rata_tugas(jumlah):
    total = 0
    for i in range(1, jumlah + 1):
        nilai = input_integer(f"Masukan Nilai Tugas ke-{i} : ")
        total += nilai
    return total / jumlah



# FUNGSI MENGHITUNG NILAI AKHIR

def nilai_akhir(uts, uas, quiz, rttugas):
    return (uts * 0.3) + (uas * 0.4) + (quiz * 0.1) + (rttugas * 0.2)



# FUNGSI MENENTUKAN INDEKS DAN PREDIKAT

def indeks_predikat(na):
    if na >= 85:
        return "A", "BAIK SEKALI"
    elif na >= 75:
        return "B", "BAIK"
    elif na >= 65:
        return "C", "CUKUP"
    elif na >= 50:
        return "D", "KURANG"
    else:
        return "E", "GAGAL"



# PROSEDUR UNTUK MENAMPILKAN HASIL

def tampilkan_hasil(na, indeks, predikat, rttugas):
    print("\nNilai Akhir        :", round(na, 1))
    print("Nilai indeks       :", indeks)
    print("Nilai Predikat     :", predikat)
    print("Rata-Rata Tugas    :", round(rttugas, 1))



# PROGRAM UTAMA (PROSEDUR)

def main():
    print("***************************************")
    print("     PROGRAM HITUNG NILAI MAHASISWA    ")
    print("***************************************\n")

    uts = input_integer("Masukan Nilai UTS : ")
    uas = input_integer("Masukan Nilai UAS : ")
    quiz = input_integer("Masukan Nilai QUIZ : ")

    banyak_tugas = input_integer("Masukan Banyak Tugas : ")
    rttugas = rata_rata_tugas(banyak_tugas)

    # untuk hitung nilai akhir
    na = nilai_akhir(uts, uas, quiz, rttugas)

    # indeks & predikat
    indeks, predikat = indeks_predikat(na)

    # hasil
    tampilkan_hasil(na, indeks, predikat, rttugas)

    # untuk nanya ulang program atau tidak
    ulang = input("\nNah COBA LAGI (y/t)? ")
    if ulang.lower() == "y":
        print("\n")
        main()


# JALANKAN PROGRAM
main()
