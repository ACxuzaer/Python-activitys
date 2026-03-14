# important packages
from abc import ABC, abstractmethod
# create a base class
class Animal(ABC):

    # abstract method
    # should be implemented by all sub-classes
    def move(self):
        pass

# sub classes
class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

# Driver code [it repreasents what i do not know]
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

k = Lion()
k.move()