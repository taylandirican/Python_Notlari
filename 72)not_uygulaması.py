def Notlari_oku():
    with open("sinavnotlari.txt","r",encoding="utf-8") as file:
       for satir in file:
           print(satir.split(","))
        #    print(satir) 



def not_gir():
    ad =input("Öğrenci adi: ")
    soyad =input("Öğrenci soyadi: ")
    not1 =input("Öğrenci notu1: ")
    not2 =input("Öğrenci notu2: ")
    not3 =input("Öğrenci notu3: ")

    with open("sinavnotlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+ soyad+ ":,"+not1+","+not2+","+not3+","+"\n")

def notlari_kayit():
    pass

while True:
    islem = input("1 - notlari oku\n2-not gir\n3-notlari kayit et\n4- çikiş\n")

    if islem =="1":
        Notlari_oku()
    elif islem =="2":
        not_gir()
    elif islem =="3":
        notlari_kayit()
    else:
        break


