#DICTIONARY
import os
os.system("cls" if os.name == "nt" else "clear")


# # print(data_mhs["nama"])

# print(data_mhs.get("tes"),'hah?')

# for data in data_mhs:
#     print(data)

# for key_data, value_data in data_mhs.items():
#     print(f"key:, {key_data},value:,{value_data} ")

# data_mhs['alamat']='Samarinda'

# data_mhs.update({"alamat":"samarinda"})
# data_mhs.update({"alamat":"semarang"})

# data_mhs = {
# "nama":"jak",
# 'NIM': 2409106056,
# "Prodi": "Imformatika",
# "Kelas": "B'2024"
# }

# del data_mhs['NIM']

# hapus = data_mhs.pop('NIM')
# print(data_mhs)
# print(hapus)

# data_mhs['no'] = hapus
# print(data_mhs)

# print(data_mhs.clear(), "clear")

# key = "apel", "jeruk", "mangga","semangka","anggur"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)
# Nilai = {
# "Matematika" : 90,
# "B. Indonesia" : 80,
# "Biologi" : 80,
# "Kimia" : 70
# }
# print(Nilai)
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# print(Nilai)

# datamhs={
# "nama":"ucup",
# "nim": 1,
# "matkul":["APD",'KALKULUS',"JARKOM"],
# "Dosen" : {"nama":"Pak Awang",
#            "matkul":"APD"}}

# print(datamhs["Dosen"]["nama"])

datamhs=[{
"nama":"ucup",
"role":"user"
},
{
"nama":"jak",
"role":"admin"
}]

print(datamhs[0]["nama"])