fruits = {"orange", "apple", "banana"}
print(fruits)

# print(fruits[0]) # indekslenemez

# for x in fruits:
#     print(x)

fruits.add("cherry")
print(fruits)


fruits.update(["mango", "grape"])

print(fruits)

fruits.update(["apple"]) # setslere aynı elemanı birden fazla kez yazamazsın 
print(fruits)

myLİST = [1,2,3,4,5,6,7,7,5,3,6,2,4]
print(myLİST)
print(set(myLİST)) # bir listeyi setse dönüştürürken tekrarlanan elemanlar sadece bir kere yazılır

fruits.remove("mango")
fruits.discard("apple")
print(fruits)

fruits.pop() # sadece setslerde rastgele elemanı siler
print(fruits)

fruits.clear()
print(fruits)
