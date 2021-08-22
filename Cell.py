class Cell:

    def __init__(self, row, col, type):
        self.pos = (row, col)
        self.type = type
    
    def setType(self, newType):
        self.type = newType

    def getPos(self):
        return self.pos

    def __eq__(self, obj):
        if isinstance(obj, Cell):
            o = Cell(obj)
            if(self.pos == o.getPos()):
                return True
        return False
