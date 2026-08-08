# Classların Miras alması

#Person => name, lastname , age,eat(),run(),drink()
#Student(Person),Teacher(Person)

# Animal => Dog(),Cat()

class Person():
    def __init__(self,fname,lname):
        print("Person Created")
        self.fname=fname
        self.lname=lname

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        print("Student created")
        self.number=number


p1=Person("Taylan","Dirican")
s1=Student("Doğu","Dirican",1001)


