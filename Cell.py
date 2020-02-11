class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
    def __str__(self):
         return "Row:" + str(self.row) + " Col:" + str(self.col) + " " + str(self.left) + " " + str(self.top) + " " + str(self.right) + " " + str(self.bottom)