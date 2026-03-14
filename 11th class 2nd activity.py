class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __inint__(self, fname, lname, year):
        super().__inint__(fname, lname)
        self.graduationyear = year

x = Student("Alex", "Mac Allester", 2015)
x.printname()
print(x.graduationyear)