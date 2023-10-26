class Char:


    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment.upper()
        self.testAlign()
        self.hp = 5
        self.ac = 10

    
    def testAlign(self):
        totalAlignments = ["LG", "NG", "CG", "LN", "TN", "CN", "LE","NE", "CE"]
        # Tests if alignment is contained in here. If not we don't want it 
        while self.alignment not in totalAlignments: 
            new_input = input("invalid alignment ").upper()
            self.alignment = new_input
