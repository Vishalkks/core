import matplotlib.pyplot as plt
import math

from Constants import directories
from files import getJSONObject
from printing import printMatrix

genreFreqsTrain = getJSONObject(directories.GENRE_FREQS_TRAIN)
results = getJSONObject(directories.RESULTS)

columns = map(lambda x:x[1], sorted([(g,sum([results[genre][g] for genre in results.keys()])) for g in results.keys()]))
columns = [math.log(c) for c in columns]
data = map(lambda x:x[1], sorted([(g,len(genreFreqsTrain[g])) for g in genreFreqsTrain.keys()]))
matrixSum = sum(columns)

printMatrix(results, directories.MATRIX_OUTPUT)
print data

plt.plot(data, columns, 'ro')
plt.xlabel('amount of data')
plt.ylabel('log number of times classified')
plt.show()
