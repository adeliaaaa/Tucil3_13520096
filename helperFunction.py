import random
from numpy import *

def getIndex(i,j):
    return ((4 * i) + j)

def findLower(matrix, row, col):
    sum = 0
    for i in range (0,4):
        for j in range (0,4):
            if((getIndex(i,j) > getIndex(row, col)) and (matrix[i][j] < matrix[row][col])):
                sum = sum + 1
    return sum

def findIndexOfElmnt(matrix, elmnt):
    for i in range (0,4):
        for j in range (0,4):
            if(matrix[i][j] == elmnt):
                return i, j

def readMyFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        a = [[int(x) for x in line.split()] for line in lines]
    return a

def createRandomPuzzle():
    a = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    random.shuffle(my_list)

    for i in range (0,4):
        for j in range (0,4):
            a[i][j] = my_list[getIndex(i,j)]

    return a

def moveUp(matrix, i, j):
    newMatrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for k in range (4):
        for l in range (4):
            newMatrix[k][l] = matrix[k][l]

    temp = newMatrix[i-1][j]
    newMatrix[i-1][j] = newMatrix[i][j]
    newMatrix[i][j] = temp

    return newMatrix

def moveDown(matrix, i, j):
    newMatrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for k in range (4):
        for l in range (4):
            newMatrix[k][l] = matrix[k][l]

    temp = newMatrix[i+1][j]
    newMatrix[i+1][j] = newMatrix[i][j]
    newMatrix[i][j] = temp

    return newMatrix

def moveRight(matrix, i, j):
    newMatrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for k in range (4):
        for l in range (4):
            newMatrix[k][l] = matrix[k][l]
    
    temp = newMatrix[i][j+1]
    newMatrix[i][j+1] = newMatrix[i][j]
    newMatrix[i][j] = temp

    return newMatrix

def moveLeft(matrix, i, j):
    newMatrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for k in range (4):
        for l in range (4):
            newMatrix[k][l] = matrix[k][l]

    temp = newMatrix[i][j-1]
    newMatrix[i][j-1] = newMatrix[i][j]
    newMatrix[i][j] = temp

    return newMatrix

def sumOfNotMatch(matrix):
    newMatrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

    sum = 0
    for i in range (0,4):
        for j in range (0,4):
            if(matrix[i][j] != 16):
                if(matrix[i][j] != newMatrix[i][j]):
                    sum = sum + 1
    return sum

def realDepth(depth):
    a = depth
    return a * (-1)