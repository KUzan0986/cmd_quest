import os
import mainСharacter
import creatures


def start_game():
    name = input("Как зовут тебя, герой? ")
    hero = mainСharacter.Character(name)
    while True:
        enemy = creatures.Rat()
        print(f"Появляется {enemy.name}!")
        while True:
            print(" /==============================\\")
            print(f"|{hero.name}\t |Жизнь\t{hero.health}\t\t|")
            print(f"|\t |Золото\t{hero.gold}\t|")
            print(f"|\t |Урон\t{hero.damage}\t\t|")
            print(f"|\t |Зелья\t{hero.potions}\t\t|")
            print(f"|\t |Уровень\t{hero.lvl}\t\t|")
            print(f"|\t |Опыт\t{hero.exp}\t\t|")
            print(" \\==============================/ ")
            print()
            print("Ваш враг")
            print(" /==============================\\")
            print(f"|{enemy.name}\t |Жизнь\t{enemy.health}\t\t|")
            print(f"|\t |Золото\t{enemy.gold}\t|")
            print(f"|\t |Урон\t{enemy.damage}\t\t|")
            print(" \\==============================/ ")
            print("Attack\tPotion")
            comand = input("Введите команду: ")
            if comand.capitalize() == "Attack":
                hero.attack(enemy)
            elif comand.capitalize() == "Potion":
                hero.potion()
            if enemy.health <= 0:
                break
            os.system('cls||clear')
        print(enemy.name, "Побежден")
        print("Вы нашли", enemy.gold, "монет!")
        hero.change_gold(enemy.gold)
        hero.add_exp(enemy.exp)
        input("Для продолжения нажмите Enter")
        os.system('cls||clear')


start_game()
