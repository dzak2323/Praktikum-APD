import os

if os.name == 'nt':  
    os.system('cls')


print(f"""
=================================================================
                           MENU LOGIN
=================================================================
""")

username_benar = "dzaki"  
password_benar = "056"    
percobaan = 3
while percobaan > 0:
    username_input = input("Silahkan masukan username anda: ")
    password_input = input("Silahkan masukan sandi anda: ")    
    if username_input == username_benar and password_input == password_benar:
        print(f"Username dan sandi anda benar, selamat datang {username_benar}")
        if os.name == 'nt':  
           os.system('cls')
        
        
        while True:
            print(f"""
            ======================================================================
                       Kalkulator Bangun Ruang Kubus dan Balok             
            ======================================================================
                        Silahkan pilih dengan mengetikan angka
             1. Volume Kubus
             2. Luas permukaan kubus
             3. Keliling kubus
             4. Volume Balok
             5. Luas Balok
             6. Keliling Balok
             7. Keluar
            ======================================================================
            """)

            pilihan = input("Silahkan pilih menu: ")

            if pilihan == '1':
                print("Anda memilih opsi satu yaitu penghitungan volume kubus")
                sisi_kubus = float(input("Silahkan masukan panjang sisi kubus: "))
                volume_kubus = (sisi_kubus * sisi_kubus * sisi_kubus)
                print("Volume kubus anda adalah:", volume_kubus)
                if os.name == 'nt':  
                   os.system('cls')

            elif pilihan == "2":
                print("Anda memilih opsi 2 yaitu perhitungan luas permukaan kubus")
                sisi_kubus = float(input("Silahkan masukan panjang sisi kubus: "))
                luas_permukaan_kubus = ((sisi_kubus * sisi_kubus) * 6)
                print("Luas permukaan kubus anda adalah:", luas_permukaan_kubus)
                if os.name == 'nt':  
                   os.system('cls')

            elif pilihan == "3":
                print("Anda memilih opsi 3 yaitu perhitungan keliling kubus")
                sisi_kubus = float(input("Silahkan masukan panjang sisi kubus: "))
                keliling_kubus = (sisi_kubus * 12)
                print('Keliling kubus anda adalah:', keliling_kubus)
                if os.name == 'nt':  
                   os.system('cls')

            elif pilihan == "4":
                print("Anda memilih opsi 4 yaitu perhitungan volume balok")
                panjang_balok = float(input("Silahkan masukan panjang balok: "))
                lebar_balok = float(input("Silahkan masukan lebar balok: "))
                tinggi_balok = float(input("Silahkan masukan tinggi balok: "))
                volume_balok = (panjang_balok * lebar_balok * tinggi_balok)
                print("Volume balok anda adalah:", volume_balok)
                if os.name == 'nt':  
                   os.system('cls')

            elif pilihan == "5":
                print("Anda memilih opsi 5 yaitu perhitungan luas balok")
                panjang_balok = float(input("Silahkan masukan panjang balok: "))
                lebar_balok = float(input("Silahkan masukan lebar balok: "))
                tinggi_balok = float(input("Silahkan masukan tinggi balok: "))
                luas_balok = (2 * ((panjang_balok * lebar_balok) + (panjang_balok * tinggi_balok) + (lebar_balok * tinggi_balok)))
                print("Luas balok anda adalah:", luas_balok)
                if os.name == 'nt':  
                   os.system('cls')

            elif pilihan == "6":
                print("Anda memilih opsi 6 yaitu perhitungan keliling balok")
                panjang_balok = float(input("Silahkan masukan panjang balok: "))
                lebar_balok = float(input("Silahkan masukan lebar balok: "))
                tinggi_balok = float(input("Silahkan masukan tinggi balok: "))
                keliling_balok = (4 * (panjang_balok + lebar_balok + tinggi_balok))
                print("Keliling balok anda adalah:", keliling_balok)
                if os.name == 'nt':  
                   os.system('cls')

            elif pilihan == "7":
                print("Terima kasih telah mencoba aplikasi saya :) ")
                break 

            else:
                print("Pilihan anda tidak valid. Silahkan coba lagi.")
        break  
    
    else:
        percobaan -= 1
        print(f"Login gagal, pastikan sandi atau username sudah benar, percobaan tersisa {percobaan}")
        
        if percobaan == 0:
            print("Percobaan anda telah habis, silahkan keluar") 
            break  

