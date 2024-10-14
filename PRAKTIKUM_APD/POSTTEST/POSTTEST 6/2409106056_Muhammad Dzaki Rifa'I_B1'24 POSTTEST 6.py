import os
os.system("cls" if os.name == "nt" else "clear")


datauser = {
    'admin1': {'password': 'admin123', 'role': 'admin'},
    'jaki1': {'password': 'jakjak', 'role': 'NPC'},
    'fulan': {'password': 'npc123', 'role': 'NPC'}
}

koleksihotwheels = {}

def tambahkoleksi():
    print("""
=======================
    Tambah Koleksi
=======================""")
    nama = input("Masukkan nama mobil: ")
    tahun = input("Masukkan tahun mobil: ")
    warna = input("Masukkan warna mobil: ")
    koleksihotwheels[nama] = {'tahun': tahun, 'warna': warna}
    print("Koleksi berhasil ditambahkan")
    input("Enter...")
    os.system("cls" if os.name == "nt" else "clear")

def tampilkankoleksi():
    print("""
=========================
 Menampilkan koleksi
=========================""")
    if not koleksihotwheels:
        print("Koleksi Hot Wheels Anda masih kosong.")
    else:
        print("Daftar Koleksi Hot Wheels:")
        for index, (nama, detail) in enumerate(koleksihotwheels.items(), start=1):
            print(f"{index}. Nama: {nama}, Tahun: {detail['tahun']}, Warna: {detail['warna']}")
    input("Enter...")
    

def editkoleksi():
    tampilkankoleksi()
    if koleksihotwheels:
        nama = input("Masukkan nama mobil yang ingin diedit: ")
        if nama in koleksihotwheels:
            print("Apa yang ingin Anda edit?")
            print("1. Nama")
            print("2. Tahun")
            print("3. Warna")
            pilihan = input("Masukkan pilihan (1/2/3): ")
            if pilihan == "1":
                nama_baru = input("Masukkan nama baru: ")
                koleksihotwheels[nama_baru] = koleksihotwheels.pop(nama)  
            elif pilihan == "2":
                koleksihotwheels[nama]['tahun'] = input("Masukkan tahun baru: ")
            elif pilihan == "3":
                koleksihotwheels[nama]['warna'] = input("Masukkan warna baru: ")
            else:
                print("Pilihan tidak valid")
            print("Koleksi berhasil diupdate")
        else:
            print("Mobil tidak ditemukan")
        input("Enter...")
    

def hapuskoleksi():
    tampilkankoleksi()
    if koleksihotwheels:
        nama = input("Masukkan nama mobil yang ingin dihapus: ")
        if nama in koleksihotwheels:
            del koleksihotwheels[nama]
            print(f"Koleksi mobil {nama} berhasil dihapus!")
        else:
            print("Mobil tidak ditemukan.")
    input("Enter...")
    os.system("cls" if os.name == "nt" else "clear")

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

        if loginuser in datauser and datauser[loginuser]['password'] == loginpass:
            if datauser[loginuser]['role'] == 'admin':
                print(f'Selamat datang, {loginuser}, Anda login sebagai admin.')
                input("Enter...")
                os.system("cls" if os.name == "nt" else "clear")
                menuadmin()
            elif datauser[loginuser]['role'] == 'NPC':
                print(f'Selamat datang, {loginuser}, Anda login sebagai NPC.')
                input("Enter...")
                os.system("cls" if os.name == "nt" else "clear")
                menuuser()
            return
        else:
            percobaan -= 1
            print(f"Username atau sandi salah, sisa percobaan: {percobaan}")

        if percobaan == 0:
            print("Sudah salah 3x wak, terkunci sudah akun mu")
            break

def register():
    print("""
================================
      Anda memilih Register
=================================""")
    userregis = input("Username: ")
    if userregis in datauser:
        print("Sudah ada yang pakai, silahkan pilih yang lain")
    else:
        passregis = input("Password: ")
        datauser[userregis] = {'password': passregis, 'role': 'NPC'}
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
