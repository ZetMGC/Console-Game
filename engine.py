from os import system
import classes
import random
from colorama import Fore, Back, Style

#--------------------------------------

BattleActions = ("BA_ATTACK", "BA_DODGE", "BA_BLOCK", "BA_HIDE")
attack, dodge, block, hide = BattleActions

CaseClass = ("CC_TRAINING", "CC_BATTLE", "CC_WALKING", "CC_INVENORY")
training, battle, walking, ineventory = CaseClass

CurrentCase = None

#--------------------------------------

Potions = [ classes.Item("Малое зелье здоровья", classes.potion, 0, 0, 0, 15, 0, 10),
            classes.Item("Среднее зелье здоровья", classes.potion, 0, 0, 0, 30, 0, 20)]

Weapons = [ classes.Item("Деревянный меч", classes.weapon, 0, 0, 3, 0, 0, 25)]

Enemies = [ classes.Enemy("Кряква", 2, 10, 0, classes.spawn), 
            classes.Enemy("Каменный паук", 2, 10, 0.2, classes.forrest)]

Locations = [ classes.Location("Спавн", classes.spawn),
              classes.Location("Лес", classes.forrest)]

#--------------------------------------

def caseHandler(currentcase, character, enemy):
    if currentcase == battle:
        while True:
            if enemy.hp > 0 and character.hp > 0:
                system('CLS')
                print(Back.RED + "БИТВА" + Style.RESET_ALL)
                print("<------------------------------------------------------>\n")

                print("Твое здоровье:", Fore.GREEN + str(character.hp) + Style.RESET_ALL, ".\nТвое оружие наносит:", Fore.GREEN + str(character.current_weapon.damage) + Style.RESET_ALL, "урона.\n")
                print("Твой противник", Fore.RED + enemy.name + Style.RESET_ALL, ", он имеет", Fore.RED + str(enemy.hp) + Style.RESET_ALL, "здоровья.\n")

                print("<------------------------------------------------------>\n")
                print(Fore.RED + "1. АТАКОВАТЬ" + Style.RESET_ALL)
                print(Fore.RED + "2. УКЛОНИТЬСЯ" + Style.RESET_ALL)
                print(Fore.RED + "3. БЛОКИРОВАТЬ" + Style.RESET_ALL)
                print(Fore.RED + "0. СБЕЖАТЬ" + Style.RESET_ALL)

                decide = int(input())
                if decide == 1:
                    battleHandler(character, enemy, attack)
                elif decide == 2:
                    battleHandler(character, enemy, dodge)
                elif decide == 3:
                    battleHandler(character, enemy, block)
                elif decide == 0:
                    battleHandler(character, enemy, hide)
                else:
                    continue

                character.hp -= enemy.damage - (enemy.damage * character.armor)
                character.hp = round(character.hp, 1)
            elif enemy.hp <= 0:
                system('CLS')
                print("ПОБЕДИЛ")
                break
            elif character.hp <= 0:
                system('CLS')
                print("ПРОИГРАЛ")
                break

    elif currentcase == ineventory:
        while True:
            system("CLS")
            print(Back.BLUE + "ИНВЕНТАРЬ\n" + Style.RESET_ALL)
            print("<------------------------------------------------------>\n")
            print(Fore.RED + "1. ЗЕЛЬЯ" + Style.RESET_ALL)
            print(Fore.RED + "2. ОРУЖИЕ" + Style.RESET_ALL)
            print(Fore.RED + "3. БРОНЯ" + Style.RESET_ALL)
            print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)

            decide = int(input())
            if decide == 1:
                if len(character.potionitem) < 1:
                    while True:
                        system("CLS")
                        print("У тебя нет зелий\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = int(input())
                        if decide == 0:
                            break
                        else:
                            continue
                elif len(character.potionitem) > 0:
                    while True:
                        system("CLS")
                        for potion in character.potionitem:
                            print(character.potionitem.index(potion) + 1, potion.name, "\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = int(input())
                        if decide == 0:
                            break
                        elif decide <= len(character.potionitem):
                            character.potionitem[decide-1].info()
                            
            elif decide == 2:
                if len(character.weaponitem) < 1:
                    while True:
                        system("CLS")
                        print("У тебя нет оjaружия\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = int(input())
                        if decide == 0:
                            break
                        else:
                            continue
                elif len(character.weaponitem) > 0:
                    while True:
                        system("CLS")
                        for weapon in character.weaponitem:
                            print(character.weaponitem.index(weapon) + 1, weapon.name, "\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = int(input())
                        if decide == 0:
                            break
                        elif decide <= len(character.weaponitem):
                            character.weaponitem[decide-1].info()
            elif decide == 3:
                if len(character.armoritem) < 1:
                    while True:
                        system("CLS")
                        print("У тебя нет брони\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = int(input())
                        if decide == 0:
                            break
                        else:
                            continue
                elif len(character.armoritem) > 0:
                    while True:
                        system("CLS")
                        for armor in character.armoritem:
                            print(character.armoritem.index(armor) + 1, armor.name, "\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = int(input())
                        if decide == 0:
                            break
                        elif decide <= len(character.armoritem):
                            character.armornitem[decide-1].info()
            elif decide == 0:
                print("NAZAD")
                break
            else:
                continue
    
    elif currentcase == walking:
        while True:
            system("CLS")
            print("<------------------------------------------------------>\n")
            print("Ты находишься в локации \"", Fore.GREEN + character.current_location.name +  Style.RESET_ALL, "\".\n")
            print("<------------------------------------------------------>\n")
            print(Fore.RED + "1. ИДТИ ДАЛЬШЕ" + Style.RESET_ALL)
            print(Fore.RED + "2. ОБЫСКАТЬ ЛОКАЦИЮ" + Style.RESET_ALL)
            print(Fore.RED + "3. ВЕРНУТЬСЯ" + Style.RESET_ALL)
            print(Fore.RED + "0. ИНВЕНТАРЬ" + Style.RESET_ALL)

            decide = int(input())
            if decide == 1: 
                character.current_location = Locations[Locations.index(character.current_location) + 1]
            elif decide == 2:
                break
            elif decide == 3:
                break
            elif decide == 0:
                caseHandler(ineventory, character, None)
            else:
                break

def interface(currentcase):
    print()

def decider(case, character):
    if character.current_location.locationclass == classes.spawn:
        if case >= 85:
            caseHandler(battle, character, enemyChecker(character.current_location.locationclass))
        else:
            caseHandler(walking, character, None)


def enemyChecker(current_location):
    SituableEnemies = []
    for enemy in Enemies:
        if current_location == enemy.location:
            SituableEnemies.append(classes.Enemy(enemy.name, enemy.damage, enemy.hp, enemy.armor, enemy.location))
    
    return random.choice(SituableEnemies)


def battleHandler(character, enemy, battleaction):
    if battleaction == attack:
        enemy.hp -= character.current_weapon.damage - (character.current_weapon.damage * enemy.armor)
        enemy.hp = round(enemy.hp, 1)
    elif battleaction == dodge:
        print("Уклонение")
    elif battleaction == block:
        print("Блок")
    elif battleaction == hide:
        print("Спрятаться")

#--------------------------------------

def main():
    score = 0

    player = classes.Person()
    player.creator()
    player.info()
    player.current_location = Locations[0]
    player.current_weapon = Weapons[0]
    player.potionitem.append(Potions[0])
    player.weaponitem.append(Weapons[0])
    while player.hp > 0:
        decider(random.randint(0, 100), player)
        score += 1

if __name__ == "__main__":
    main()
else:
    print("Модуль имортирован")


#pyinstaller -F -i "d:/dsd/dsd.ico" engine.py