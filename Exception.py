#Ini adalah contoh dari penggunaan fungsi Try dan Except.
try: 
    angka1= 10
    
    angka2= input('Masukkan angka kedua : ')

    hasil= angka1 / int (angka2)
    print('Hasil pembagian : ', hasil)
        
except :
    print('Terjadi kesalahan pembagian')
