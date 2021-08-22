

class Board:
    
    def __init__(self,  rows, cols, snake):
        self.rows = rows
        self.cols = cols
        self.board = [[(0,0)] * cols] * rows
        self.snake = snake
        self.fillBoard()

    def fillBoard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = (row, col)

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def __str__(self):
        result = ""
        for row in range(self.rows):
            for col in range(self.cols):
                result += "({}, {})".format(row, col)
            result += '\n'
        return result
    