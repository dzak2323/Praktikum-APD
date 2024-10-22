import os


BatasKoleksi = 100
Koleksi = 0
datauser = {
    'admin1': {'password': 'admin123', 'role': 'admin'},
    'jaki1': {'password': 'jakjak', 'role': 'NPC'},
    'fulan': {'password': 'npc123', 'role': 'NPC'}
}
koleksiHotwheels = {}


def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")


def tambahkanKoleksi(nama, tahun, warna):
    global koleksiHotwheels
    koleksiHotwheels[nama] = {'tahun': tahun, 'warna': warna}
    print("Koleksi berhasil ditambahkan")
    input("Enter...")


def tampilkanKoleksi():
    bersihkanLayar()
    print("""
========================= 
  Menampilkan koleksi 
=========================""")
    if not koleksiHotwheels:
        print("Koleksi Hot Wheels Anda masih kosong.")
    else:
        print("Daftar Koleksi Hot Wheels:")
        for index, (nama, detail) in enumerate(koleksiHotwheels.items(), start=1):
            print(f"{index}. Nama: {nama}, Tahun: {detail['tahun']}, Warna: {detail['warna']}")
    input("Enter...")


def tambahKoleksi():
    global Koleksi
    print("""
======================= 
    Tambah Koleksi 
=======================""")
    nama = input("Masukkan nama mobil: ")
    tahun = input("Masukkan tahun mobil: ")
    warna = input("Masukkan warna mobil: ")
    tambahkanKoleksi(nama, tahun, warna)
    Koleksi += 1

def editKoleksi():
    tampilkanKoleksi()
    if koleksiHotwheels:
        nama = input("Masukkan nama mobil yang ingin diedit: ")
        if nama in koleksiHotwheels:
            print("Apa yang ingin Anda edit?")
            print("1. Nama")
            print("2. Tahun")
            print("3. Warna")
            pilihan = input("Masukkan pilihan (1/2/3): ")
            if pilihan == "1":
                namaBaru = input("Masukkan nama baru: ")
                koleksiHotwheels[namaBaru] = koleksiHotwheels.pop(nama)
            elif pilihan == "2":
                koleksiHotwheels[nama]['tahun'] = input("Masukkan tahun baru: ")
            elif pilihan == "3":
                koleksiHotwheels[nama]['warna'] = input("Masukkan warna baru: ")
            else:
                print("Pilihan tidak valid")
            print("Koleksi berhasil diupdate")
        else:
            print("Mobil tidak ditemukan")
    input("Enter...")

def hapusKoleksi():
    tampilkanKoleksi()
    if koleksiHotwheels:
        nama = input("Masukkan nama mobil yang ingin dihapus: ")
        if nama in koleksiHotwheels:
            del koleksiHotwheels[nama]
            print(f"Koleksi mobil {nama} berhasil dihapus!")
        else:
            print("Mobil tidak ditemukan.")
    input("Enter...")
    bersihkanLayar()

def totalKoleksi(i=0):
    if i >= len(koleksiHotwheels):
        print(f"Total koleksi Hot Wheels Anda: {i}")
        input("Enter...")
        return
    totalKoleksi(i + 1)

def menuAdmin():
    while True:
        bersihkanLayar()
        print("""
============================== 
    Anda masuk menu admin 
==============================
1. Tampilkan koleksi
2. Tambah koleksi
3. Edit koleksi
4. Hapus koleksi
5. Total koleksi
6. Keluar""")
        inputadmin = input("Masukkan pilihanmu wahai admin: ")
        if inputadmin == "1":
            bersihkanLayar()
            tampilkanKoleksi()
        elif inputadmin == "2":
            bersihkanLayar()
            tambahKoleksi()
        elif inputadmin == "3":
            bersihkanLayar()
            editKoleksi()
        elif inputadmin == "4":
            bersihkanLayar()
            hapusKoleksi()
        elif inputadmin == "5":
            bersihkanLayar()
            totalKoleksi()
        elif inputadmin == "6":
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
=================================""")
        loginuser = input('Silahkan masukkan username anda: ')
        loginpass = input('Silahkan masukkan password anda: ')
        if loginuser in datauser and datauser[loginuser]['password'] == loginpass:
            if datauser[loginuser]['role'] == 'admin':
                print(f'Selamat datang, {loginuser}, Anda login sebagai admin.')
                input("Enter...")
                bersihkanLayar()
                menuAdmin()
            elif datauser[loginuser]['role'] == 'NPC':
                print(f'Selamat datang, {loginuser}, Anda login sebagai NPC.')
                input("Enter...")
                bersihkanLayar()
                menuUser()
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
        bersihkanLayar()

def menuUser():
    while True:
        bersihkanLayar()
        print("""
==============================
    Anda masuk menu user
==============================
1. Tampilkan koleksi
2. Keluar""")
        inputuser = input("Masukkan pilihanmu wahai NPC: ")
        if inputuser == "1":
            bersihkanLayar()
            tampilkanKoleksi()
        elif inputuser == "2":
            print("Keluar dari menu NPC, Terima kasih")
            break
        else:
            print("Pilihan anda tidak valid")

def mainMenu():
    while True:
        print(f"""
=================================================================
                           MENU LOGIN
=================================================================
1. Login
2. Register
3. Cancel""")
        userinput = input("Masukkan pilihan: ")
        if userinput == '1':
            bersihkanLayar()
            login()
        elif userinput == '2':
            bersihkanLayar()
            register()
        elif userinput == '3':
            bersihkanLayar()
            print("Terimakasih telah mencoba program saya :)")
            break
        else:
            print("Pilihan anda tidak valid")

mainMenu()