#error handing 

# except ZeroDivisionError:
#     print("y için 0 girilemez")
# except ValueError:
#     print("x ve y için sayisal değer girmelisiniz")
while True:
    try:
        x =int(input("x: "))
        y =int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("yanliş bilgi girdiniz",ex)
    else:
        break
    finally: # break ya da tekrar olması önemsenmez sürekli çalışır /dosya açtık ve dosyayı kapatırken bitirmek için kullanılır
        print("try except sonlandi.")
    