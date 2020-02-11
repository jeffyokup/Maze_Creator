import random

tableSize = 3
grid = []
for row in range(tableSize):
    new = []
    for col in range(tableSize):
        new.append(0)
    grid.append(new)


def printGrid(grid):
    for row in range(tableSize):
        for col in range(tableSize):
            print(grid[row][col], end = " ")
        print()


x = random.randint(1, 10)
print(x)