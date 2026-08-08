# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önce işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# def hello(name):
#     print("hello",name)

# def sayGreeting():
#     print("greeting")
# hello("ali")


# hello = my_decorator(hello)
# hello() 



# sayGreeting = my_decorator(sayGreeting)
# sayGreeting()

import math
import time





def decorative(fonk):
    def wrapper(sayı):
        start = time.time()
        time.sleep(1)
        fonk(sayı)
        finish = time.time()      
        print("fonksiyon "+str(finish-start)+"saniye sürdü")
        return wrapper


usalma =  decorative()
usalma()


def usalma(a,b):
    print(math.pow(a,b))
        

def faktoriyel(num):
    start = time.time()
    time.sleep(1)
    print(math.factorial(num))
    finish = time.time()
    print("fonksiyon "+str(finish-start)+"saniye sürdü")



usalma(2,3)

faktoriyel(6)





