from src.char import Char
import pytest



def test_make_name():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.name is not None
def test_Alignment():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.alignment is not None

def test_Health():
    charactor = Char("jett", "lga", [10, 10, 1, 10, 10, 10])
    assert charactor.hp == 1

def test_Armor():
    charactor = Char("jett", "lga", [10, 16, 10, 10, 10, 10])
    assert charactor.ac == 13

def test_Attack(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    assert type(charactor.attack(15, charactor2, 3)) == bool

def test_calc_dmg():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    charactor.calcDamage(19, charactor2, charactor.str.mod, charactor.str.mod, 1)
    assert charactor2.hp == 4

def test_crit():
    charactor = Char("jett", "lga", [16, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    charactor2.ac = 100
    charactor.calcDamage(20, charactor2, charactor.str.mod, charactor.str.mod, 1)
    assert charactor2.hp == 0

def test_str(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.str.mod == 0

def test_dex(): 
    charactor = Char("jett", "lga", [10, 1, 10, 10, 10, 10])
    assert charactor.dex.mod == -5

def test_con(): 
    charactor = Char("jett", "lga", [10, 10, 20, 10, 10, 10])
    assert charactor.con.mod == 5

def test_wis(): 
    charactor = Char("jett", "lga", [10, 10, 10, 11, 10, 10])
    assert charactor.wis.mod == 0

def test_int(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 7, 10])
    assert charactor.int.mod == -2

def test_riz(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 12])
    assert charactor.riz.mod == 1

def test_xp():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    charactor.calcDamage(19, charactor2, charactor.str.mod, charactor.str.mod, 1)
    assert charactor.xp == 10

def test_lvl():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10])
    charactor.xp = 1000
    charactor.testLvl()
    assert charactor.lvl == 2

# From here
def test_extra_lvl_hp():
    charactor = Char("jett", "lga", [1, 10, 10, 10, 10, 10])
    charactor.xp = 1000
    charactor.testLvl()
    assert charactor.hp == 10

def test_extra_dmg():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    charactor.xp = 4000
    charactor.testLvl()
    charactor.calcDamage(8, charactor2, charactor.str.mod, charactor.str.mod, 1)
    assert charactor2.hp == 4