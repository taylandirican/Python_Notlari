Günler=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
with open("C:/Users/AD/Desktop/Dersprogramı.txt","w",encoding="utf-8") as file: 

    for g in Günler:

        while True:

            try:
                a = int(input(f"{g} günü kaç bölüm istersin:"))
            except Exception as ex:
                print("Lütfen bir sayı giriniz")

            else:
                for b in range(1,a+1):
                        c = input(f"{b}. bölümde ne yapacaksin:")
                        file.write(f"{g} => {b}: {c}\n")
                if a ==0:
                        pass
                else:
                        file.write("______________________________\n")
                break



