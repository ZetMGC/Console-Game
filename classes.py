from os import system
from types import FrameType
import colorama
from colorama import Fore, Back, Style

#--------------------------------------

PersonClass = ("PC_MAGICIAN", "PC_WARRIOR", "PC_ARCHER")
magician, warrior, archer = PersonClass

CharacterBonus = ("CB_STUN", "CB_BLEEDING", "CB_POISONING", "CB_REGEN", "CB_GAIN", "CB_WEAKNESS") # Оглушение, кровотечение, отравление, регенерация, усиление, слабость
stun, bleeding, poisoning, regen, gain, weakness = CharacterBonus

RangeClass = ("RC_NEAR", "RC_AVERAGE", "RC_FAR")
near, average, far = RangeClass

ItemClass = ("IC_POTION","IC_UNKNOWNPOTION", "IC_WEAPON", "IC_ARMOR", "IC_ACCESSORY")
potion, unknownpotion, weapon, armor, acc = ItemClass

LocationClass = ("LC_FORREST", "LC_SPAWN")
forrest, spawn = LocationClass

#--------------------------------------

class Person:
    Inventory = ([], [], [])
    potionitem, weaponitem, armoritem = Inventory

    def __init__(self):
        self.name = None
        self.sex = None
        self.pclass = None
        self.hp = None
        self.hpmax = None
        self.bonus = None

        self.armor = None
        self.arrows = None
        self.mana = None
        self.stamina = None

        self.current_weapon = None
        self.current_armor = None
        self.current_location = None

        colorama.init()

    def info(self):
        while True:
            system('CLS')
            print("<------------------------------------------------------>\n")

            print("Твое имя: ", Fore.RED + self.name, "\n" + Style.RESET_ALL)
            print("У тебя", Fore.GREEN + str(self.hp) + Style.RESET_ALL, "здоровья\n")

            if self.sex == True:
                print("Твой пол мужской\n")
            else:
                print("Твой пол женский\n")
            
            if self.pclass == magician:
                print("Ты маг\n")
            elif self.pclass == warrior:
                print("Ты воин\n")
            elif self.pclass == archer:
                print("Ты лучник\n")

            print("<------------------------------------------------------>")
            print(Fore.RED + "0. ПРОДОЛЖИТЬ" + Style.RESET_ALL)
            decide = int(input())
            if decide == 0:
                break
            else:
                continue

    def creator(self):
        self.name = input("Введите имя персонажа: ")
        system('CLS')

        while True:
            print("Введите", Fore.BLUE + "\"1\"", Style.RESET_ALL + ", чтобы выбрать мужской пол.\nВведите", Fore.BLUE + "\"2\"", Style.RESET_ALL + ", чтобы выбрать женский пол.\n")
            sex = int(input())
            system('CLS')
            if sex == 1:
                self.sex = True
                break
            elif sex == 2:
                self.sex = False 
                break
            else:
                print(Back.RED + "Вы выбрали неверное значение." + Style.RESET_ALL)
                continue     

        while True:
            print("Введите", Fore.BLUE + "\"1\"", Style.RESET_ALL + ", чтобы выбрать класс \"Воин\".\nВведите", Fore.BLUE + "\"2\"", Style.RESET_ALL + ", чтобы выбрать класс \"Маг\".\nВведите", Fore.BLUE + "\"3\"", Style.RESET_ALL + ", чтобы выбрать класс \"Лучник\".\n")
            pclass = int(input())
            system('CLS')
            if pclass == 1:
                self.pclass = warrior
                self.hpmax = 125
                self.hp = self.hpmax
                self.armor = 0.45
                self.stamina = 100
                break
            elif pclass == 2:
                self.pclass = magician
                self.hpmax = 75
                self.hp = self.hpmax
                self.armor = 0.15
                self.stamina = 100
                break
            elif pclass == 3:
                self.pclass = archer
                self.hpmax = 100
                self.hp = self.hpmax
                self.armor = 0.30
                self.stamina = 100
                break
            else:
                print(Back.RED + "Вы выбрали неверное значение." + Style.RESET_ALL)

#--------------------------------------

class Item:
    def __init__(self, name, itemclass, armor, hp, damage, heal, manaheal, weight, critdamage):
        self.name = name
        self.itemclass = itemclass
        self.armor = armor
        self.hp = hp
        self.damage = damage
        self.heal = heal 
        self.manaheal = manaheal  
        self.weight = weight
        

    def info(self):
        while True:
            system('CLS')
            print("<------------------------------------------------------>\n")

            if self.itemclass == potion:
                print("Это", Fore.BLUE + self.name + Style.RESET_ALL, ".\n")
                print("Оно восстанавливает:", Fore.GREEN + str(self.heal) + Style.RESET_ALL, "здоровья и", Fore.GREEN + str(self.manaheal) + Style.RESET_ALL, "маны.\n")
                print("Вес предмета:", Fore.GREEN + str(self.weight) + Style.RESET_ALL, ".\n")
            elif self.itemclass == weapon:
                print("Это", Fore.BLUE + self.name + Style.RESET_ALL, ".\n")
                print("Наносит:", Fore.GREEN + str(self.damage) + Style.RESET_ALL, "урона.\n")
                print("Вес предмета:", Fore.GREEN + str(self.weight) + Style.RESET_ALL, ".\n")
            elif self.itemclass == armor:
                print("Это", Fore.BLUE + self.name + Style.RESET_ALL, ".\n")
                print("Она защищает от", Fore.GREEN + str(self.armor) + Style.RESET_ALL, "% получаемого урона.\n")
                print("Вес предмета:", Fore.GREEN + str(self.weight) + Style.RESET_ALL, ".\n")

            print("<------------------------------------------------------>")

            print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)
            decide = int(input())
            if decide == 0:
                break
            else:
                continue

#--------------------------------------

class Enemy:
    def __init__(self, name, damage, hp, armor, location, range):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.armor = armor
        self.location = location
        self.range = range

class Location:
    def __init__(self, name, locationclass, enemychanse):
        self.locationclass = locationclass
        self.name = name
        self.enemychanse = enemychanse