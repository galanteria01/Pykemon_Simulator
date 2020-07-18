import random


class pokemon:
    def __init__(self, name, hp, breed, powers):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.breed = breed
        self.powers = powers

    def about_me(self):
        print("______________________________________")
        print("This is "+self.name+" of type "+self.breed)
        print("It has health points of "+str(self.hp))
        print("--------------------------------------")

    def take_dmg(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self,dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp