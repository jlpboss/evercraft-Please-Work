from src.char import Char
import pytest
from src.dnd_Class import dnd_Class
from src.dice import die
# (self, hp, crit_chance, crit_mult, is_mage, is_theif)
fighter = dnd_Class(8, 1, 18, 2, False, False)
mage = dnd_Class(3, 2, 20, 2, True, False)
theif = dnd_Class(5, 2, 20, 3, False, True)
none = dnd_Class(5, 2, 20, 2, False, False)

noRace = [0, 0, 0, 0, 0, 0]
human = [1, 1, 1, 1, 1, 1]
elf = [0, 2, 0, 0, 1, 0]
dwarf = [1, 0, 2, 0, 0, 0]
gnome = [0, 0, 0, 2, 1, 0]
half_Orc = [2, 0, 1, 0, 0, 0]
half_elf = [0, 1, 1, 0, 0, 2]

def test_make_name():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10], none, noRace)
    assert charactor.name is not None
def test_Alignment():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10], none, noRace)
    assert charactor.alignment is not None

def test_Health():
    charactor = Char("jett", "lga", [10, 10, 1, 10, 10, 10], none, noRace)
    assert charactor.hp == 1

def test_Armor():
    charactor = Char("jett", "lga", [10, 16, 10, 10, 10, 10], none, noRace)
    assert charactor.ac == 13

def test_Attack(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10], none, noRace)
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10], none, noRace)
    assert type(charactor.attack(15, charactor2, 3)) == bool

def test_calc_dmg():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10], none, noRace)
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10], none, noRace)
    charactor.calcDamage(19, charactor2, 1)
    assert charactor2.hp == 4

def test_crit():
    charactor = Char("jett", "lga", [16, 10, 10, 10, 10, 10], none, noRace)
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10], none, noRace)
    charactor2.ac = 100
    charactor.calcDamage(20, charactor2, 1)
    assert charactor2.hp == 0

def test_str(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10], none, noRace)
    assert charactor.str.mod == 0

def test_dex(): 
    charactor = Char("jett", "lga", [10, 1, 10, 10, 10, 10], none, noRace)
    assert charactor.dex.mod == -5

def test_con(): 
    charactor = Char("jett", "lga", [10, 10, 20, 10, 10, 10], none, noRace)
    assert charactor.con.mod == 5

def test_wis(): 
    charactor = Char("jett", "lga", [10, 10, 10, 11, 10, 10], none, noRace)
    assert charactor.wis.mod == 0

def test_int(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 7, 10], none, noRace)
    assert charactor.int.mod == -2

def test_riz(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 12], none, noRace)
    assert charactor.riz.mod == 1

def test_xp():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10], none, noRace)
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10], none, noRace)
    charactor.calcDamage(19, charactor2, 1)
    assert charactor.xp == 10

def test_lvl():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10], none, noRace)
    charactor.xp = 1000
    charactor.testLvl()
    assert charactor.lvl == 2

# From here
def test_extra_lvl_hp():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10], none, noRace)
    charactor.xp = 1000
    charactor.testLvl()
    assert charactor.hp == 10

def test_extra_dmg():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10], none, noRace)
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10], none, noRace)
    charactor.xp = 4000
    charactor.testLvl()
    charactor.calcDamage(8, charactor2, 1)
    assert charactor2.hp == 4

def test_death(): 

    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10], theif, noRace)
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10], none, noRace)
    # charactor.xp = 4000
    # charactor.testLvl()
    charactor.calcDamage(20, charactor2, 5)
    charactor2.calcDamage(20, charactor, 5)
    assert charactor.hp == 5

def test_Fighter_hp(): 
    charactor = Char("Will", "CG", [10,10,10,10,10,10], fighter, noRace)
    assert charactor.hp == 8

def test_FIghter_to_hit():
    charactor = Char("Will", "CG", [10,10,10,10,10,10], fighter, noRace)
    charactor2 = Char("Will", "CG", [10,10,10,10,10,10], mage, noRace)
    charactor.calcDamage(9, charactor2, 3)
    assert charactor2.is_alive == False

def test_mage_Attack():
    charactor = Char("Will", "CG", [10,10,10,12,12,14], mage, noRace)
    charactor2 = Char("Jett", "CG", [10,10,10,10,10,10], mage, noRace)
    charactor.calcDamage(9, charactor2, 1)
    assert charactor2.is_alive == False

def test_theif_Attack():
    charactor = Char("Will", "CG", [10,14,10,10,10,10], theif, noRace)
    charactor2 = Char("Jett", "CG", [10,10,10,10,10,10], mage, noRace)
    charactor.calcDamage(9, charactor2, 1)
    assert charactor2.is_alive == False

def test_theif_crit():
    charactor = Char("Will", "CG", [10,10,10,10,10,10], theif, noRace)
    charactor2 = Char("Jett", "CG", [10,10,10,10,10,10], mage, noRace)
    charactor.calcDamage(20, charactor2, 1)
    assert charactor2.hp == 0

def test_race():
    charactor = Char("Will", "CG", [11,10,10,10,10,10], fighter, human)
    charactor2 = Char("jett", "CG", [10,10,10,10,10,10], mage, human)
    charactor.calcDamage(8, charactor2, 3)
    assert charactor2.is_alive == False

def test_die_roll():
    d20 = die(20)
    x = d20.roll()
    assert x == d20.value