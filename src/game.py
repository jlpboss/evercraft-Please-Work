from char import Char
from dnd_Class import dnd_Class
from dice import die

fighter = dnd_Class(8, 1, 18, 2, False, False)
human = [1, 1, 1, 1, 1, 1]
charactor = Char("Will", "CG", [11,10,10,10,10,10], fighter, human)
d20 = die(20)

print("so your...")
char_name = input("So, What is your name? ")
