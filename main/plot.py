import matplotlib.pyplot as plt
import math

from Constants import directories
from files import getJSONObject
from helper import printMatrix

numSongs = getJSONObject(directories.NUM_SONGS_TRAIN)
genreFreqsTrain = getJSONObject(directories.GENRE_FREQS_TRAIN)
results = getJSONObject(directories.RESULTS)

printMatrix(results, directories.MATRIX_OUTPUT)

columns = map(lambda x:x[1], sorted([(g,sum([results[genre][g] for genre in results.keys()])) for g in results.keys()]))
data = map(lambda x:x[1], sorted([(g,len(genreFreqsTrain[g])) for g in genreFreqsTrain.keys()]))

matrixSum = sum(columns)

print columns
columns = [math.log(c) for c in columns]
print data

plt.plot(data, columns, 'ro')
plt.xlabel('amount of data')
plt.ylabel('log number of times classified')
plt.show()