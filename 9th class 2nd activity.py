class student:
    grade = 8
    name = "Uzaer"

    def introduction(self):
        print("Hi! i am a student")

    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()