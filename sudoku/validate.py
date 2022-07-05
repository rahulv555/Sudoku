
from sqlalchemy import true

from populateSudoku import getSudoku
import numpy as np


def Solve(g, i=0, j=0):
    if(i >= 9):
        return True
    if j >= 9:
        return Solve(g, i+1, 0)

    if(g[i][j] != 0):
        return Solve(g, i, j+1)

    for n in range(1, 10):
        if isValid(g, i, j, n):
            g[i][j] = n
            if(Solve(g, i, j+1) == True):
                return True
            g[i][j] = 0

    return False


def isValid(g, r, c, n):
    for i in range(0, 9):
        if(g[r][i] == n or g[i][c] == n):
            return False

    l = (int)(r//3)
    l = l*3
    u = (int)(c//3)
    u = u*3

    for i in range(l, l+3):
        for j in range(u, u+3):
            if g[i][j] == n:
                return False

    return True


# grid = getSudoku()
# print(grid)
# Solve(grid)
# print(grid)
