from typing import Sized
from collections import deque
import board

class Snake:

    def __init__(self, board):
        
        self.board = board
        self.maxLength = self.board.getRows() * self.board.getCols()
        self.length = 3
        self.body = deque()


    def setBody(self, board):
        rows = board.getRows()
        cols = board.getCols()
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
    

    
    