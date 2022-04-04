import random
from numpy import *

from displayAscii import *

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

def sumOfNotMatch(matrix):
    newMatrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

    sum = 0
    for i in range (0,4):
        for j in range (0,4):
            if(matrix[i][j] != 16):
                if(matrix[i][j] != newMatrix[i][j]):
                    sum = sum + 1
    return sum

def insertFile():
    asciiInsertFileName()
    print("type 'Random' to generate a random puzzle")
    print("type filename to load a puzzle from a file")
    print()
    fileName = input("Insert file name: ")
    if(fileName == "Random"):
        return createRandomPuzzle()
    else:
        fileName = "./src/TestCase/" + fileName

        puzzle = readMyFile(fileName)

        return puzzle

def printMatrix(matrix):
    print("-------------------------")
    for i in range (0,4):
        for j in range (0,4):
            print("|", end="  ")
            if(matrix[i][j] < 10):
                print(matrix[i][j], end="  ")
            else:
                if(matrix[i][j] == 16):
                    print(end="   ")
                else:
                    print(matrix[i][j], end=" ")
        print("|")
        print("-------------------------")

def kurangItiapUbin(matrix):
    print("Nilai kurang(i) tiap ubin: ")
    for i in range(1,17):
        row, col = findIndexOfElmnt(matrix,i)
        print("Kurang(", i, ") = ", findLower(matrix, row, col))

def KurangIValue(matrix):
    value = 0
    for i in range (0,4):
        for j in range (0,4):
            if((matrix[i][j] == 16) and (i % 2 == 0) and (j % 2 == 1)):
                value = value + 1
            elif ((matrix[i][j] == 16) and (i % 2 == 1) and (j % 2 == 0)):
                value = value + 1
            value = value + findLower(matrix, i, j)
    return value

def printKurangIValue(matrix):
    print()
    print("Nilai dari Kurang(i) value + X: ", KurangIValue(matrix))

def printUrutanMatrix(path):
    print("Urutan Penyelesaian: ")
    stepCounter = 0
    for matrix in path:
        if(stepCounter == 0):
            print("Matrix semula: ")
            printMatrix(matrix)
            print()
        else:
            print("Step ke-", stepCounter)
            printMatrix(matrix)
            print()
        stepCounter = stepCounter + 1