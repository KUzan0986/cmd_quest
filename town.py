import random


class Town:
    list_of_town = [
        "Emmett Village", "Idris Town",
        "Spock Farm", "Aquila City", "Nyota Town", "Teyla Farm"
    ]

    def __init__(self):
        self.name = random.choice(self.list_of_town)
        self.pay_healing = 15
        self.pay_damage_up = 3 + 3
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
