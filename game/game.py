import random

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
        



fighter = dnd_Class(8, 1, 18, 2, False, False)
human = [1, 1, 1, 1, 1, 1]
charactor = Char("Will", "CG", [11,10,10,10,10,10], fighter, human)
d20 = die(20)

print("so your...")
char_name = input("So, What is your name? ")
char_class_str = input("whats your class? ")
charRace_str= input("so whats your race? ")
charAlign = input("so what is your aligment? ")


match char_class_str:
    case "fighter":
        char_class = dnd_Class(8, 1, 18, 2, False, False)

match charRace_str:
    case "human":
        charRace = [1, 1, 1, 1, 1, 1]

player_Charactor = Char(char_name, charAlign, [10,10,10,10,10,10], char_class, charRace)

print(player_Charactor.hp)
