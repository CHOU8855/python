from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass


class Human(Animal):

    def move(self):
        print('I can walk and run')

class Snake(Animal):
    def move(self):
        print('I can slither')

class Dog(Animal):

    def move(self):
        print('I can dribble and drool')

class Lion(Animal):

    def move(self):
        print('I can roar')

class Parrot(Animal):

    def move(self):
        print('I can squwak')

class Zebra(Animal):

    def move(self):
        print('I have unique stripes and I am graceful aswell as being elegant.')

R = Human()
R.move()

K = Snake()
K.move()

L = Dog()
L.move()

R = Lion()
R.move()

P = Parrot()
P.move()

Z = Zebra()
Z.move()