from typing import Sized
from collections import deque
import board

class Snake:

    def __init__(self, rows, cols):
        self.length = 3
        self.body = deque()
        self.setBody(rows, cols)
        

    def setBody(self, rows, cols):
        if(rows > 10):
            headPos = (rows // 2) - 1
            xPos = cols // 2
            for i in range(3):
                self.body.append((headPos + i, xPos))
            
    def getLength(self):
        return self.length    

    def bodyHas(self, cell):
        if(self.body.count(cell) > 0):
            return True
        else:
            return False

    def getBody(self):
        return self.body
    

    
    