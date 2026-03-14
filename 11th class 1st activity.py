# parent class
class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # calling parent constructor
        Person.__init__(self, name, idnumber)


# creating object
a = Employee('Penguin', 20210401, 15000, "Intern")

a.display()