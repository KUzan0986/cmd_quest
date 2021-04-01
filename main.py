import os
import mainСharacter
import creatures
import random
import town


def print_hero(hero):
    print(" /==============================\\")
    print(f"|{hero.name}\t |Жизнь\t{hero.health}\t\t|")
    print(f"|\t |Золото\t{hero.gold}\t|")
    print(f"|\t |Урон\t{hero.damage}\t\t|")
    print(f"|\t |Зелья\t{hero.potions}\t\t|")
    print(f"|\t |Уровень\t{hero.lvl}\t|")
    print(f"|\t |Опыт\t{hero.exp}\t\t|")
    print(f"|\t |LvlUp\t{95 + 5 * hero.lvl}\t\t|")
    print(" \\==============================/ ")


def print_enemy(enemy, hero):
    print("Ваш враг")
    print(" /==============================\\")
    print(f"|{enemy.name}\t |Жизнь\t{enemy.health}\t\t|")
    print(f"|\t |Урон\t{enemy.damage}\t\t|")
    print(" \\==============================/ ")
    print("Attack\tPotion")
    comand = input("Введите команду: ")
    if comand.capitalize() == "Attack":
        hero.attack(enemy)
    elif comand.capitalize() == "Potion":
        hero.potion()


def print_town(town, hero):
    print(f"Добро пожаловать в {town.name}!")
    print(" /==============================\\")
    print(f"|\tЛечение |{town.pay_healing} золота\t|")
    print(f"|\t УронUP |{town.pay_damage_up} золота\t|")
    print(f"|\t Зелья |{town.pay_buy_potion} золота\t|")
    print(" \\==============================/ ")
    print("Healing\tDamage\tBuy\tExit")
    comand = input("Введите команду: ")
    if comand.capitalize() == "Healing":
        town.healing(hero)
    elif comand.capitalize() == "Damage":
        town.damage_up(hero)
    elif comand.capitalize() == "Buy":
        town.buy_potion(hero)
    elif comand.capitalize() == "Exit":
        town.exit = True


def print_encounter(encounter, hero):
    if isinstance(encounter, town.Town):
        print_town(encounter, hero)
    elif isinstance(encounter, creatures.Enemy):
        print_enemy(encounter, hero)


def start_game():
    while True:
        is_dead = False
        name = input("Как зовут тебя, герой? ")
        hero = mainСharacter.Character(name)
        while True:
            if random.randint(0, 10) in range(0, 8):
                encounter = creatures.Enemy(hero)
                print(f"Появляется {encounter.name}!")
            else:
                encounter = town.Town()
                print(f"Добро пожаловать в город {encounter.name}!")
            while True:
                print_hero(hero)
                print()
                print_encounter(encounter, hero)
                if hero.health <= 0:
                    is_dead = True
                    os.system('cls||clear')
                    break
                if isinstance(encounter, town.Town):
                    if encounter.exit:
                        input("Мы будем рады вас ждать снова!")
                        os.system('cls||clear')
                        break
                if isinstance(encounter, creatures.Enemy):
                    if encounter.health <= 0:
                        print(encounter.name, "Побежден")
                        print("Вы нашли", encounter.gold, "монет!")
                        hero.change_gold(encounter.gold)
                        hero.add_exp(encounter.exp)
                        hero.monsters += 1
                        input("Для продолжения нажмите Enter")
                        os.system('cls||clear')
                        break
                os.system('cls||clear')
            if is_dead:
                print("К сожалению, вы умерли...")
                print(f"Вы убили монстров: {hero.monsters}!")
                input("Для продолжения нажмите Enter")
                os.system('cls||clear')
                break
            os.system('cls||clear')


start_game()
