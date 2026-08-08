# öğrenciler = {}

# name_a = input("Bir isim giriniz")
# name_b = input("Bir isim giriniz")
# name_c = input("Bir isim giriniz")

# surname_a = input("Bir soyisim giriniz")
# surname_b = input("Bir soyisim giriniz")
# surname_c = input("Bir soyisim giriniz")

# tell_a = input("Bir tel no giriniz")
# tell_b = input("Bir tel no giriniz")
# tell_c = input("Bir tel no giriniz")

# No_a = input("Bir no giriniz")
# No_b = input("Bir no giriniz")
# No_c = input("Bir no giriniz")

# öğrenciler = {
#     No_a : {
#         "Ad" : name_a,
#         "Soyad" : surname_a,
#         "TelNo" : tell_a
#     },
#     No_b : {
#         "Ad" : name_b,
#         "Soyad" : surname_b,
#         "TelNo" : tell_b
#     },
#     No_c : {
#         "Ad" : name_c,
#         "Soyad" : surname_c,
#         "TelNo" : tell_c
#     }
# }

# print(öğrenciler)

# i = input("Numarani gir")
# print(öğrenciler[i])

# ogrNo = input("Öğrenci no: ")
# öğrenci = öğrenciler[ogrNo]
# print(öğrenci)

# print(f"Girdiğiniz {i} nolu öğrencinizin adi: {öğrenci['Ad']}, öğrencinizin soyadi: {öğrenci['Soyad']}, öğrencinizin telefon numarasi: {öğrenci['TelNo']}")



ders1 =str(input("Bir ders girinziz"))
ders2 =str(input("Bir ders girinziz"))
ders3 =str(input("Bir ders girinziz"))


üniteler1 =str(input("Bir ünite girinziz"))
üniteler2 =str(input("Bir ünite girinziz"))
üniteler3 =str(input("Bir ünite girinziz"))


sfsay1=int(input("Bir sayi girinziz"))
sfsay2=int(input("Bir sayi girinziz"))
sfsay3=int(input("Bir sayi girinziz"))




dersler = {
    ders1:{
        üniteler1
        ,sfsay1
    },
    ders2:{
        üniteler2
        ,sfsay2
    },
    ders3:{
        üniteler3
        ,sfsay3
    }
}



print(dersler[ders1])





