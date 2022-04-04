from typing import NamedTuple
from numpy import *
from queue import PriorityQueue
import time

from helperFunction import *
from displayAscii import *

class mastrixStruct(NamedTuple):
    cost: int
    nodeNumber: int
    notInResult: int
    matriksPuzzle: matrix
    depth: int
    path: list

def KurangI(matrix):
    value = 0
    for i in range (0,4):
        for j in range (0,4):
            if((matrix[i][j] == 16) and (i % 2 == 0) and (j % 2 == 1)):
                value = value + 1
            elif ((matrix[i][j] == 16) and (i % 2 == 1) and (j % 2 == 0)):
                value = value + 1
            value = value + findLower(matrix, i, j)
    if(value % 2 == 0):
        return True
    else:
        return False

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

def solvePuzzle(puzzlenya):
    q = PriorityQueue()
    node = 1
    path = list()
    path.append(puzzlenya)

    puzzleMatrix = mastrixStruct(sumOfNotMatch(puzzlenya), (node * -1), sumOfNotMatch(puzzlenya), puzzlenya, 0, path)

    answer = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    visited = []
    inQueue = []

    q.put(puzzleMatrix)
    inQueue.append(puzzleMatrix.matriksPuzzle)
    start_time = time.time()
    found = True

    while not q.empty():
        end_timeNow = time.time()
        timeNeeded = end_timeNow - start_time
        if(timeNeeded > 1800):
            found = False
            break

        current = q.get()

        if current.matriksPuzzle not in visited:
            visited.append(current.matriksPuzzle)

            if(current.matriksPuzzle == answer):
                break
            else:
                row, col = findIndexOfElmnt(current.matriksPuzzle, 16)

                if(row > 0):
                    node = node + 1
                    newMatrix = moveUp(current.matriksPuzzle, row, col)
                    cost = current.depth + 1 + sumOfNotMatch(newMatrix)
                    newPath = current.path.copy()
                    newPath.append(newMatrix)
                    newMatrixStruct = mastrixStruct(cost, (node * -1), sumOfNotMatch(newMatrix), newMatrix, current.depth + 1, newPath)
                    if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                        q.put(newMatrixStruct)
                        inQueue.append(newMatrixStruct.matriksPuzzle)
                if(row < 3):
                    node = node + 1
                    newMatrix = moveDown(current.matriksPuzzle, row, col)
                    cost = current.depth + 1 + sumOfNotMatch(newMatrix)
                    newPath = current.path.copy()
                    newPath.append(newMatrix)
                    newMatrixStruct = mastrixStruct(cost, (node * -1), sumOfNotMatch(newMatrix), newMatrix, current.depth + 1, newPath)
                    if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                        q.put(newMatrixStruct)
                        inQueue.append(newMatrixStruct.matriksPuzzle)
                if(col > 0):
                    node = node + 1
                    newMatrix = moveLeft(current.matriksPuzzle, row, col)
                    cost = current.depth + 1 + sumOfNotMatch(newMatrix)
                    newPath = current.path.copy()
                    newPath.append(newMatrix)
                    newMatrixStruct = mastrixStruct(cost, (node * -1), sumOfNotMatch(newMatrix), newMatrix, current.depth + 1, newPath)
                    if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                        q.put(newMatrixStruct)
                        inQueue.append(newMatrixStruct.matriksPuzzle)
                if(col < 3):
                    node = node + 1
                    newMatrix = moveRight(current.matriksPuzzle, row, col)
                    cost = current.depth + 1 + sumOfNotMatch(newMatrix)
                    newPath = current.path.copy()
                    newPath.append(newMatrix)
                    newMatrixStruct = mastrixStruct(cost, (node * -1), sumOfNotMatch(newMatrix), newMatrix, current.depth + 1, newPath)
                    if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                        q.put(newMatrixStruct)
                        inQueue.append(newMatrixStruct.matriksPuzzle)

    end_time = time.time()
    timeNeeded = end_time - start_time

    if(found == True):
        asciiFound()
        kurangItiapUbin(puzzlenya)
        printKurangIValue(puzzlenya)
        printUrutanMatrix(current.path)
    else:
        asciiFailedToSolve();
        kurangItiapUbin(puzzlenya)
        printKurangIValue(puzzlenya)

    return timeNeeded, node, current.path