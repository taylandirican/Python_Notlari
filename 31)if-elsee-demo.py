# isim = input("Ad:")
# Yaş = int(input("Yaş:"))
# E_durumu = input("E_durumu(ortaokul, lise, vb.):")
# if (Yaş>=18) and (E_durumu == "lise" or E_durumu == "üniversite"):
#      print("Ehliyet Alabilir")
# else:
#      print("Ehliyet Alamaz")


# ilknot = int(input("ilk yazili sonucu:"))
# ikincinot = int(input("ikinci yazili sonucu:"))
# sözlü = int(input("sözlü sonucu:"))
# ort = (ilknot+ikincinot+sözlü)/3
# print(ort)
# if 0<=ort<=24:
#     print("0")
# elif 25<=ort<=44:
#     print("1")
# elif 45<=ort<=54:
#     print("2")
# elif 55<=ort<=69:
#     print("3")
# elif 70<=ort<=84:
#     print("4")
# elif 85<=ort<=100:
#     print("5")

# days = int(input("araciniz kaç gündür trafikte: "))
# if days <=365:
#     print("1. Bakim")
# elif 365<days<=365*2:
#     print("2. Bakim")
# elif 365*2<days<=365*3:
#     print("3. Bakim")
# else:
#     print("hata")



# import datetime
# tarih = (input("araciniz hangi tarihte trafiğe çikti (2019/8/9): "))
# tarih = tarih.split("/")
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

# simdi = datetime.datetime.now()
# print(simdi)
# trafiğeçikiş = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# fark = simdi-trafiğeçikiş
# print(fark.days)
# days = fark.days
# if days <=365:
#       print("1. Bakim")
# elif 365<days<=365*2:
#       print("2. Bakim")
# elif 365*2<days<=365*3:
#       print("3. Bakim")
# else:
#      print("hata")
