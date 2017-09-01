import matplotlib.pyplot as plt
import pylab

from Constants import directories
from files import getJSONObject

numSongs = getJSONObject(directories.NUM_SONGS_TRAIN)
genreFreqsTrain = getJSONObject(directories.GENRE_FREQS_TRAIN)


#print map(lambda x:x[0], sorted(numSongs.items()))
#print map(lambda x:x[1], sorted(numSongs.items()))
#print map(lambda x:x[0], sorted([(g,len(genreFreqsTrain[g])) for g in genreFreqsTrain.keys()]))
#print map(lambda x:x[1], sorted([(g,len(genreFreqsTrain[g])) for g in genreFreqsTrain.keys()]))

songs = map(lambda x:x[1], sorted(numSongs.items()))
data = map(lambda x:x[1], sorted([(g,len(genreFreqsTrain[g])) for g in genreFreqsTrain.keys()]))
plt.plot(songs, data, 'ro')
plt.xlabel('songs')
plt.ylabel('data')
plt.show()