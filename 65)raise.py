# x = 10
# if x >5:
#     raise Exception("x 5 den büyük değer alamaz")

# def checkpassword(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("password en az 8 karakterli olmalidir")
#     elif not re.search("[a-z]", psw):
#         raise Exception("parola küçük harf içermellidir")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola büyük harf içermellidir")
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam içermellidir")  
#     elif not re.search("[_@$]", psw):
#         raise Exception("parola alpha numeric harf içermellidir")  
#     elif re.search(" ", psw):
#         raise Exception("parola boşluk içeremez")    
#     else:
#         print("Parola kaydedildi")
# password = "1234567aA5_"

# try:
#     checkpassword(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Parolaniz kaydedildi")
# finally:
#     print("validation tamamlandi")


# class Person:
#     def __init__(self,name,year):
#         if len(name)>10:
#             raise Exception("en fazla 10 karakter içermelidir")
#         else:
#             self.name=name

# p =Person("Aliiiiiiiii",1222)
        