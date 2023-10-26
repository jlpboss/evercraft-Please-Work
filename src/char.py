from src.mods import mod

class Char:

    def __init__(self, name, alignment, mod_arr):
        self.name = name
        self.alignment = alignment
        self.hp = 5
        self.ac = 10
        self.str = mod(mod_arr[0], 0)
        self.dex = mod(mod_arr[1], 0)
        self.con = mod(mod_arr[2], 0)
        self.wis = mod(mod_arr[3], 0)
        self.int = mod(mod_arr[4], 0)
        self.riz = mod(mod_arr[5], 0)


    def attack(self, roll, enemy, to_hit_mod):
        if roll == 20: 
            return True
        elif roll + to_hit_mod >= enemy.ac:
            return True
        else:
            return False
        
    def calcDamage(self, roll, enemy, to_hit_mod, damage_mod, damage_roll): 
        if self.attack(roll, enemy, to_hit_mod):
            if(roll == 20):
                damage_roll = damage_roll * 2
            enemy.hp -= (damage_roll + damage_mod) 