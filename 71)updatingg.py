file = open("newfile2.txt","w",encoding="utf-8")
with open("newfile2.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    print(file.write("deneme"))

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

# ******Sayfa Sonunda Güncelleme******
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nTaylan Dirican")


# ******Sayfa Başında Güncelleme******
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Taylan\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

#*****Sayfa Ortasında Güncelleme

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     liste = file.readlines()
#     liste.insert(1,"Mauro İcardi\n")
#     file.seek(0)
#     file.writelines(liste)
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())