import os
import mainСharacter
import creatures


def start_game():
    while True:
        is_dead = False
        name = input("Как зовут тебя, герой? ")
        hero = mainСharacter.Character(name)
        while True:
            enemy = creatures.Enemy(hero)
            print(f"Появляется {enemy.name}!")
            while True:
                print(" /==============================\\")
                print(f"|{hero.name}\t |Жизнь\t{hero.health}\t\t|")
                print(f"|\t |Золото\t{hero.gold}\t|")
                print(f"|\t |Урон\t{hero.damage}\t\t|")
                print(f"|\t |Зелья\t{hero.potions}\t\t|")
                print(f"|\t |Уровень\t{hero.lvl}\t|")
                print(f"|\t |Опыт\t{hero.exp}\t\t|")
                print(f"|\t |LvlUp\t{95 + 5 * hero.lvl}\t\t|")
                print(" \\==============================/ ")
                print()
                print("Ваш враг")
                print(" /==============================\\")
                print(f"|{enemy.name}\t |Жизнь\t{enemy.health}\t\t|")
                print(f"|\t |Урон\t{enemy.damage}\t\t|")
                print(" \\==============================/ ")
                print("Attack\tPotion\tBuy")
                comand = input("Введите команду: ")
                if comand.capitalize() == "Attack":
                    hero.attack(enemy)
                elif comand.capitalize() == "Potion":
                    hero.potion()
                elif comand.capitalize() == "Buy":
                    hero.buy()
                if hero.health <= 0:
                    is_dead = True
                    os.system('cls||clear')
                    break
                if enemy.health <= 0:
                    print(enemy.name, "Побежден")
                    print("Вы нашли", enemy.gold, "монет!")
                    hero.change_gold(enemy.gold)
                    hero.add_exp(enemy.exp)
                    hero.monsters += 1
                    input("Для продолжения нажмите Enter")
                    break
                os.system('cls||clear')
            if is_dead:
                print("К сожалению, вы умерли...")
                print(f"Вы убили монстров: {hero.monsters}!")
                input("Для продолжения нажмите Enter")
                break
            os.system('cls||clear')


start_game()
