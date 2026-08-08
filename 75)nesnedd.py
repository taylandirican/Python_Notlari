# def greeting(name):
#     print("helllo",name)

# greeting("Taylan")
# print(greeting)
# sayhello = greeting
# print(sayhello)
# print(greeting)


# del sayhello #sadece tanımlamayı siler, datayı  silmez
# print(greeting)
# print(sayhello)


# encapsulation
# def outer(no):
#     print("outer")
#     def inner_increment(no2):
#         print("inner")
#         return no +1
#     no2 = inner_increment(no)
#     print(no,no2)
# outer(10) # inner çalışmaz
# inner_increment(10) #Çalışmaz çünkü sadece outer içinde tanımlı

# def b(no):
#     print("g çalıştı")
#     print(no)
#     def ap(no):
#         print("a çalıştı")
#         print(no)
#     ap(0)
# b(0)
# ap(0) =>hata verir fonksiyonun içinde olduğu için


# def factoriel(number):
#     if not isinstance(number, int):
#         raise TypeError("number must be an integer")    

#     if  not number>=0:
#         print("Number must be zero or positive")

#     def inner_factoriel(number):
#         if number <= 1:
#             return 1
#         return number * inner_factoriel(number-1)
#     return inner_factoriel(number)
# try:
#     print(factoriel("a"))
# except Exception as ex:
#     print(ex)



# Defter=[]
# def kayıt(isim,soyisim):
#     a=isim+"_"+soyisim
#     Defter.append(a)
#     def yaz(isim,soyisim):
#         print("yazıldı")
#         return isim+" "+soyisim
#     return yaz(isim,soyisim)
# print(kayıt("taylan","dirican"))
# print(Defter)
