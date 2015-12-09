class Square:
    def __init__(self, name):
        """Takes as input square name as a string. (e.g. C4). Can return column and row information, as well as square name. Additionally, can say whether it is under attack?"""
        self.name=name
        self.column=name[0]
        self.row=name[1]
        self.under_attack=False   
         
    def return_name(self):
        """returns name of square"""
        return self.name
    def return_column(self):
        return self.column
    def return_row(self):
        return self.row
    def is_under_attack(self):
        return self.under_attack

#To check whether something is under attack, check whether a queen is on the same column or row first. Then, check the diagonals (+1 column +1 row; -1 column -1 row; +1 column -1row; -1 column +1 row. Until the edge of the board. Recursively code this?)

a1=Square("a1")
a2=Square("a2")
a3=Square("a3")
a4=Square("a4")
a5=Square("a5")
a6=Square("a6")
a7=Square("a7")
a8=Square("a8")

class Column:
    def __init__(self, name):
        self.name=name
        
        
class Row:
    def __init__(self, name):
        self.name=name

class Board:
    def __init__(self):
        