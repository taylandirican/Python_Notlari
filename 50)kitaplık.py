kitaplik = ["SAVAŞveBARIŞ"]
def kitap(*isim):
    seçim = input("Ne yapmak istersiniz(KitapAl/KitapKoy):")
    if seçim =="KitapKoy":
        yenikitap = isim
        kitaplik.append(yenikitap)
        print(kitaplik)
    if seçim =="KitapAl":
        if isim in kitaplik:
            olankitap = isim
            kitaplik.remove(olankitap)
            print(kitaplik)
        else:
            print("Kitap kitaplikta bulunmuyor")


a = input("Kİtap İsmi:")
a.strip()
kitap(a)

a = input("Kİtap İsmi:")
a.strip()
kitap(a)




