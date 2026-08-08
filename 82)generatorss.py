def cube():  
    for i in range(5):
        yield i **3   #yield değeri saklamıyor

generator = cube()
iterator = cube()

iterator = iter(generator)


for i in cube():
    print(i)


liste = (i**3 for i in range(5))
print(liste)

print(next(liste))
print(next(liste))
print(next(liste))
print(next(liste))
print(next(liste))
