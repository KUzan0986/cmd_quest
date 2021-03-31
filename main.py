import os
import mainСharacter


def start_game():
    name = "Hero"
    hero = mainСharacter.Character(name)
    while True:
        print(" /==============================\\")
        print(f"|{hero.name}\t |Жизнь\t{hero.health}\t\t|")
        print(f"|\t |Золото\t{hero.gold}\t|")
        print(f"|\t |Урон\t{hero.damage}\t\t|")
        print(" \\==============================/ ")
        print("Health\tGold\tDamage")
        comand = input("Введите команду: ")
        if comand.capitalize() == "Health":
            change = input("На сколько меняем?")
            hero.change_health(int(change))
        elif comand.capitalize() == "Gold":
            change = input("На сколько меняем?")
            hero.change_gold(int(change))
        elif comand == "Damage":
            change = input("На сколько меняем?")
            hero.change_damage(int(change))
        os.system('cls||clear')


start_game()
