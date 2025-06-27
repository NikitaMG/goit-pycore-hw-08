import random


class Hero:
    def __init__(self, name, nation, level):
        self.name = name
        self.nation = nation
        self.level = level
        self.last_fight = None


loot = ["sword", "shield", "heal", "armour"]



    def __str__(self):
        return f"{self.name} (nation: {self.nation}, Level: {self.level})"

    def attack(self, enemy):
        if enemy.nation == "red":
            print(enemy)
            print(f"{self.name} attack {enemy.nation}")
            self.last_fight = enemy
        else:
            print(enemy)
            print("it is friend!")
            self.last_fight = None


def fight_result(self, func):
    if self.last_fight:
        result = func(self, self.last_fight)
        print(f"Fight result: {result}")
    else:
        print("No fight happened.")


class Enemy(Hero):
    def __init__(self, name, nation, level, drop):
        super().__init__(name, nation, level)
        self.drop = drop

    def Drop_chance(self):
        pass


def calculate_result(hero1, enemy):
    if hero1.level > enemy.level:
        return f"{hero1.name} wins!"
    elif hero1.level < enemy.level:
        return f"{enemy.name} wins!"
    else:
        return "It's a draw!"


color = ["red", "blue", "green", "white"]

ice_mage = Hero("nolan", "blue", 100)
other_mage = Hero("Warrior", random.choice(color), random.randint(60, 100))

ice_mage.attack(other_mage)
ice_mage.fight_result(calculate_result)
