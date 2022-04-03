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

def asciiGameName():
    print("____  _______   _______  __   __  _______  _______  ___      _______ ")
    print("|    ||       | |       ||  | |  ||       ||       ||   |    |       |")
    print("|   ||   ____| |    _  ||  | |  ||____   ||____   ||   |    |    ___|")
    print("|   ||  |____  |   |_| ||  |_|  | ____|  | ____|  ||   |    |   |___ ")
    print("|   ||_____  | |    ___||       || ______|| ______||   |___ |    ___|")
    print("|   | _____| | |   |    |       || |_____ | |_____ |       ||   |___ ")
    print("|___||_______| |___|    |_______||_______||_______||_______||_______|")
    print("Welcome to 15 puzzle!!!")
    print()

def asciiInsertFileName():
    print(" ___                  _     ___ _ _                         ")
    print("|_ _|_ _  ___ ___ _ _| |_  | __(_) |___ _ _  __ _ _ __  ___ ")
    print("|  || ' \(_-</ -_) '_|  _| | _|| | / -_) ' \/ _` | '  \/ -_)")
    print("|___|_||_/__/\___|_|  \__| |_| |_|_\___|_||_\__,_|_|_|_\___|")

def asciiSolvingPuzzle():
    print(" ___      _     _                 ")
    print("/ __| ___| |_ _(_)_ _  __ _       ")
    print("\__ \/ _ \ \ V / | ' \/ _` |_ _ _ ")
    print("|___/\___/_|\_/|_|_||_\__, (_|_|_)")
    print("                    |___/       ")
    print()

def asciiFound():
    print("___                 _ _ ")
    print("| __|__ _  _ _ _  __| | |")
    print("| _/ _ \ || | ' \/ _` |_|")
    print("|_|\___/\_,_|_||_\__,_(_)")
    print("Persoalan dapat diselesaikan")
    print()

def asciiNotFound():
    print(" _  _     _     ___                 _ _ ")
    print("| \| |___| |_  | __|__ _  _ _ _  __| | |")
    print("| .` / _ \  _| | _/ _ \ || | ' \/ _` |_|")
    print("|_|\_\___/\__| |_|\___/\_,_|_||_\__,_(_)")
    print("Persoalan tidak bisa diselesaikan")
    print()

def asciiFailedToSolve():
    print("   ___                  ")
    print("  / _ \ _ __ _ __ ______")
    print(" | (_) | '_ \ '_ (_-<_-<")
    print("  \___/| .__/ .__/__/__/")
    print("       |_|  |_|         ")
    print("You've waited more than 30 minutes!")
    print("Try again or Try another puzzle")
    print()