#Berikut ini adalah contoh konversi data implisit dan eksplisit.
#Konversi data implisit itu dilakukan secara otomatis oleh python.
#Sedangkan Konversi data eksplisit itu dilakukan secara manual oleh programmer/developer/user.

#Contoh konversi data menggunakan if else (contoh buat program login akun)
akun = {"Fitra": "Erectus123", "Fatimah": "Cantik123"}

def login():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password:")

    if username in akun and akun [username] == password: 
        print("Login berhasil! selamat datang ", username)

    else: 
        print("Login gagal! username atau password salah.")

        if __name__ == "__main__":
            login()