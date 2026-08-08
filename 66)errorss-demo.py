liste =["1","2","5a","10b","abc"]
for l in liste:
    try:
        int(l)
    except Exception as ex:
        print("Sayisal bir değer değil",ex)
    finally:
        print("checked",l)




def checkpassword(p):
    import re
    if re.search("[iöğüç]",p):
        raise Exception("Turkce karakter girilemez")
while True:   
    x = input("bir parola giriniz")
    try:
        checkpassword(x)
    except Exception as ex:
        print(ex)
    else:
        print("Şifre kaydedildi")
        break
    finally:
        print("password checked")





a =1
def factoriel(q):
    global a
    for f in range(1,q+1):
        a = a*f
    print(a)
while True:    
    try:
        d = int(input("Bir sayi giriniz"))
    except Exception as ex:
        print("Lütfen sayi giriniz,",ex)
    else:
        factoriel(d)
        break



