# try:
#     file = open("newfile2.txt","r")
# except FileNotFoundError:
#     print("Dosya yok")
# finally:
#     print("Dosya kapandi")
#     file.close



file=open("newfile.txt","r", encoding="utf-8")

# for döngüsü

for i in file:
    print(i,end="")


#read() fonksiyonu

content1 = file.read()
print("İçerik1")
print(content1)


content2 = file.read()
print("İçerik2")
print(content2)

content = file.read(6)
content = file.read(7)
content = file.read(7)

print(content)


#readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")


#readlines() fonksiyonu

# liste = file.readlines()
# print(liste[0])
# print(liste[1])
# print(liste[2])





file.close()