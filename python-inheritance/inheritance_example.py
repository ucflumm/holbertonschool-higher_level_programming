#!/usr/bin/python3


class Pet:
    """Super class pet"""
    name = "" 

    def high_five(self):
        print("Gives high 5 to vs pets!")

# Class cat inherits from Pet
class Cat(Pet):
    # subclass method 
    def show_name(self):
        # using name from superclass access with self
        print("My name is ", self.name)

    def meow(self, counter):
        for i in range(counter):
            print("Meow")

# Class dog inherits from pet
class Dog(Pet):
    def show_name(self):
        print("My woof name is ", self.name)

    def bark(self, counter):
        for i in range(counter):
            print("Woof!")

main_coon = Cat()
main_coon.name = "Patches"
main_coon.high_five()
main_coon.show_name()
main_coon.meow(3)

dulux = Dog()
dulux.name = "Dulux DOGE"
dulux.high_five()
dulux.show_name()
dulux.bark(2)
