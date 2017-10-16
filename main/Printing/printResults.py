from Constants import directories
from files import getJSONObject
from printing import printMatrix
from lib.metrics import printAllPrecisions, printAllRecalls

confMatrix = getJSONObject(directories.CONFUSION_MATRIX)
printMatrix(confMatrix, directories.MATRIX_OUTPUT)

printAllPrecisions(confMatrix)
printAllRecalls(confMatrix)