class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("huy", "quang")
x.printname() 

class person(Person):
    pass
x= person("huy", "quang")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.g = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.g)

x = Student("huy", "quang", 2025)
x.welcome()  


