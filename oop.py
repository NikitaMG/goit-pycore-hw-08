class Hero:
    def __init__(self, name, nation, level):
        self.name = name
        self.nation = nation
        self.level = level
        self.last_fight = None

    def attack(self, enemy):
        if enemy.nation == "red":
            print(f"{self.name} attack {enemy.nation}")
            self.last_fight = enemy
        else:
            print("it is friend!")
            self.last_fight = None

    def fight_result(self, func):
        if self.last_fight:
            result = func(self, self.last_fight)
            print(f"Fight result: {result}")
        else:
            print("No fight happened.")


def calculate_result(hero1, hero2):
    if hero1.level > hero2.level:
        return f"{hero1.name} wins!"
    elif hero1.level < hero2.level:
        return f"{hero2.name} wins!"
    else:
        return "It's a draw!"


ice_mage = Hero("nolan", "blue", 100)

ice_mage.attack(Hero("Vitus", "red", 90))
ice_mage.fight_result(calculate_result)
