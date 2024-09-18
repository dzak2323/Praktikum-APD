nama = str(input("masukan nama anda: "))
umur = int(input("masukan umur anda: "))
tinggi = float(input("masukan tinggi anda(CM): "))
jawaban = (input("apakah anda bisa mengendarai motor(ya/tidak): ")).lower()

total = (umur + tinggi)

print(f"""
=============================
    Bio Data Anda
=============================
Nama                    : {nama}
Umur                    : {umur}
tinggi                  : {tinggi}
apakah bisa?            : {'ya' if jawaban  == 'ya' else 'tidak'}"
total variabel numerik  : {total}
=============================""")