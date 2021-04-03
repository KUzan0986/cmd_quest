import creatures

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
        self.gold = 15
        self.potions = 3
        self.exp = 0
        self.lvl = 1
        self.monsters = 0

    def change_gold(self, cgold=0):
        self.gold += cgold

    def change_damage(self, cdamage=0):
        self.damage += cdamage

    def change_health(self, chealth=0):
        self.health += chealth

    def change_potions(self, cpotions=0):
        self.potions += cpotions

    def attack(self, foe):
        foe.health -= self.damage
        if foe.health > 0:
            foe.attack(self)

    def potion(self):
        if self.potions == 0:
            print("У тебя нет зелий")
        else:
            self.health += 19 + 5 * self.lvl
            self.potions -= 1

    def add_lvl(self):
        self.health += 25 + self.lvl * 10
        self.damage += 5 + self.lvl * 5
        self.lvl += 1

    def add_exp(self, exp=0):
        if self.exp+exp >= 95 + 5 * self.lvl:
            self.exp = (self.exp + exp) - (95 + 5 * self.lvl)
            self.add_lvl()
        else:
            self.exp += exp
