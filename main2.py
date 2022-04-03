from typing import NamedTuple
from numpy import *
from queue import PriorityQueue
import time

from helperFunction import *

class mastrixStruct(NamedTuple):
    cost: int
    matriksPuzzle: matrix
    depth: int
    haveParent: bool
    parent: matrix

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

q = PriorityQueue()
fileName = "move30.txt"

puzzleMatrix = mastrixStruct(0, readMyFile(fileName), 0, False, None)
answer = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
visited = []
inQueue = []

q.put(puzzleMatrix)
inQueue.append(puzzleMatrix.matriksPuzzle)

start_time = time.time()
while not q.empty():
    # print(q.qsize())
    current = q.get()
    print(current.matriksPuzzle, current.cost, current.depth)

    if current.matriksPuzzle not in visited:
        visited.append(current.matriksPuzzle)

        if(current.matriksPuzzle == answer):
            print("Found")
            break
        else:
            row, col = findIndexOfElmnt(current.matriksPuzzle, 16)

            if(row > 0):
                newMatrix = moveUp(current.matriksPuzzle, row, col)
                cost = (current.depth * -1) + sumOfNotMatch(newMatrix)
                newMatrixStruct = mastrixStruct(cost, newMatrix, ((current.depth + 1) * -1), True, current.matriksPuzzle)
                if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                    q.put(newMatrixStruct)
                    inQueue.append(newMatrixStruct.matriksPuzzle)
            if(row < 3):
                newMatrix = moveDown(current.matriksPuzzle, row, col)
                cost = (current.depth * -1) + sumOfNotMatch(newMatrix)
                newMatrixStruct = mastrixStruct(cost, newMatrix, ((current.depth + 1) * -1), True, current.matriksPuzzle)
                if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                    q.put(newMatrixStruct)
                    inQueue.append(newMatrixStruct.matriksPuzzle)
            if(col > 0):
                newMatrix = moveLeft(current.matriksPuzzle, row, col)
                cost = (current.depth * -1) + sumOfNotMatch(newMatrix)
                newMatrixStruct = mastrixStruct(cost, newMatrix, ((current.depth + 1) * -1), True, current.matriksPuzzle)
                if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                    q.put(newMatrixStruct)
                    inQueue.append(newMatrixStruct.matriksPuzzle)
            if(col < 3):
                newMatrix = moveRight(current.matriksPuzzle, row, col)
                cost = (current.depth * -1) + sumOfNotMatch(newMatrix)
                newMatrixStruct = mastrixStruct(cost, newMatrix, ((current.depth + 1) * -1), True, current.matriksPuzzle)
                if (newMatrixStruct.matriksPuzzle not in visited) and (newMatrixStruct.matriksPuzzle not in inQueue):
                    q.put(newMatrixStruct)
                    inQueue.append(newMatrixStruct.matriksPuzzle)

end_time = time.time()
print(current.matriksPuzzle)
print("Time: ", end_time - start_time)

# sigmaKurangI = KurangI(puzzleMatrix.matriksPuzzle)
# print(sigmaKurangI)
