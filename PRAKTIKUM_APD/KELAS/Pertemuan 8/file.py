#ERROR HANDLING DAN FILE EKSTERNAL
import json
# angka = int(input("Masukan angka"))
# print(angka)

# try:
#     angka = int(input("Masukan angka: "))
#     print(angka)
# except:
#     print("angka bjir")
# else:
#     print("sip")
# finally:
#     print("Selesai")

# try:
#     nama = input("Namamu siapa: ").strip
#     if len(nama) > 5:
#         raise ValueError("Namamu kepanjangan")
#     if not nama.strip():
#         raise ValueError("Gakboleh kosong")
# except ValueError as betul :
#     print(betul)

# def coba():
#     while True:
#         try:
#                angka = int(input("Masukan angka: "))
#                print(angka)
#                break
#         except:
#             print("bukan angka")

# coba()

# file = open('data.txt','r')
# print(file)

# with open('data.txt','r') as file:
#     konten = file.read()
#     print(konten)

# file = open('example.txt', 'w')

path = 'data.json'

def readdata():
    with open(path) as json_file:
        # return json_file
        return json.load(json_file)

def bacadata(data_baru):
    with open('path','w')

