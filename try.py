import random

multi_hp = 20
multi_dex = 10
multi_mana = 5


class Character:
    def __init__(self, name, strength, dex, intel):
        self.name = name
        self.strength = strength
        self.dex = dex
        self.intel = intel
        self.health = strength * multi_hp
        self.stamina = dex * multi_dex
        self.mana = intel * multi_mana

    @classmethod
    def create_Character(cls, name):
        return cls(name, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

    @staticmethod
    def calculate_damage(strength):
        damage = strength * random.randint(1, 5)
        return damage

    def bstats(self):
        return ('{} \n'
                'strength: {},dex: {},intel: {} \n'
                'HP: {} \n'
                'Stamina: {} \n'
                'Mana: {}').format(blue.name, blue.strength, blue.dex, blue.intel, blue.health, blue.stamina, blue.mana)


class Enemy(Character):
    def __init__(self, name, strength, dex, intel, drop=None):
        super().__init__(name, strength, dex, intel)
        self.drop = drop if drop is not None else []

    @classmethod
    def create_enemy(cls, name):
        return cls(name, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
                   drop=["posion", "sword", "blood"])

    def rstats(self):
        return ('{} \n '
                'strength: {},dex: {},intel: {} \n '
                'HP: {} \n'
                'Stamina: {} \n'
                'Mana: {}'
                ).format(red.name, red.strength, red.dex, red.intel, red.health, red.stamina, red.mana)

    def chose_drop(self):
        loot = random.choice(self.drop)
        return loot


blue = Character.create_Character("Nikita")
red = Enemy.create_enemy("Enemy")
print(blue.bstats())
print("------------------")
print(red.rstats())
print("-- FIGHT--")


def fight():
    while blue.health > 0 and red.health > 0:
        blue_damage = Character.calculate_damage(blue.strength)
        red.health -= blue_damage
        print(f"Enemy get {blue_damage} damage, {red.health} HP left \n"
              f"----------")
        red_damage = Enemy.calculate_damage(red.strength)
        blue.health -= red_damage
        print(f"Warrior get {red_damage} damage, {blue.health} HP left \n"
              f"----------")
    if blue.health <= 0:
        print("Red WON!")
    else:
        print("Blue WON!", "You get: ", red.chose_drop())


fight()


# make damage depends on stamina
# divide class (warrior/mage...)
# add spells