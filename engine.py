import random
import classes, inventory
from inventory import InventoryHandler
from battle import battleHandler
from os import system
from classes import Item, WeaponItem, PotionItem, Enemy, Location
from colorama import Fore, Back, Style

#--------------------------------------
""
CaseClass = ("CC_TRAINING", "CC_BATTLE", "CC_WALKING", "CC_INVENORY", "CC_STATS", "CC_SEARCH")
training, battle, walking, inventory, stats, search= CaseClass
CurrentCase = None

#--------------------------------------

Potions = [ PotionItem("Малое зелье здоровья", classes.potion, heal=15, manaheal=0),
            PotionItem("Среднее зелье здоровья", classes.potion, heal=30, manaheal=0)]

Weapons = [ WeaponItem("Деревянный меч", classes.weapon, damage=3, critchance=25), 
            WeaponItem("Затупленный железный меч", classes.weapon, damage=10, critchance=15)]

Enemies = [ Enemy("Кряква", 2, 10, 0, classes.spawn, classes.near), 
            Enemy("Каменный паук", 2, 10, 0.2, classes.forrest, classes.near)]

Locations = [ Location("Спавн", classes.spawn, 0.15),
              Location("Лес", classes.forrest, 0.2),
              Location("Тропинка в лесу", classes.forrest, 0.10)]

#--------------------------------------
#функция, наполняющая лутом локации игры
def locationInit(character):
    if character.current_location.locationclass == classes.spawn:
        character.current_location.ordinary.append(Potions[0])

def pickUp(character, storage):
    while True:
        system("CLS")
        print("<------------------------------------------------------>\n")
        print("Введи номер предмета, который хочешь подобрать\n")
        if len(storage) > 0:
            i = 0
            while i < len(storage):
                print(Fore.RED, i + 1, ". ", Style.RESET_ALL, storage[i].name, "\n", sep="")
                i += 1
        else:
            break
                
        print("<------------------------------------------------------>\n")
        print(Fore.RED + "0. ОТМЕНА" + Style.RESET_ALL)

        decide = input()
        try: 
            decide = int(decide)
            if decide > 0 and decide <= len(storage):
                if storage[decide-1].itemclass == classes.potion:
                    character.potionitem.append(storage[decide-1])
                    storage.pop(decide-1)
                elif storage[decide-1].itemclass == classes.weapon:
                    character.weaponitem.append(storage[decide-1])
                    storage.pop(decide-1)
                elif storage[decide-1].itemclass == classes.armor:
                    character.armoritem.append(storage[decide-1])
                    storage.pop(decide-1)
            elif decide == 0:
                break
        except ValueError:
            continue
        
#обработчик выборов игоком и реакции интерфейса на выбор
def caseHandler(currentcase, character, enemy):
    if currentcase == battle:
        character, enemy = battleHandler(character, enemy)

    elif currentcase == inventory:
        InventoryHandler(character)
    
    #если игрок решил обыскать
    elif currentcase == search:
        while True:
            system("CLS")
            print("<------------------------------------------------------>\n")
            if len(character.current_location.ground) == 0:
                print("На земле пусто.\n")
            else:
                print("На земле лежит:\n")
                i = 0
                while i < len(character.current_location.ground):
                    print(Fore.RED, i + 1, ". ", Style.RESET_ALL, character.current_location.ground[i].name, "\n", sep="")
                    i += 1
                    
            print("<------------------------------------------------------>\n")
            print(Fore.RED + "1. ОБЫСКАТЬ ЛОКАЦИЮ" + Style.RESET_ALL)
            print(Fore.RED + "2. ПОДОБРАТЬ ПРЕДМЕТ" + Style.RESET_ALL)
            print(Fore.RED + "0. ЗАКОНЧИТЬ ОБЫСК" + Style.RESET_ALL)

            decide = input()
            if decide == "1": 
                character.current_location.DropDecider(random.random())
            elif decide == "2":
                pickUp(character, character.current_location.ground)
            elif decide == "0":
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
            print(Fore.RED + "4. ИНФОРМАЦИЯ О ПЕРСОНАЖЕ" + Style.RESET_ALL)
            print(Fore.RED + "0. ИНВЕНТАРЬ" + Style.RESET_ALL)

            decide = input()
            if decide == "1": 
                character.current_location = Locations[Locations.index(character.current_location) + 1]
            elif decide == "2":
                caseHandler(search, character, None)
            elif decide == "3":
                character.current_location = Locations[Locations.index(character.current_location) - 1]
            elif decide == "4":
                character.info()
            elif decide == "0":
                caseHandler(inventory, character, None)
            else:
                break

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
    locationInit(player)
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