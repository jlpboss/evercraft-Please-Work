from src.char import Char
import pytest

charactor = Char("jett", "lga")

def test_make_name():
    assert charactor.name is not None
def test_Alignment():
    assert charactor.alignment is not None

def test_Health():
    assert charactor.hp == 5

def test_Armor():
    assert charactor.ac == 10