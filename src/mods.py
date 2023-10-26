class mod:

    def __init__(self, value, additonal_mods):
        self.score = value + additonal_mods
        self.mod = (((value + additonal_mods) - 10) // 2)