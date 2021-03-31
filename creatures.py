import random


def set_damage(name, lvl):
    if name in ["Rat"]:
        damage = random.randint(1, 2) * lvl
    elif name in ["Goblin"]:
        damage = random.randint(5, 10) * lvl
    elif name in ["Dragon"]:
        damage = random.randint(15, 25) * lvl
    return damage


def set_health(name, lvl):
    if name in ["Rat"]:
        health = random.randint(10, 15)*lvl
    elif name in ["Goblin"]:
        health = random.randint(20, 30)*lvl
    elif name in ["Dragon"]:
        health = random.randint(45, 60)*lvl
    return health


def set_gold(name, lvl):
    if name in ["Rat"]:
        gold = random.randint(1, 5) * lvl
    elif name in ["Goblin"]:
        gold = random.randint(7, 12) * lvl
    elif name in ["Dragon"]:
        gold = random.randint(20, 50) * lvl
    return gold


def set_exp(name, lvl):
    if name in ["Rat"]:
        exp = random.randint(5, 10) * lvl
    elif name in ["Goblin"]:
        exp = random.randint(15, 20) * lvl
    elif name in ["Dragon"]:
        exp = random.randint(30, 50) * lvl
    return exp


class Enemy:
    list_of_enemyes = [
        "Rat", "Rat", "Rat", "Goblin", "Goblin", "Dragon"
    ]

    import random
    # list_of_enemyes = [
    #         "Rat", "Goblin", "Dragon"
    #     ]
    #
    #
    # print(list_of_enemyes[random.randint(0, 2)])

    def __init__(self, hero):
        self.name = self.list_of_enemyes[random.randint(0, len(self.list_of_enemyes)-1)]
        self.health = set_health(self.name, hero.lvl)
        self.damage = set_damage(self.name, hero.lvl)
        self.gold = set_gold(self.name, hero.lvl)
        self.exp = set_exp(self.name, hero.lvl)
