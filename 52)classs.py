#class

class Person:       
    #class attributes
    address = "no information"
    #constructor (yapıcı method)    
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print("init metodu çalişti")
        #methods


#object, instance
p1 = Person(name="TAYLAN",year=2008)
p2 = Person(name="Doğu",year=2013)


p1.name = "Eray"
p1.year=1977
p1.address ="Bahadin"

#accesing object attributes
print(f"p1: name:{p1.name}, year:{p1.year}, address: {p1.address}")
print(f"p2: name:{p2.name}, year:{p2.year}, address: {p2.address}")

# print(p1)
# print(p2)

# print(type(p1))
# print(type(p2))
# print(p1==p2)



# class dergi:
#     def __init__ (self,yayin,konu,isim):
#         self.yayin = yayin
#         self.konu = konu
#         self.isim = isim


# dergi1 = dergi("Tübitak","bilim","BilimveTeknik")
# dergi2 = dergi("Cepa","Kültür","CepaDergi")




# class Araba:
#     marka ="Toyota"
#     def __init__(self,isim,yas):
#         self.isim=isim
#         self.yas=yas
#     def hareket(self):
#         print("Araba hareket ediyor")

# araba1=Araba("Maviş",12)
# print(araba1.isim)
# print(araba1.yas)
# print(araba1.marka)
# araba1.hareket()
