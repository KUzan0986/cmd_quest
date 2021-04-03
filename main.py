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
    print("Attack-1\tPotion-2")
    comand = input("Введите команду: ")
    if comand.capitalize() == "1":
        hero.attack(enemy)
    elif comand.capitalize() == "2":
        hero.potion()


def print_town(town, hero):
    print(f"Добро пожаловать в {town.name}!")
    print(" /==============================\\")
    print(f"|\tЛечение |{town.pay_healing} золота\t|")
    print(f"|\t УронUP |{town.pay_damage_up} золота\t|")
    print(f"|\t Зелья |{town.pay_buy_potion} золота\t|")
    print(" \\==============================/ ")
    print("Healing-1\tDamage-2\tBuy-3\tExit-0")
    comand = input("Введите команду: ")
    if comand.capitalize() == "1":
        town.healing(hero)
    elif comand.capitalize() == "2":
        town.damage_up(hero)
    elif comand.capitalize() == "3":
        town.buy_potion(hero)
    elif comand.capitalize() == "0":
        town.exit = True


def print_encounter(encounter, hero):
    if isinstance(encounter, town.Town):
        print_town(encounter, hero)
    elif isinstance(encounter, creatures.Enemy):
        print_enemy(encounter, hero)


def start_game():

    to_monster = True
    while True:
        is_dead = False
        name = input("Как зовут тебя, герой? ")
        hero = mainСharacter.Character(name)
        while True:

            if to_monster:
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
                        to_monster = True
                        os.system('cls||clear')
                        break
                if isinstance(encounter, creatures.Enemy):
                    if encounter.health <= 0:
                        print(encounter.name, "Побежден")
                        print("Вы нашли", encounter.gold, "монет!")
                        print("Вы получили", encounter.exp, "опыта!")
                        hero.change_gold(encounter.gold)
                        hero.add_exp(encounter.exp)
                        hero.monsters += 1
                        print("Бьёмся дальше или идем в город?")
                        print("Fight-1\tTown-2")
                        while True:
                            comand = input("Введите команду:")
                            if comand.capitalize() == "1":
                                to_monster = True
                                break
                            elif comand.capitalize() == "2":
                                to_monster = False
                                break
                            else:
                                print("Не знаю такую команду")
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
