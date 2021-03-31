class Rat:
    def __init__(self):
        self.name = "Rat"
        self.health = 15
        self.damage = 1
        self.gold = 15


    def change_gold(self, cgold=0):
        self.gold += cgold

    def change_damage(self, cdamage=0):
        self.damage += cdamage

    def change_health(self, chealth=0):
        self.health += chealth