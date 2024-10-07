import os
os.system("cls" if os.name == "nt" else "clear")

datauser = [['admin1', 'admin123', 'admin'],
            ['jaki1', 'jakjak', 'NPC'],
            ['fulan', 'npc123', 'NPC']]

koleksihotwheels = []

def tambahkoleksi():
    print("""
=======================
    Tambah Koleksi
=======================""")
    nama = input("Masukkan nama mobil: ")
    tahun = input("Masukkan tahun mobil: ")
    warna = input("Masukkan warna mobil: ")
    koleksihotwheels.append([nama, tahun, warna])
    print("Koleksi berhasil ditambahkan")
    input("Enter...")

def tampilkankoleksi():
    print("""
=========================
 Menampilkan koleksi
=========================""")
    if not koleksihotwheels:
        print("Koleksi Hot Wheels Anda masih kosong.")
    else:
        print("Daftar Koleksi Hot Wheels:")
        for index, mobil in enumerate(koleksihotwheels, start=1):
            print(f"{index}. Nama: {mobil[0]}, Tahun: {mobil[1]}, Warna: {mobil[2]}")
    input("Enter...")

def editkoleksi():
    tampilkankoleksi()
    if koleksihotwheels:
        indexadmin_input = input("Pilih nomor koleksi yang ingin diedit: ")
        if indexadmin_input.isdigit():
            indexadmin = int(indexadmin_input) - 1
            if 0 <= indexadmin < len(koleksihotwheels):
                print("Apa yang ingin Anda edit?")
                print("1. Nama")
                print("2. Tahun")
                print("3. Warna")
                pilihan = input("Masukkan pilihan (1/2/3): ")
                if pilihan == "1":
                    koleksihotwheels[indexadmin][0] = input("Masukkan nama baru: ")
                elif pilihan == "2":
                    koleksihotwheels[indexadmin][1] = input("Masukkan tahun baru: ")
                elif pilihan == "3":
                    koleksihotwheels[indexadmin][2] = input("Masukkan warna baru: ")
                else:
                    print("Pilihan tidak valid")
                print("Koleksi berhasil diupdate")
            else:
                print("Koleksi tidak ditemukan")
        else:
            print("Input tidak valid")
    input("Enter...")

def hapuskoleksi():
    tampilkankoleksi()
    if koleksihotwheels:
        indexdelete_input = input("Pilih nomor koleksi yang ingin dihapus: ")
        if indexdelete_input.isdigit():
            indexdelete = int(indexdelete_input) - 1
            if 0 <= indexdelete < len(koleksihotwheels):
                koleksihotwheels.pop(indexdelete)
                print("Koleksi berhasil dihapus!")
            else:
                print("Koleksi tidak ditemukan.")
        else:
            print("Input tidak valid, Silakan masukkan angka yang tertera")
    input("Enter...")

def menuadmin():
    while True:
        print("""
==============================
      Anda masuk menu admin
==============================
1. Tampilkan koleksi
2. Tambah koleksi
3. Edit koleksi
4. Hapus koleksi
5. Keluar
""")
        inputadmin = input("Masukkan pilihanmu wahai admin: ")

        if inputadmin == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tampilkankoleksi()
        elif inputadmin == "2":
            os.system("cls" if os.name == "nt" else "clear")
            tambahkoleksi()
        elif inputadmin == "3":
            os.system("cls" if os.name == "nt" else "clear")
            editkoleksi()
        elif inputadmin == "4":
            os.system("cls" if os.name == "nt" else "clear")
            hapuskoleksi()
        elif inputadmin == "5":
            print("Keluar dari menu admin terima kasih!")
            break
        else:
            print("Pilihan tidak valid")

def login():
    percobaan = 3
    while percobaan > 0:
        print("""
================================
    Anda memilih menu login
================================""")
        loginuser = input('Silahkan masukkan username anda: ')
        loginpass = input('Silahkan masukkan password anda: ')

        userfound = False
        for user in datauser:
            if loginuser == user[0] and loginpass == user[1]:
                userfound = True
                if user[2] == 'admin':
                    print(f'Selamat datang, {loginuser}, Anda login sebagai admin.')
                    menuadmin()
                elif user[2] == 'NPC':
                    print(f'Selamat datang, {loginuser}, Anda login sebagai NPC.')
                    input("Enter...")
                    menuuser()

                return
        
        if not userfound:
            percobaan -= 1
            print(f"Username atau sandi salah, sisa percobaan: {percobaan}")

        if percobaan == 0:
            print("Sudah salah 3x wak, tekunci sudah akun mu")
            break

def register():
    print("""
================================
      Anda memilih Register
=================================""")
    userregis = input("Username: ")
    users = False
    for user in datauser:
        if user[0] == userregis:
            users = True
            break
    
    if users:
        print("Sudah ada yang pakai, silahkan pilih yang lain")
    else:
        passregis = input("Password: ")
        datauser.append([userregis, passregis, 'NPC'])
        print(f"Akun Anda berhasil terdaftar dengan ID: {userregis} sebagai NPC.")
        input("Enter...")
        os.system("cls" if os.name == "nt" else "clear")

def menuuser():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""
==============================
      Anda masuk menu user
==============================
1. Tampilkan koleksi
2. Keluar
""")
        inputuser = input("Masukkan pilihanmu wahai NPC: ")

        if inputuser == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tampilkankoleksi()
        elif inputuser == "2":
            print("Keluar dari menu NPC, Terima kasih")
            break
        else:
            print("Pilihan anda tidak valid")

def mainmenu():
    while True:
        print(f"""
=================================================================
                           MENU LOGIN
=================================================================
1. Login
2. Register
3. Cancel
""")
        userinput = input("Masukkan pilihan: ")
        if userinput == '1':
            os.system("cls" if os.name == "nt" else "clear")
            login()
        elif userinput == '2':
            os.system("cls" if os.name == "nt" else "clear")
            register()
        elif userinput == '3':
            os.system("cls" if os.name == "nt" else "clear")
            print("Terimakasih telah mencoba program saya :)")
            break
        else:
            print("Pilihan anda tidak valid")

mainmenu()



    

