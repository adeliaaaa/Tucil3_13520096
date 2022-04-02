from typing import NamedTuple
from numpy import * 

class MyStruct(NamedTuple):
    matriksPuzzle: matrix
    cost: int

def getIndex(i,j):
    return ((4 * i) + j)

def findLower(matrix, row, col):
    sum = 0
    for i in range (0,4):
        for j in range (0,4):
            if((getIndex(i,j) > getIndex(row, col)) and (matrix[i][j] < matrix[row][col])):
                sum = sum + 1
    return sum

def KurangI(matrix):
    value = 0
    for i in range (0,4):
        for j in range (0,4):
            if((matrix[i][j] == 16) and (i % 2 == 0) and (j % 2 == 1)):
                value = value + 1
            elif ((matrix[i][j] == 16) and (i % 2 == 1) and (j % 2 == 0)):
                value = value + 1
            value = value + findLower(matrix, i, j)

    return value


my_item = MyStruct([[1,2,3,4], [5,6,16,8], [9,10,7,11], [13,14,15,12]], 0)

sigmaKurangI = KurangI(my_item.matriksPuzzle)

print(sigmaKurangI)
