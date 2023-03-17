import random
import  classes
from battle import battleHandler
from os import system
from classes import Item, WeaponItem, PotionItem, Enemy, Location
from colorama import Fore, Back, Style

#--------------------------------------

CaseClass = ("CC_TRAINING", "CC_BATTLE", "CC_WALKING", "CC_INVENORY")
training, battle, walking, ineventory = CaseClass

CurrentCase = None

#--------------------------------------

Potions = [ PotionItem("Малое зелье здоровья", classes.potion, heal=15, manaheal=0),
            PotionItem("Среднее зелье здоровья", classes.potion, heal=30, manaheal=0)]

Weapons = [ WeaponItem("Деревянный меч", classes.weapon, damage=3, critchance=25) ]

Enemies = [ Enemy("Кряква", 2, 10, 0, classes.spawn, classes.near), 
            Enemy("Каменный паук", 2, 10, 0.2, classes.forrest, classes.near)]

Locations = [ Location("Спавн", classes.spawn, 0.15),
              Location("Лес", classes.forrest, 0.2)]

#--------------------------------------
#обработчик выборов игоком и реакции интерфейса на выбор
def caseHandler(currentcase, character, enemy):
    if currentcase == battle:
        character, enemy = battleHandler(character, enemy)

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
                        print("У тебя нет оружия\n")
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
                character.current_location = Locations[Locations.index(character.current_location) - 1]
            elif decide == 0:
                caseHandler(ineventory, character, None)
            else:
                break

def interface(currentcase):
    print()

def positionChanger(currentPos, rangeClass, stamina=100):
    if stamina > 80:
        if random(0, 3) > 0:
            print("fuck")

def decider(case, character):
    if character.current_location.locationclass == classes.spawn:
        if case < character.current_location.enemychanse:
            caseHandler(battle, character, enemyChecker(character.current_location.locationclass))
        else:
            caseHandler(walking, character, None)


def enemyChecker(current_location):
    SituableEnemies = []
    for enemy in Enemies:
        if current_location == enemy.location:
            SituableEnemies.append(classes.Enemy(enemy.name, enemy.damage, enemy.hp, enemy.armor, enemy.location, enemy.range))
    
    return random.choice(SituableEnemies)

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
        decider(random.random(), player)
        score += 1

if __name__ == "__main__":
    main()
else:
    print("Модуль имортирован")


#pyinstaller -F -i "d:/dsd/dsd.ico" engine.py