class Hero:
    def __init__(self, name, nation, level):
        self.name = name
        self.nation = nation
        self.level = level

    def attack(self, enemy):
        if enemy.nation == "red":
            print(f"{self.name} attack {enemy.nation}")
        else:
            print("it is friend!")

    def fight_result(self, func):
        pass


ice_mage = Hero("nolan", "blue", 100)

ice_mage.attack(Hero("Vitus", "red", "90"))