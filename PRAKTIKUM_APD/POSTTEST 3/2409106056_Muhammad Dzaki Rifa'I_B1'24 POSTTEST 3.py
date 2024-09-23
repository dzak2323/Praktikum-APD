import os


if os.name == 'nt':  
    os.system('cls')




print(f"""
======================================================================
           Kalkulator Bangun Ruang kubus dan balok             
======================================================================
            Silahkan pilih dengan mengetikan angka
 1.Volume Kubus
 2.Luas permukaan kubus
 3.keliling kubus
 4.Volume balok
 5.luas balok
 6.keliling balok
 7.Keluar
======================================================================
      """)

pilihan = input("Silahkan pilih menu: ")

if pilihan == '1':
    print("Anda memilih opsi satu yaitu penghitungan volume kubus")
    sisi_kubus = float(input("silahkan masukan panjang sisi kubus: "))
    volume_kubus= (sisi_kubus * sisi_kubus * sisi_kubus)
    print("volume kubus anda adalah: ", volume_kubus)

elif pilihan == "2":
     print("Anda memilih opsi 2 yaitu perhitungan luas permukaan kubus")
     sisi_kubus = float(input("silahkan masukan panjang sisi kubus anda: "))
     luas_Permukaan_kubus = ((sisi_kubus * sisi_kubus) * 6)
     print("Luas permukaan kubus anda adalah: ", luas_Permukaan_kubus)

elif pilihan == "3":
    print("Anda memilih opsi 3 yaitu perhitungan keliling kubus")
    sisi_kubus = float(input("silahkan masukan panjang sisi kubus anda: "))
    keliling_kubus = (sisi_kubus * 12)
    print('keliling kubus anda adalah: ', keliling_kubus)

elif pilihan == "4":
    print("Anda memilih opsi 4 yaitu perhitungan volume balok")
    panjang_balok = float(input("Silahkan masukan panjang balok anda: "))
    lebar_balok = float(input("Silahkan masukan lebar balok anda: "))
    tinggi_balok = float(input("Silahkan masukan tinggi balok anda: "))
    volume_balok = (panjang_balok * lebar_balok * tinggi_balok)
    print("Volume balok anda adalah:", volume_balok)

elif pilihan == "5":
    print("Anda memilih opsi 5 yaitu perhitungan luas balok")
    panjang_balok = float(input("Silahkan masukan panjang balok anda: "))
    lebar_balok = float(input("Silahkan masukan lebar balok anda: "))
    tinggi_balok = float(input("Silahkan masukan tinggi balok anda: "))
    luas_balok = (2 * ((panjang_balok * lebar_balok) + (panjang_balok * tinggi_balok) + (lebar_balok * tinggi_balok)))
    print("luas balok anda adalah: ",luas_balok)

elif pilihan == "6":
    print("Anda memilih opsi 6 yaitu perhitungan keliling balok")
    panjang_balok = float(input("Silahkan masukan panjang balok anda: "))
    lebar_balok = float(input("Silahkan masukan lebar balok anda: "))
    tinggi_balok = float(input("Silahkan masukan tinggi balok anda: "))
    keliling_balok = (4 * (panjang_balok + lebar_balok + tinggi_balok))
    print("keliling balok anda adalah: ", keliling_balok)

elif pilihan == "7":
    print("Terimakasih telah mencoba aplikasi saya :) ")
    
else:
    print("Pilihan anda tidak valid")




    




