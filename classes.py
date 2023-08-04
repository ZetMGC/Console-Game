import colorama
import random
from os import system
from types import FrameType
from progress.bar import FillingSquaresBar

from colorama import Fore, Back, Style

#--------------------------------------

PersonClass = ("PC_MAGICIAN", "PC_WARRIOR", "PC_ARCHER")
magician, warrior, archer = PersonClass

CharacterBonus = ("CB_STUN", "CB_BLEEDING", "CB_POISONING", "CB_REGEN", "CB_GAIN", "CB_WEAKNESS", "CB_NONE") # Оглушение, кровотечение, отравление, регенерация, усиление, слабость
stun, bleeding, poisoning, regen, gain, weakness, none = CharacterBonus

RangeClass = ("RC_NEAR", "RC_AVERAGE", "RC_FAR")
near, average, far = RangeClass

ItemClass = ("IC_POTION","IC_UNKNOWNPOTION", "IC_WEAPON", "IC_ARMOR", "IC_ACCESSORY")
potion, unknownpotion, weapon, armor, acc = ItemClass

LocationClass = ("LC_FORREST", "LC_SPAWN")
forrest, spawn = LocationClass

LocationDropClass = ("LDC_ORDINARY", "LDC_RARE", "LDC_LEGENDARY")
ordinary, rare, legendary = LocationDropClass

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
        self.bonus = none

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
            HPbar = FillingSquaresBar('Твое здоровье:', max = self.hpmax, suffix='%(index)d / %(max)d')
            HPbar.goto(self.hp)
            HPbar.color = 'red'
            HPbar.start()

            if self.sex == True:
                print("\nТвой пол мужской\n")
            else:
                print("\nТвой пол женский\n")
            
            if self.pclass == magician:
                print("Ты маг\n")
            elif self.pclass == warrior:
                print("Ты воин\n")
            elif self.pclass == archer:
                print("Ты лучник\n")

            if self.current_weapon != None:
                print("Твое оружие: ", Fore.GREEN + self.current_weapon.name + Style.RESET_ALL, end="\t\t")
            else:
                print("Твое оружие:", Fore.RED + "Нет." + Style.RESET_ALL, end="\t\t")
            
            if self.current_armor != None:
                print("Твоя броня: ", Fore.GREEN + self.current_armor.name, "\n" + Style.RESET_ALL)
            else:
                print("Твоя броня:", Fore.RED + "Нет.\n" + Style.RESET_ALL)            

            print("<------------------------------------------------------>")
            print(Fore.RED + "0. ПРОДОЛЖИТЬ" + Style.RESET_ALL)
            decide = input()
            if decide == "0":
                break
            else:
                continue

            HPbar.finish()

    def creator(self):
        system('CLS')
        self.name = input("Введите имя персонажа: ")
        system('CLS')

        while True:
            print("Введите", Fore.BLUE + "\"1\"", Style.RESET_ALL + ", чтобы выбрать мужской пол.\nВведите", Fore.BLUE + "\"2\"", Style.RESET_ALL + ", чтобы выбрать женский пол.\n")
            sex = input()
            system('CLS')
            if sex == "1":
                self.sex = True
                break
            elif sex == "2":
                self.sex = False 
                break
            else:
                print(Back.RED + "Вы выбрали неверное значение." + Style.RESET_ALL)
                continue     

        while True:
            print("Введите", Fore.BLUE + "\"1\"", Style.RESET_ALL + ", чтобы выбрать класс \"Воин\".\nВведите", Fore.BLUE + "\"2\"", Style.RESET_ALL + ", чтобы выбрать класс \"Маг\".\nВведите", Fore.BLUE + "\"3\"", Style.RESET_ALL + ", чтобы выбрать класс \"Лучник\".\n")
            pclass = input()
            system('CLS')
            if pclass == "1":
                self.pclass = warrior
                self.hpmax = 125
                self.hp = self.hpmax
                self.armor = 0.45
                self.stamina = 100
                break
            elif pclass == "2":
                self.pclass = magician
                self.hpmax = 75
                self.hp = self.hpmax
                self.armor = 0.15
                self.stamina = 100
                break
            elif pclass == "3":
                self.pclass = archer
                self.hpmax = 100
                self.hp = self.hpmax
                self.armor = 0.30
                self.stamina = 100
                break
            else:
                print(Back.RED + "Вы выбрали неверное значение." + Style.RESET_ALL)

#--------------------------------------

#базовый предмета
class Item:
    def __init__(self, name, itemclass):
        self.name = name
        self.itemclass = itemclass
        

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

#класс оружия
class WeaponItem(Item):
    def __init__(self, name, itemclass, damage, critchance):
        super().__init__(name, itemclass)
        self.damage = damage
        self.critchance = critchance
    
    def info(self, character):
        while True:
            system('CLS')
            print("<------------------------------------------------------>\n")

            print("Это", Fore.BLUE + self.name + Style.RESET_ALL, ".\n")
            print("Наносит:", Fore.GREEN + str(self.damage) + Style.RESET_ALL, "урона.\n")

            print("<------------------------------------------------------>\n")
            if character.current_weapon == self:
                print(Fore.RED + "1. ПЕРЕСТАТЬ ИСПОЛЬЗОВАТЬ" + Style.RESET_ALL)
            else:
                print(Fore.RED + "1. ИСПОЛЬЗОВАТЬ" + Style.RESET_ALL)
            print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)

            decide = input()
            if decide == "1":
                if character.current_weapon == self:
                    character.current_weapon = None
                else:
                    character.current_weapon = self
            elif decide == "0":
                break
            else:
                continue

# класс зелий
class PotionItem(Item):
    def __init__(self, name, itemclass, heal, manaheal):
        super().__init__(name, itemclass)
        self.heal = heal 
        self.manaheal = manaheal
    
    def info(self, character):
        while True:
            system('CLS')
            print("<------------------------------------------------------>\n")

            print("Это", Fore.BLUE + self.name + Style.RESET_ALL, ".\n")
            print("Оно восстанавливает:", Fore.GREEN + str(self.heal) + Style.RESET_ALL, "здоровья.\n")
            print("Оно восстанавливает:", Fore.GREEN + str(self.manaheal) + Style.RESET_ALL, "маны.\n")

            print("<------------------------------------------------------>\n")
            print(Fore.RED + "1. ИСПОЛЬЗОВАТЬ" + Style.RESET_ALL)
            print(Fore.RED + "0. НАЗАД" + Style.RESET_ALL)

            decide = input()
            if decide == "1":
                character.hp += self.heal
                character.potionitem.remove(self)
                break
            elif decide == "0":
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
    Drop = ([], [], [], [])
    ordinary, rare, legendary, ground = Drop
    
    def __init__(self, name, locationclass, enemychanse):
        self.locationclass = locationclass
        self.name = name
        self.enemychanse = enemychanse
        

    def DropDecider(self, chance):
        if chance > 0.4 and chance < 0.9:
            if len(self.ordinary) > 0:
                drop = random.choice(self.ordinary)
                self.ground.append(drop)
                self.ordinary.remove(drop)