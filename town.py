import random


class Town:
    list_of_town = [
        "Emmett", "Idris", "Spock", "Aquila", "Nyota", "Teyla"
    ]

    def __init__(self):
        self.name = self.list_of_town[random.randint(0, len(self.list_of_town) - 1)]
        self.pay_healing = 15
        self.pay_damage_up = 20
        self.pay_buy_potion = 10
        self.exit = False

    def healing(self, hero):
        if hero.gold < self.pay_healing:
            input("Не хватает золота!")
        else:
            hero.gold -= self.pay_healing
            hero.health += 25 + hero.lvl

    def buy_potion(self, hero):
        if hero.gold < self.pay_buy_potion:
            input("Не хватает золота!")
        else:
            hero.gold -= self.pay_buy_potion
            hero.potions += 1

    def damage_up(self, hero):
        if hero.gold < self.pay_damage_up:
            input("Не хватает золота!")
        else:
            hero.gold -= self.pay_damage_up
            hero.damage += 14 + hero.lvl
