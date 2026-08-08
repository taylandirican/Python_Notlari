class Person:
    def __init__(self,name,year):
        self.name=name
        self.year=year

    #instance methods
    def intro(self):
        print("Hello There") 

    def calculateAge(self):
        return 2024-(self.year)



p1=Person("Taylan",2008)

p1.intro()
print(p1.calculateAge())

