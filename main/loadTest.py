from Constants import directories
from files import getJSONObject
from helper import printMatrix
from metrics import printAllPrecisions, printAllRecalls

results = getJSONObject(directories.RESULTS)
printMatrix(results, directories.MATRIX_OUTPUT)

printAllPrecisions(results)
printAllRecalls(results)