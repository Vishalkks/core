from Constants import directories
from files import getJSONObject
from printing import printMatrix
from lib.metrics import printAllPrecisions, printAllRecalls

results = getJSONObject(directories.RESULTS)
printMatrix(results, directories.MATRIX_OUTPUT)

printAllPrecisions(results)
printAllRecalls(results)