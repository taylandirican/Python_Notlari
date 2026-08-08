def usalma(no):
    def inner(power):
        return no**power
    return inner


two = usalma(2)
print (two(6))

three = usalma(3)
print (three(4))


def kat_al(sayı):
    def kat(sayı1):
        return sayı*sayı1
    return kat

a =kat_al(2)
print(a(4))


# def yetki_sorgula(page):
#     def inner(role):
#         if role =="Admin":
#             return f"{role} rolü {page} sayfasına ulaşabilir."
#         else:
#             return f"{role} rolü {page} sayfasına ulaşamaz."
#     return inner
# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))




# def islem(islemadi):
#     def toplama(*args):
#         toplam=0
#         for i in args:
#             toplam+=i
#         return toplam
#     def çapma(*args):
#         çarpım=1
#         for i in args:
#             çarpım*=i
#         return çarpım
#     if islemadi =="toplama":
#         return toplama
#     elif islemadi =="çarpma":
#         return çapma
    
# a =islem("çarpma")
# print(a(4,8,9,78,51,94,125,8784))





