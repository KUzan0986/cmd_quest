import creatures

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
        self.gold = 15
        self.potions = 3

    def change_gold(self, cgold=0):
        self.gold += cgold

    def change_damage(self, cdamage=0):
        self.damage += cdamage

    def change_health(self, chealth=0):
        self.health += chealth

    def change_potions(self, cpotions=0):
        self.potions += cpotions

    def attack(self, foe):
        self.health -= foe.damage
        foe.health -= self.damage
