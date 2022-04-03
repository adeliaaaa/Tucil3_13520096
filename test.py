# from queue import PriorityQueue
# from typing import NamedTuple

# from numpy import matrix
# from helperFunction import readMyFile


# class mastrixStruct(NamedTuple):
#     cost: int
#     matriksPuzzle: matrix
#     depth: int
#     haveParent: bool
#     parent: matrix


# visited = []
# matriksnya = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# matriksnya2 = [[15,6,3,4], [5,2,7,8], [9,13,11,12], [10,14,1,16]]
# matriksnya3 = [[8,11,3,4], [5,6,7,1], [9,10,2,12], [13,14,15,16]]
# matriksnya4 = [[5,2,3,4], [1,6,15,8], [9,10,11,12], [13,14,7,16]]
# matriksnya5 = [[11,2,3,4], [15,6,7,8], [9,10,1,12], [13,14,5,16]]

# visited.append(matriksnya)
# visited.append(matriksnya2)

# if matriksnya2 in visited:
#     print("Sudah ada")
# else:
#     print("Belum ada")

# q = PriorityQueue()

# matriksss = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# puzzleMatrix = mastrixStruct(15, [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 100-3, False, None)
# puzzleMatrix2 = mastrixStruct(2, [[15,9,3,16], [5,6,13,8], [12,10,11,2], [7,14,1,4]], 100-3, False, None)
# puzzleMatrix3 = mastrixStruct(40, [[4,2,3,12], [5,16,7,8], [9,10,15,1], [13,14,11,6]], 100-5, False, None)
# puzzleMatrix4 = mastrixStruct(8, [[7,16,12,4], [5,6,1,8], [15,10,11,3], [13,14,9,2]], 100-3, False, None)
# puzzleMatrix5 = mastrixStruct(15, [[16,9,3,13], [5,6,7,10], [2,8,11,12], [4,14,15,1]], 100-5, False, None)

# q.put(puzzleMatrix)
# q.put(puzzleMatrix2)
# q.put(puzzleMatrix3)
# q.put(puzzleMatrix4)
# q.put(puzzleMatrix5)

# while not q.empty():
#     current = q.get()
#     print(current.matriksPuzzle, current.cost, current.depth)

import tkinter as tk


window = tk.Tk()