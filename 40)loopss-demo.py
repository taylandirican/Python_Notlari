import random
sayi = random.randint(1,10)
  

can = int(input("Kaç can istersiniz: "))
hak = can
sayaç = 0
while hak >0:
    hak -= 1
    sayaç += 1
    tahmin = int(input("tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler sayiyi {sayaç}. denemede bildiniz, puaniniz:{100 - (100/can)*(sayaç-1)}")
        break
    elif sayi > tahmin:
        print(f"Yukari ({hak} hakkin kaldi)")
    elif sayi < tahmin:
        print(f"Aşaği ({hak} hakkin kaldi)")
    if hak == 0:    
        print(f"Bilemediniz, tutulan sayi: {sayi}")























