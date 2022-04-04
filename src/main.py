from numpy import *

from mainFunction import *
from helperFunction import *
from displayAscii import *

asciiGameName()
puzzlenya = insertFile()
asciiSolvingPuzzle()


if(KurangI(puzzlenya)):
    print("Matrix posisi awal: ")
    printMatrix(puzzlenya)
    timeNeeded, node, path = solvePuzzle(puzzlenya)

    print("Waktu eksekusi: ", timeNeeded, " detik")
    print("Jumlah node yang dibangkitkan: ", node)
else:
    asciiNotFound()
    print("Matrix posisi awal: ")
    printMatrix(puzzlenya)
    kurangItiapUbin(puzzlenya)
    printKurangIValue(puzzlenya)