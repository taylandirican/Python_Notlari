# def square(num):
#     return num**2
# result = square(54)
# print(result)


# numbers = [1,4,5,6,8,9,56]

# print(list(map(square,numbers)))    #list olmazsa adres verir

# for a in map(square,numbers):
#     print(a)

# print(list(map(lambda n:n**4,numbers)))       # lambda = tek seferlik fonksiyon

# b = lambda j:  j**3
# print(list(map(b,numbers)))

# print(b(8))








# c =[1,3,63454,65,678678,56,54,5678,8,67,554,34,5,7,85687,878,7]
# def check(num): return num%2==0

# print(list(map(check,c)))    #map int ifadeyi burada bool a dönüştürür.
# print(list(filter(check,c)))    #filter doğru olan elemanları bulur

# print(list(filter(lambda n : n%4==0,c)))


# d =[7]
# a = lambda a : a/2
# print(list(map(a,d)))


# print(list(map(check,d)))
# print(list(filter(check,d)))




# taylan = lambda c:c/7
# print(list(map(taylan,d)))

