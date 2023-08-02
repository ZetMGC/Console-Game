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
        try:
            decide = int(decide)
            if decide == 1:
                if len(character.potionitem) < 1:
                    while True:
                        system("CLS")
                        print("У тебя нет зелий\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        decide = input()
                        try:
                            decide = int(decide)
                            if decide == 0:
                                break
                        except ValueError:
                            continue
                elif len(character.potionitem) > 0:
                    while True:
                        system("CLS")
                        i = 0
                        while i < len(character.potionitem):
                            print(Fore.RED, (i + 1), ". ", Style.RESET_ALL, character.potionitem[i].name, "\n", sep="")
                            i += 1
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        try:
                            decide = int(input())
                            if decide == 0:
                                break
                            elif decide <= len(character.potionitem):
                                character.potionitem[decide-1].info(character)
                        except ValueError:
                            continue
                
            elif decide == 2:
                if len(character.weaponitem) < 1:
                    while True:
                        system("CLS")
                        print("У тебя нет оружия\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        try:
                            decide = int(input())
                            if decide == 0:
                                break
                        except ValueError:
                            continue
                elif len(character.weaponitem) > 0:
                    while True:
                        system("CLS")
                        i = 0
                        while i < len(character.weaponitem):
                            print(Fore.RED, (i + 1), ". ", Style.RESET_ALL, character.weaponitem[i].name, "\n", sep="")
                            i += 1
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        try:
                            decide = int(input())
                            if decide == 0:
                                break
                            elif decide <= len(character.weaponitem):
                                character.weaponitem[decide-1].info(character)
                        except ValueError:
                            continue

            elif decide == 3:
                if len(character.armoritem) < 1:
                    while True:
                        system("CLS")
                        print("У тебя нет брони\n")
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        try:
                            decide = int(input())
                            if decide == 0:
                                break
                        except ValueError:
                            continue
                elif len(character.armoritem) > 0:
                    while True:
                        system("CLS")
                        i = 0
                        while i < len(character.armoritem):
                            print(Fore.RED, (i + 1), ". ", Style.RESET_ALL, character.armoritem[i].name, "\n", sep="")
                            i += 1
                        print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
                        try:
                            decide = int(input())
                            if decide == 0:
                                break
                            elif decide <= len(character.armoritem):
                                character.armornitem[decide-1].info(character)
                        except ValueError:
                            continue
            elif decide == 0:
                break
        except ValueError:
            continue