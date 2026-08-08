# # global scope
# x = "Global x"

# def fu():
#     #local scope
#     x = "Local x"
#     print(x)
# fu()
# print(x)


# n ="Taylan"
# def change(newname):
#     n = newname
#     print(n)
# change("Doğu")
# print(n)



# a = "Gs"
# def g():
#     a ="İcardi"
#     print(a)
#     def hello():
#         a ="Muslera"
#         print("Hello "+a)

#     hello()
# g()


# x =50
# def t(x):
#     print(f"x : {x}")

#     x  =100
#     print(f"changed x to {x}")

# t(7)
# print(x)

# x =50
# def t():
#     global x     #fonksiyon içindeki değişikliği dışarı verir
#     print(f"x : {x}")

#     x  =100
#     print(f"changed x to {x}")

# t()
# print(x)