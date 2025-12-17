#Ini adalah contoh tipe Numeric di python.

#perkalian
kali1= 5
kali2= 4
hasilkali= kali1 * kali2 #untuk perkalian di tandai dengan (*)

print("hasil perkalian", hasilkali)

#pembagian
bagi1= 20
bagi2= 5
hasilbagi= bagi1 / bagi2 #untuk pembagian di tandai dengan (/)
print("\n")
print("hasil pembagiannya adalah", hasilbagi)

#penjumlahan dan pengurangan
tambah1= 15
tambah2= 15
kurang1= 10
kurang2= 5

hasiltambah= tambah1 + tambah2 #untuk penjumlahan di tandai dengan (+)
hasilkurang= kurang1 - kurang2 #untuk pengurangan di tandai dengan (-)
hasilgabungan= tambah1 + tambah2 - kurang1 - kurang2
print("\n") 
print("hasil penjumalahan adalah", hasiltambah)
print("hasil pengurangan adalah", hasilkurang)
print("hasil secara total adalah", hasilgabungan)

#Modulus 
modul1= 10
modul2= 4
hasilmodul= modul1 % modul2 #untuk modulus di tandai dengan (%)
print("\n") 
print("hasil modulus adalah", hasilmodul)

#pangkat
pangkat1= 5
hasilpangkat= pangkat1 ** 2 #untuk pangkat di tandai dengan (**2 untuk kuadrat,
# (**3 untuk kubik))
print("\n") 
print("hasil pangkat adalah", hasilpangkat)

#Rumus Pythagoras
sisi=3
sisi2=4
sisimiring= (sisi**2 + sisi2**2) **0.5

sisimiring2= (sisi**2 + sisi2**2) **(1/2)

import math
sisimiring3= math.sqrt(sisi**2 + sisi2**2)

#bisa juga pakai ini: math.sqrt(sisi**2 + sisi2**2)
# TAPI HARUS PAKE FUNGSI IMPORT (contoh: Import math) atau bisa juga
# (sisi**2 + sisi2**2) **(1/2)
print("\n") 
print("sisi miringnya adalah", sisimiring)
print("sisi miringnya2 adalah", sisimiring2)
print("sisi miringnya3 adalah", sisimiring3)


#contoh menerapkan operator dengan tipe numeric
#pada fungsi if dan else.
a=10
b=12
if a>b : 
    print("\n A adalah variabel terbesar")
else : 
    print("\n B adalah variabel terbesar")






