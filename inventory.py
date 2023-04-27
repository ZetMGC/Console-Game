from os import system
from progress.bar import FillingSquaresBar
import colorama
from colorama import Fore, Back, Style

def InventoryHandler(character):
    while True:
        system("CLS")
        print(Back.BLUE + "ИНВЕНТАРЬ\n" + Style.RESET_ALL)
        print("<------------------------------------------------------>\n")
        print(Fore.RED + "1. ЗЕЛЬЯ" + Style.RESET_ALL)
        print(Fore.RED + "2. ОРУЖИЕ" + Style.RESET_ALL)
        print(Fore.RED + "3. БРОНЯ" + Style.RESET_ALL)
        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
        decide = input()
        if decide == "1":
            if len(character.potionitem) < 1:
                while True:
                    system("CLS")
                    print("У тебя нет зелий\n")
                    print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                    decide = input()
                    if decide == "0":
                        break
                    else:
                        continue
            elif len(character.potionitem) > 0:
                while True:
                    system("CLS")
                    for potion in character.potionitem:
                        print(Fore.RED, (character.potionitem.index(potion) + 1), ". ", Style.RESET_ALL, potion.name, "\n", sep="")
                    print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                    decide = input()
                    if decide == "0":
                        break
                    elif int(decide) <= len(character.potionitem):
                        character.potionitem[int(decide)-1].info(character)
            
        elif decide == "2":
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
                        print(Fore.RED, (character.weaponitem.index(weapon) + 1), ". ", Style.RESET_ALL, weapon.name, "\n", sep="")
                    print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                    decide = input()
                    if decide == "0":
                        break
                    elif int(decide) <= len(character.weaponitem):
                        character.weaponitem[int(decide)-1].info(character)

        elif decide == "3":
            if len(character.armoritem) < 1:
                while True:
                    system("CLS")
                    print("У тебя нет брони\n")
                    print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                    decide = input()
                    if decide == "0":
                        break
                    else:
                        continue
            elif len(character.armoritem) > 0:
                while True:
                    system("CLS")
                    for armor in character.armoritem:
                        print(Fore.RED, (character.armoritem.index(armor) + 1), ". ", Style.RESET_ALL, armor.name, "\n", sep="")
                    print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                    decide = input()
                    if decide == "0":
                        break
                    
                    elif int(decide) <= len(character.armoritem):
                        character.armornitem[int(decide)-1].info(character)

        elif decide == "0":
            print("NAZAD")
            break
        else:
            continue