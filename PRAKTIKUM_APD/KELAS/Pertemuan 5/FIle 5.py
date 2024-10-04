# data = [1,2,3,4,5,True,"jaki",[2,3]]
    # data_1 = list(1,2,3,4,5)
# print(data[7][0])

# buah = ["apel","melon","anggur"]
# print(buah)
# print()

# buah.append("semnagka")
# print(buah)

# buah.insert(0,"rambutan")
# print()
# print(buah)

# buah.extend(["rambutan","semangka"])
# print(buah)

# print(len(buah))

# buah[0] = "kelengkeng"
# print (buah)

# del buah[1]
# print (buah)

# buah.pop(1)
# print (buah)

# buah.remove("apel")
# print (buah)

dataMahasiswa = [
    ["056","dzaki",["apd","basdat"]],
    ["055", "devon"]
    ]
# print (dataMahasiswa[0][2][0])

buah = ["apel","melon","anggur"]

# for data in buah:
#     index = 1
#     print(f"data ke {index + 1}")
#     print(data)
#     print ("="*10)

for index , item in enumerate(dataMahasiswa):
    print(f"data ke {index + 1}")
    print(f"username {dataMahasiswa[0][1]}")
    print
    print
   