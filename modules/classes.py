import random


class pokemon:
    def __init__(self, name, hp, breed, powers):
        self.name = name
        self.hp = hp
        self.breed = breed
        self.powers = powers

    def about_me(self):
        print("This is "+self.name+" of classsification "+self.breed)
        print("It has health points of "+str(self.hp))
        print("\n")