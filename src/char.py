from src.mods import mod

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

        if self.hp < 1:
            self.hp = 1

        self.attack_mod_types = self.make_mod_list(self.dnd_Class.stats_for_attack)
        self.ac_mod_types = self.make_mod_list(self.dnd_Class.stats_for_ac)
        self.attack_mod_bonus = self.make_mod_list(self.dnd_Class.bounus_stats_for_attack)
        self.ac_mod_bonus = self.make_mod_list(self.dnd_Class.bounus_stats_for_ac)
        
        self.attack_mod_types.sort()
        self.ac_mod_types.sort()
        self.to_hit_mod = self.attack_mod_types[-1] + sum(self.attack_mod_bonus)
        self.damage_mod = self.attack_mod_types[-1] + sum(self.attack_mod_bonus)
        self.ac = 10 + self.ac_mod_types[-1] + sum (self.ac_mod_bonus)


    def make_mod_list(self, list):
        out = []
        for item in list:
            match item:
                case "str":
                    out.append(self.str.mod)
                case "dex":
                    out.append(self.dex.mod)
                case "con":
                    out.append(self.con.mod)
                case "wiz":
                    out.append(self.wiz.mod)
                case "int":
                    out.append(self.int.mod)
                case "cha":
                    out.append(self.riz.mod)
        return out

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
        