from src.char import Char
import pytest



def test_make_name():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.name is not None
def test_Alignment():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.alignment is not None

def test_Health():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.hp == 5

def test_Armor():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.ac == 10

def test_Attack(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    assert type(charactor.attack(15, charactor2, 3)) == bool

def test_calc_dmg():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    charactor.calcDamage(19, charactor2, 1, 0, 1)
    assert charactor2.hp == 4

def test_crit():
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    charactor2 = Char("will", "Lg", [10, 10, 10, 10, 10, 10])
    charactor2.ac = 100
    charactor.calcDamage(20, charactor2, 1, 0, 1)
    assert charactor2.hp == 3

def test_str(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.str is not None

def test_dex(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.dex is not None

def test_con(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.con is not None

def test_wis(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.wis is not None

def test_int(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.int is not None

def test_riz(): 
    charactor = Char("jett", "lga", [10, 10, 10, 10, 10, 10])
    assert charactor.riz is not None