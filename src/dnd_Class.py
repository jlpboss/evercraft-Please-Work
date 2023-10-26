
class dnd_Class: 
    def __init__(self, hp, lvl_hit, crit_chance, crit_mult, is_mage, is_theif):
        self.health = hp
        self.lvl_hit = lvl_hit
        self.crit_Number = crit_chance
        self.crit_mult = crit_mult
        self.use_mental_for_attack = is_mage
        self.use_dex_for_attack = is_theif
