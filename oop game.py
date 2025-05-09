# make damage depends on stamina
# divide class (warrior/mage...)
# add spells

import random
import math
hp_multi = 3
stamina_multi = 2
mana_multi = 5


class Character:
    def __init__(self, name, strength, dex, intel, level):
        self.name = name
        self.strength = strength
        self.dex = dex
        self.intel = intel
        self.level = level


    @classmethod
    def create_char(cls):

        start = input("chose your class: Warrior, Archer, Mage: ")
        nam = input("chose a name: ")

        if start == "Warrior":
            strength = random.randint(5, 15)
            dex = random.randint(3, 8)
            intel = random.randint(1, 5)
            return Warrior(nam, strength, dex, intel,1)
        elif start == "Archer":
            strength = random.randint(3, 10)
            dex = random.randint(5, 15)
            intel = random.randint(2, 5)
            return Archer(nam, strength, dex, intel,1)
        elif start == "Mage":
            strength = random.randint(3, 8)
            dex = random.randint(2, 10)
            intel = random.randint(5, 15)
            return Mage(nam, strength, dex, intel,1)
        else:
            print("incorrect class!")
            return None


class Warrior(Character):
    def __init__(self, name, strength, dex, intel, level):
        super().__init__(name, strength, dex, intel, level)
        self.health = strength * level * (hp_multi ** 1.8)
        self.stamina = dex * level * stamina_multi
        self.mana = intel * level * mana_multi

    def __str__(self):
        return f"{self.name} the Warrior: HP={self.health:.1f}, Stamina={self.stamina}, Mana={self.mana}"


class Archer(Character):
    def __init__(self, name, strength, dex, intel, level):
        super().__init__(name, strength, dex, intel, level)
        self.health = strength * level * hp_multi
        self.stamina = dex * level * (stamina_multi ** 2)
        self.mana = intel * level * mana_multi

    def __str__(self):
        return f"{self.name} the Archer: HP={self.health:.1f}, Stamina={self.stamina:.1f}, Mana={self.mana}"


class Mage(Character):
    def __init__(self, name, strength, dex, intel, level):
        super().__init__(name, strength, dex, intel, level)
        self.health = strength * level * hp_multi
        self.stamina = dex * level * stamina_multi
        self.mana = intel * level * (mana_multi ** 1.2)

    def __str__(self):
        return f"{self.name} the Mage: HP={self.health:.1f}, Stamina={self.stamina}, Mana={self.mana:.1f}"


character = Character.create_char()

if character:
    print(character)
