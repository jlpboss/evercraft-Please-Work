import random
# from src.char import Char
# from src.dice import die
# from src.dnd_Class import dnd_Class

class die:

    def __init__(self, valueRange):
        self.value = None
        self.valueRange = valueRange

    def roll(self):
        holdRandom = random.randrange(1, self.valueRange, 1)
        self.value = holdRandom
        return holdRandom

class mod:

    def __init__(self, value, additonal_mods):
        self.score = value + additonal_mods
        self.mod = (((value + additonal_mods) - 10) // 2)


class dnd_Class: 
    def __init__(self, hp, lvl_hit, crit_chance, crit_mult, is_mage, is_theif):
        self.health = hp
        self.lvl_hit = lvl_hit
        self.crit_Number = crit_chance
        self.crit_mult = crit_mult
        self.use_mental_for_attack = is_mage
        self.use_dex_for_attack = is_theif


class Char:

    def __init__(self, name, alignment, mod_arr, dnd_Class, dnd_race):
        self.name = name
        self.alignment = alignment
        self.str = mod(mod_arr[0], dnd_race[0])
        self.dex = mod(mod_arr[1], dnd_race[1])
        self.con = mod(mod_arr[2], dnd_race[2])
        self.wis = mod(mod_arr[3], dnd_race[3])
        self.int = mod(mod_arr[4], dnd_race[4])
        self.riz = mod(mod_arr[5], dnd_race[5])
        self.dnd_Class = dnd_Class
        self.hp = self.dnd_Class.health + self.con.mod 
        self.ac = 10 + self.dex.mod
        self.xp = 0
        self.lvl = (self.xp // 1000) + 1
        self.is_alive = True
        self.to_hit_mod = self.str.mod
        self.damage_mod = self.str.mod

        if self.hp < 1:
            self.hp = 1

        if self.dnd_Class.use_mental_for_attack:
            mental_mods = [self.int.mod, self.wis.mod, self.riz.mod]
            mental_mods.sort()
            self.to_hit_mod = mental_mods[-1]
            self.damage_mod = mental_mods[-1]
            self.ac = 10 + mental_mods[-1]

        if self.dnd_Class.use_dex_for_attack:
            self.to_hit_mod = self.str.mod + self.dex.mod
            self.damage_mod = self.str.mod + self.dex.mod

    def attack(self, roll, enemy, to_hit_mod):
        if roll >= self.dnd_Class.crit_Number: 
            return True
        elif roll + to_hit_mod >= enemy.ac:
            return True
        else:
            return False
        
    def calcDamage(self, roll, enemy, damage_roll): 
        if self.is_alive:
            if self.attack(roll, enemy, self.to_hit_mod + self.lvl // self.dnd_Class.lvl_hit):
                if roll >= self.dnd_Class.crit_Number:
                    damage_roll = damage_roll * self.dnd_Class.crit_mult
                total_dmg = (damage_roll + self.damage_mod)
                if total_dmg <= 1:
                    total_dmg = 1
                enemy.hp -= total_dmg
                if enemy.hp <= 0:
                    enemy.is_alive = False
                self.testLvl()

    def testLvl(self):
        self.xp += 10
        if self.lvl != (self.xp // 1000) + 1:
            self.hp += self.dnd_Class.health + self.con.mod
        self.lvl = (self.xp // 1000) + 1
        

def random_Stat():
    d6 = die(6)
    one = d6.roll()
    two = d6.roll()
    three = d6.roll()
    return one + two + three

def print_stats(player_Charactor, char_class_str, charRace_str):
    stats_out ="""

    {}: 

    Class: {}
    Race: {}

    Hp: {}
    AC: {}
    Alignment: {}

    Level: {}
    Xp: {}

    Str: {}
    Dex: {}
    Con: {}
    Wis: {}
    Int: {}
    Cha: {}

    """.format(player_Charactor.name, char_class_str, charRace_str, player_Charactor.hp, player_Charactor.ac, player_Charactor.alignment, player_Charactor.lvl, player_Charactor.xp, player_Charactor.str.score, player_Charactor.dex.score, player_Charactor.con.score, player_Charactor.wis.score, player_Charactor.int.score, player_Charactor.riz.score)
    print(stats_out)

def random_enemy():
    d4 = die(4)
    d15 = die(15)
    d6 = die(6)
    class_list = ["fighter", "mage", "theif", "lame_O"]
    name_list = ["Justin", "Ezekial", "Trés", "Goblin Mode", "Shrek", "Letoys", "Orgaega", "Rubrae", "Eglantine", "Samara", "Bitha", "Mimosa", "Dalvura", "Yathlanae", "2015 Kanye"]
    race_list = ["human", "elf", "dwarf", "gnome", "half_orc", "half_elf"]
    char_class_str = class_list[d4.roll() - 1]
    char_name = name_list[d15.roll() - 1]
    charRace_str = race_list[d6.roll() - 1]
    charAlign = "TN"

    match char_class_str:
        case "fighter":
            char_class = dnd_Class(8, 1, 18, 2, False, False)
        case "mage":
            char_class = dnd_Class(3, 2, 20, 2, True, False)
        case "theif":
            char_class = dnd_Class(5, 2, 20, 3, False, True)
        case "lame_O":
            char_class = dnd_Class(5, 1, 20, 2, False, False)

    match charRace_str:
        case "human":
            charRace = [1, 1, 1, 1, 1, 1]
        case"elf":
            charRace= [0, 2, 0, 0, 1, 0]
        case "dwarf":
            charRace = [1, 0, 2, 0, 0, 0]
        case "gnome":
            charRace = [0, 0, 0, 2, 1, 0]
        case "half_orc":
            charRace = [2, 0, 1, 0, 0, 0]
        case "half_elf":
            charRace = [0, 1, 1, 0, 0, 2]


    return [Char(char_name, charAlign, [random_Stat(), random_Stat(), random_Stat(), random_Stat(), random_Stat(), random_Stat()], char_class, charRace), char_class_str, charRace_str]

fighter = dnd_Class(8, 1, 18, 2, False, False)
human = [1, 1, 1, 1, 1, 1]
charactor = Char("Will", "CG", [11,10,10,10,10,10], fighter, human)
d20 = die(20)

character_Finished = False

print("""
Hey, you. You’re finally awake. You were trying to cross the border,
right? Walked right into that Imperial ambush, same as us, and that
thief over there.
But who ... are you?
""")


while not character_Finished:
    char_name = input("What is your name? ")
    char_class_str = input("Whats your class? (fighter, mage, theif) ")
    charRace_str= input("Whats your race? (human, elf, dwarf, gnome, half_orc, half_elf) ")
    charAlign = input("What is your aligment? ")


    match char_class_str:
        case "fighter":
            char_class = dnd_Class(8, 1, 18, 2, False, False)
        case "mage":
            char_class = dnd_Class(3, 2, 20, 2, True, False)
        case "theif":
            char_class = dnd_Class(5, 2, 20, 3, False, True)
        case "BIGGEST BIRD":
            char_class = dnd_Class(12, 0.5, 10, 4, True, True)

    match charRace_str:
        case "human":
            charRace = [1, 1, 1, 1, 1, 1]
        case"elf":
            charRace= [0, 2, 0, 0, 1, 0]
        case "dwarf":
            charRace = [1, 0, 2, 0, 0, 0]
        case "gnome":
            charRace = [0, 0, 0, 2, 1, 0]
        case "half_orc":
            charRace = [2, 0, 1, 0, 0, 0]
        case "half_elf":
            charRace = [0, 1, 1, 0, 0, 2]

    player_Charactor = Char(char_name, charAlign, [random_Stat(), random_Stat(), random_Stat(), random_Stat(), random_Stat(), random_Stat()], char_class, charRace)

    print_stats(player_Charactor, char_class_str, charRace_str)

    correct = input("Does this look correct?(y/n) ")

    if correct == "y":
        character_Finished = True

kills = 0
while player_Charactor.is_alive:
    d20 = die(20)
    d6 = die(6)
    print("Watch out! An enemy is approaching!")
    [enemy, enemy_class, enemy_race] = random_enemy()
    print_stats(enemy, enemy_class, enemy_race)

    while enemy.is_alive:
        if player_Charactor.is_alive == False:
            break
        input("attack? ")
        old_hp = enemy.hp
        player_Charactor.calcDamage(d20.roll(), enemy, d6.roll())

        if player_Charactor.attack(d20.value, enemy, player_Charactor.to_hit_mod): 
            print("""
            You Hit {} with a {} and did {} damage
            """.format(enemy.name, d20.value, old_hp - enemy.hp))
        else:
            print("""
            You Missed {} with a {} doing no damage
            """.format(enemy.name, d20.value))

        print("{} attacks you!".format(enemy.name))

        old_hp = player_Charactor.hp
        enemy.calcDamage(d20.roll(), player_Charactor, d6.roll())

        if enemy.attack(d20.value, player_Charactor, enemy.to_hit_mod): 
            print("""
            {} hit you with a {} and did {} damage
            """.format(enemy.name, d20.value, old_hp - player_Charactor.hp))
        else:
            print("""
            {} Missed you with a {} doing no damage
            """.format(enemy.name, d20.value))
    
    if not enemy.is_alive:
        print("You Killed {}".format(enemy.name))
        kills += 1

print("You fought valiantly and killed {} enemies. Final stats:".format(kills))
print_stats(player_Charactor, char_class_str, charRace_str)
