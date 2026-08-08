# def changeName(n):
#     n ="Taylan"
   
# name="Doğu"
# changeName(name)
# print(name)

def change(n):
    n[0] = "İstanbul"
Şehirler = ["Ankara","izmir"]

change(Şehirler)
print(Şehirler)

n = Şehirler[:]
n[0]=" İstanbul" 

change(Şehirler[:])

print(Şehirler)


# def add(a,b,c=0):
#     return sum((a,b,c))

# print(add(10,20))
# print(add(10,20,30))

# def add(*params):
#     print(params)
#     print(params[1])
#     return sum((params))

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,78,67))

# def displayUser(**params):
#     print(type(params))
#     for key,value in params.items():
#         print("{} is {}".format(key,value))
# displayUser(name ="Taylan", age="16", city="Ankara")
# displayUser(name ="Eray", age="47", city="Ankara",no="232456")
# displayUser(name ="Sati", age="16", city="Ankara",no="232456",mail="ffdfgfd" )


# def myFunc(a,b,c,*params,**args):
#     print(a)
#     print(b)
#     print(c)
#     print(params)
#     print(args)
# myFunc(2,4,665,564,654,89,237,34,key1="k",key2="w")

a = []
def list(*params):
    a.append(params)



list(1,2,3,3,4,4,3,98)
print(a)




def dictionary(**a):
    return a


print(dictionary(Marka="Tarylan", Holding="Taylan",))

