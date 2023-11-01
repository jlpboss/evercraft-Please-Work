
class dnd_Class: 
    def __init__(self, hp, lvl_hit, crit_chance, crit_mult, stats_for_attack, stats_for_ac, bounus_stats_for_attack, bounus_stats_for_ac):
        self.health = hp
        self.lvl_hit = lvl_hit
        self.crit_Number = crit_chance
        self.crit_mult = crit_mult
        self.stats_for_attack = stats_for_attack
        self.stats_for_ac = stats_for_ac
        self.bounus_stats_for_attack = bounus_stats_for_attack
        self.bounus_stats_for_ac = bounus_stats_for_ac
