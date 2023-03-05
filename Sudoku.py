import numpy as np
import random


def make_grid(numbers):
    grid = []
    line = []
    a = 0
    for i in numbers:
        line.append(int(i))
        a +=1
        if a % 9 == 0:
            grid.append(line)
            line = []
    return grid
    
def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print(" ",end="")
    print(((str(np.matrix(grid))).replace("[","")).replace("]",""))

    
def check_valid(mesh,r,c,n):
    valid = True
    #check row and column
    for x in range(9):
        if mesh[x][c] == n:
            valid = False
            break
    for y in range(9):
        if mesh[r][y] == n:
            valid = False
            break
    row_section = r // 3
    col_section = c // 3
    for x in range(3):
        for y in range(3):
            #check if section is valid
            if mesh[row_section * 3 + x][col_section * 3 + y] == n:
                valid = False
                break
    return valid

def generate(q):
    
    for i in range(q):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while not check_valid(grid,row,col,num) or grid[row][col]!=0:
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        grid[row][col]=num

    print(" ",end="")
    print(((str(np.matrix(grid))).replace("[","")).replace("]",""))

