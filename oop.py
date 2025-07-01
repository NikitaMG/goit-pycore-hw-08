import random


class Hero:
    def __init__(self, name, nation, level, power):
        self.name = name
        self.nation = nation
        self.level = level
        self.attacking = round(power + (level * 0.1),1)
        self.power = power
        self.health = power * level
        self.last_fight = None

    def attack(self, enemy):
        if enemy.nation == "red":
            print(enemy)
            print(f"{self.name} level: {self.level} attack {enemy.nation}")
            self.last_fight = enemy
        elif enemy.level >= 90:
            print(enemy, "ELITE!!")
            print(f"{self.name} level: {self.level} attack {enemy.nation}")
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

    def __str__(self):
        return f"{self.name} (nation: {self.nation}, Level: {self.level})"


class Enemy(Hero):
    def __init__(self, name, nation, level, power):
        super().__init__(name, nation, level,power)

    def drop_loot(self):
        drop = ["sword", "shield", "poison", "boots", "Nothing"]
        return random.choice(drop)

    def unique_drop(self):
        udrop = ["Nothing", "Nothing", "Nothing", "Golden apple"]
        return random.choice(udrop)


def calculate_result(hero1, enemy):
    if hero1.level > enemy.level:
        if enemy.level >= 90:
            return (f"{hero1.name} wins \n"
                    f"You have received {enemy.unique_drop()}")
        else:
            return (f"{hero1.name} wins \n"
                    f"You have received {enemy.drop_loot()}")
    elif hero1.level < enemy.level:
        return f"{hero1.namel} lost!! to {enemy.nation} {enemy.name}"
    else:
        return "draw!"


color = ["red", "blue", "green", "white"]

ice_mage = Hero("nolan", "blue",random.randint(50,100),random.randint(1,10))
other_mage = Enemy("Warrior", random.choice(color), random.randint(60, 100), random.randint(1,10))

ice_mage.attack(other_mage)
ice_mage.fight_result(calculate_result)
