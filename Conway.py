import random
import sys
import time

def Conway(rows, columns, iterations):
    grid = InitializeGrid(rows, columns)
    itr = 0
    while itr < iterations:
        DisplayGrid(grid)
        grid = GetNextState(grid)
        itr+=1
        time.sleep(1)

            
def GetLivingNeighbors(grid, row, col):
    living = 0
    for i in range(row-1, row+2):
        for j in range(col-1,col+2):
            if not (i == row and j == col):
                living += grid[i][j]
    return living

def InitializeGrid(rows, columns):
    grid = [[0 for x in range(columns+2)] for x in range(rows+2)]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            if random.random() < 0.20:
                grid[i][j] = True
            else:
                grid[i][j] = False
    return grid

def GetNextState(grid):
    nextGrid = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            numLivingNeighbors = GetLivingNeighbors(grid, i, j)
            if numLivingNeighbors == 3 or (grid[i][j] and numLivingNeighbors == 2):
                nextGrid[i][j] = True
            else:
                nextGrid[i][j] = False
    return nextGrid

def DisplayGrid(grid):
    output = ''
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j]:
                output += '#'
            else:
                output += '.'
        output += '\n'
    print output

def TestGrid():
    #grid = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    grid = [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
    for i in range(0, 10):
        DisplayGrid(grid)
        grid = GetNextState(grid)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Not the correct number of arguments. Please input in the format \'python Conway.py <rows> <cols> <iterations>\''
        exit()
    Conway(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
#    TestGrid()
