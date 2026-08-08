#*****key - value*****#

#41 => Kocaeli,  34 => İstanbul

# sehirler = ["İstanbul", "Kocaeli"]
# plakalar = [34, 41]
# print(plakalar[sehirler.index("İstanbul")])
# print(sehirler[plakalar.index(34)])


#print(plakalar["kocaeli"]) => 41
#print(plakalar["istanbul"]) => 34

# plakalar = { "Kocaeli" : 41, 'İstanbul' : 34}

# print(plakalar["Kocaeli"])
# print(plakalar["İstanbul"])

# plakalar["Ankara"] = 6
# print(plakalar)
# print(plakalar["Ankara"])


# plakalar["Kocaeli"] = "new value"
# print(plakalar)




users = {
    "TaylanDirican" : {
        "Yas": 15,
        "Hobby" : "Guitar and Code", 
        "Address" : "Ankara",
        "Roles" : ["Admin","User"]
    },
    "Mavi" : {
        "Yas": 15,
        "Hobby" : "Bowling", 
        "Address" : "Ankara",
        "Roles" : ["User"]
    }
}
print(users["TaylanDirican"])
print(users["Mavi"])

print(users["Mavi"]["Yas"])
print(users["Mavi"]["Hobby"])
print(users["Mavi"]["Address"])
print(users["Mavi"]["Roles"][0])

print(users["TaylanDirican"]["Yas"])
print(users["TaylanDirican"]["Hobby"])
print(users["TaylanDirican"]["Address"])
print(users["TaylanDirican"]["Roles"][0])
