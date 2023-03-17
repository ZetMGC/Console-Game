import random
import classes
from classes import CharacterBonus
from os import system
from colorama import Fore, Back, Style

#----------------------------------------------------------------

BattleActions = ("BA_ATTACK", "BA_DODGE", "BA_BLOCK", "BA_HIDE",  "BA_CHANGEPOS")
attack, dodge, block, hide, changepos = BattleActions

#----------------------------------------------------------------

def battleHandler(character, enemy):
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
            print(Fore.RED + "4. ЗАНЯТЬ ВЫГОДНУЮ ПОЗИЦИЮ" + Style.RESET_ALL)
            print(Fore.RED + "0. СБЕЖАТЬ" + Style.RESET_ALL)

            decide = int(input())
            if decide == 1:
                battleSystem(character, enemy, attack)
            elif decide == 2:
                battleSystem(character, enemy, dodge)
            elif decide == 3:
                battleSystem(character, enemy, block)
            elif  decide == 4:
                battleSystem(character, enemy, changepos)
            elif decide == 0:
                battleSystem(character, enemy, hide)
            else:
                continue

        elif enemy.hp <= 0:
            system('CLS')
            print("ПОБЕДИЛ")
            return character, enemy
        elif character.hp <= 0:
            system('CLS')
            print("ПРОИГРАЛ")
            return character, enemy

def CriticalDamage(character):
    Stamina = character.stamina
    Damage = character.current_weapon.damage
    CritChance = character.current_weapon.critchance
    if (Stamina > 80):
        if (random.random() < CritChance):
            Damage *= random.randrange(80, 100)/100
            character.stamina -= round(Damage*10)
            return Damage
        else:
            return 0
    elif (Stamina > 50):
        if (random.random() < CritChance):
            Damage *= random.randrange(50, 100)/100
            character.stamina -= round(Damage*10)
            return Damage
        else:
            return 0
    elif (Stamina > 30):
        if (random.random() < CritChance):
            Damage *= random.randrange(30, 100)/100
            character.stamina -= round(Damage*10)
            return Damage
        else:
            return 0
    elif (Stamina > 0):
        if (random.random() < CritChance):
            Damage *= random.randrange(0, 100)/100
            character.stamina -= round(Damage*10)
            return Damage
        else:
            return 0
    elif (Stamina <= 0):
        return 0

def battleSystem(character, enemy, battleaction):
    # если игрок в стане
    if character.bonus == classes.stun: 
        currentDamage = character.current_weapon.damage

    # если игрок кровоточит
    elif character.bonus == classes.bleeding:
        currentDamage = character.current_weapon.damage

    # если игрок отравлен
    elif character.bonus == classes.poisoning:
        currentDamage = character.current_weapon.damage

    # если игрок
    elif character.bonus == classes.regen: 
        currentDamage = character.current_weapon.damage
    
    # если игрок под усилением
    elif character.bonus == classes.gain:
        currentDamage = character.current_weapon.damage
    
    # если на игрока наложена слабость
    elif character.bonus == classes.weakness:
        currentDamage = character.current_weapon.damage
    
    # если на игрока не действуют эффекты
    else:
        currentDamage = character.current_weapon.damage
    
    # АТАКА
    if battleaction == attack:
        # Атака противника влоб
        enemy.hp -= currentDamage - (currentDamage * enemy.armor) + CriticalDamage(character)
        enemy.hp = round(enemy.hp, 1)
        # Противник атакует в ответ
        character.hp -= enemy.damage - (enemy.damage * character.armor)
        character.hp = round(character.hp, 1)

    # УКЛОНЕНИЕ
    elif battleaction == dodge:
        if character.stamina >= 80:
            if random.randint(0, 3) > 0:
                # удалось уклониться, атакуем двойным уроном, сами урона не получаем
                enemy.hp -= (character.current_weapon.damage - (character.current_weapon.damage * enemy.armor)) * 2 - (character.current_weapon.damage * character.current_armor)
                enemy.hp = round(enemy.hp, 1)
                character.stamina -= 20
            else:
                # Враг атакует, если уколниться не удалось
                character.hp -= enemy.damage - (enemy.damage * character.armor)
                character.hp = round(character.hp, 1)
                character.stamina -= 20
        elif character.stamina >= 50:
            # При меньшей стамине шанс уклонения ниже
            if random.randint(0,5) > 3:
                enemy.hp -= (character.current_weapon.damage - (character.current_weapon.damage * enemy.armor)) * 1.5 - (character.current_weapon.damage * character.current_armor)
                enemy.hp = round(enemy.hp, 1)
                character.stamina -= 20
            else:
                character.hp -= enemy.damage - (enemy.damage * character.armor)
                character.hp = round(character.hp, 1)
                character.stamina -= 20
        else:
            character.hp -= enemy.damage - (enemy.damage * character.armor)
            character.hp = round(character.hp, 1)
            character.stamina -= 20

    # БЛОК
    elif battleaction == block:
        print("Блок")
    elif battleaction == hide:
        print("Спрятаться")
