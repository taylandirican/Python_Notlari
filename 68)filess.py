#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#Kulanımı: open(dosya_adi,dosya_erisme_modu)
#dosya erisme modu => dosyayı hangi amaçala açtığımğzğ belirler

#"w": (Write) yazma modu. Dosyayı konumda oluşturur
#   **Dosyayı konumda oluşturur
#   **Dosya içeriğini siler ve yeniden ekleme yapar

# file = open("newfile.txt","w")
# file = open("C:/users/AD/desktop/newfile.txt","w")

# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Taylan Dirican")
# file.close()

#"a": (Append) ekleme modu. Dosya konumda yoksa oluşturulur

# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nTaylan Dirican\n ")
# file.close()

#"x": (Create) oluşturma modu. Dosya zaten varsa hata verir,Sadece dosya oluşturur

# file = open("newfile5.txt","x",encoding="utf-8")

#"r": (Read) okuma modu. Dosya konumda yoksa hata verir


file = open("Dersprogramı.xlsx","x",encoding="utf-8")
