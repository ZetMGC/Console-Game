import random
import classes, inventory
from inventory import InventoryHandler
from battle import battleHandler
from os import system
from classes import Item, WeaponItem, PotionItem, Enemy, Location
from colorama import Fore, Back, Style

#--------------------------------------

CaseClass = ("CC_TRAINING", "CC_BATTLE", "CC_WALKING", "CC_INVENORY", "CC_STATS")
training, battle, walking, inventory, stats= CaseClass
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

    elif currentcase == inventory:
        InventoryHandler(character)
    elif currentcase == walking:
        while True:
            system("CLS")
            print("<------------------------------------------------------>\n")
            print("Ты находишься в локации \"", Fore.GREEN + character.current_location.name +  Style.RESET_ALL, "\".\n")
            print("<------------------------------------------------------>\n")
            print(Fore.RED + "1. ИДТИ ДАЛЬШЕ" + Style.RESET_ALL)
            print(Fore.RED + "2. ОБЫСКАТЬ ЛОКАЦИЮ" + Style.RESET_ALL)
            print(Fore.RED + "3. ВЕРНУТЬСЯ" + Style.RESET_ALL)
            print(Fore.RED + "4. ИНФОРМАЦИЯ О ПЕРСОНАЖЕ" + Style.RESET_ALL)
            print(Fore.RED + "0. ИНВЕНТАРЬ" + Style.RESET_ALL)

            decide = input()
            if decide == "1": 
                character.current_location = Locations[Locations.index(character.current_location) + 1]
            elif decide == "2":
                break
            elif decide == "3":
                character.current_location = Locations[Locations.index(character.current_location) - 1]
            elif decide == "4":
                character.info()
            elif decide == "0":
                caseHandler(inventory, character, None)
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