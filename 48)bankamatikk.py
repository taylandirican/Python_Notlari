hesapA= {
    "AD":"Taylan Dirican",
    "HESAPNO":"12345",
    "BAKİYE":3000,
    "EKHESAP":2000
}

hesapB= {
    "AD":"Eray Dirican",
    "HESAPNO":"67890",
    "BAKİYE":6000,
    "EKHESAP":5000
}


# def paraçek(hesap, miktar):
#     print(f"Merhaba {hesap['AD']}")
#     if hesap["BAKİYE"]>=miktar:
#         hesap["BAKİYE"]-miktar
#         print(f"Hesabinizdan {miktar} tutar çekilmişir,Bakiyenizde{hesap['BAKİYE']} tutar kalmiştir")
#     else:
#         a = str(input("Bakiyenizde yeterli tutarda para yoktur, EKHESAP kullanmak istiyor musunuz(E/H):"))
    
#     if a == "E" and (hesap["BAKİYE"]+hesap["EKHESAP"])>=miktar:
#         toplam =hesap["BAKİYE"]+hesap["EKHESAP"]
#         b = toplam - miktar
#         hesap["EKHESAP"] = b
#         print(f"Bakiyenizde para kalmamiştir,Ekhesabinizda {hesap['EKHESAP']} tutar kalmiştir,para çekilmiştir")
#     else:
#         print("Para çekilememiştir.")
#kendi yaptığım kod karmaşık olduğu için hatayı bulamıyorum
# paraçek(hesapA,1000)




def paraçek(hesap, miktar):
    print(f"Merhaba {hesap['AD']}")
    sorgulama(hesap)
    if hesap["BAKİYE"]>=miktar:
        hesap["BAKİYE"]-=miktar
        print(f"Hesabinizdan {miktar} tutar çekilmişir,Bakiyenizde{hesap['BAKİYE']} tutar kalmiştir")

    else:
        toplam =hesap["BAKİYE"]+hesap["EKHESAP"] 

        if toplam >=miktar:
                a = input("ek hesap kullanilsin mi(e/h)")

                if a =="e":
                        toplam =hesap["BAKİYE"]+hesap["EKHESAP"]
                        ekhesapkullanilacak = miktar - hesap["BAKİYE"]
                        hesap["EKHESAP"] -=ekhesapkullanilacak 
                        print(f"paranizi alabilirsiniz, ek hesabinizda {hesap['EKHESAP']} tutar kalmiştir")

                else:
                        print(f"{hesap['HESAPNO']} nolu hesabinizda {hesap['BAKİYE']} tutar kalmiştir")

        else:
            print("Para çekilememiştir.")

def sorgulama(hesap):
      print(f"{hesap['HESAPNO']} nolu hesabinizda {hesap['BAKİYE']}tutar vardir")


paraçek(hesapA,1000)
print("***********************")
paraçek(hesapA,3000)
print("***********************")
paraçek(hesapA,2000)








