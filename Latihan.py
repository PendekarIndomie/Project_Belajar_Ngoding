'''#latihan penggunaan f-string (nomor 1)
nama = "budi"
umur = 18 
tinggi = 170.5 

print(f"nama saya {nama}, umur saya {umur}, dan tinggi saya {tinggi}")

#latihan penggunaan operasi aritmatika (nomor 2)
panjang = 10
lebar = 5
pi = 3.14
r = 7

luas_lingkaran = pi * (r**2)
print("\n")
print(f"luas lingkaran dengan jari-jari {r} adalah {luas_lingkaran}")

print("=======================")
#Nomor 1
x=5
y=2.5
hitung=(x**2+y**2)/(x*y)
print(hitung)

print("\n")
#nomor 2

a=[3, 1, 4, 1, 5]
a.append(9)
del a[1]
print(a)
print("\n")

#Nomor 3
t=(2, 4, 6, 8)
print(t[3])
print(t[2:4])

print("\n")

#Nomor 4
buah={"Apel":5, "jeruk":3,}
buah["pisang"]= 7
print(buah)

print("\n")

#Nomor 5
angka=int(input("Masukkan angka yang ingin di hitung :"))
hitung=(angka^3)
print(hitung)
print(type(hitung))

print("\n")

#Nomor 6
angka=int(input("Masukkan angka anda: "))
if angka>0 :
    print("Angka yang telah input anda adalah bilangan positif")
elif angka<0 :
    print("Angka yang telah anda input adalah bilangan negatif")
else:
    print("Bilangan nol")'''
print("\n")

#Nomor 7
for i in range(2, 21, 2):
    print(i, end= " ")

print("\n")

#Nomor 7


