
def sayHello(name="user"):
    print("Hello " + name)

sayHello("Taylan")
sayHello()

# def sayHello(name="user"):
#    return "Hello "+ name
# msg  = sayHello("Taylan")

# print(msg)


# def total(num1, num2):
#     return num1 + num2
# result = total(10,20)
# print(result)


def yasHesapla(dogumYili):
    return 2026 - dogumYili
ageTaylan = yasHesapla(2008)

print(ageTaylan)


def Mezunolmayakaçyil(dogumYili, isim):
    '''
    DOCSTRİNG: Doğum yiliniza göre mezun olmaniza kaç yil kaldi
    INPUT: Doğum yili, isim
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 24 - yas

    if emeklilik > 0:
        print(f"Mezun olmaniza {emeklilik} yil kaldi ")
    else:
        print("Zaten mezun oldunuz")
Mezunolmayakaçyil(2008,"Taylan")
Mezunolmayakaçyil(1998,"Doğu")
print(help(Mezunolmayakaçyil))


# list = [1,2,3,4]
# print(help(list.append))




def sayitoplama(sayi1,sayi2):
    return  sayi1 + sayi2


print(sayitoplama(9,1))
