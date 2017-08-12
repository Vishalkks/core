from Constants import directories
from files import getObject


def getAggregate(numSongs):
	return sum(numSongs.values())


def genreProb(genre):
	numSongs = getObject(directories.NUM_SONGS_TRAIN)
	return numSongs[genre]/getAggregate(numSongs)


def tokenProb(token, genre):
	allTrainFreqs = getObject(directories.ALL_TRAIN_FREQS)
	genreTrainFreqs = getObject(directories.GENRE_TRAIN_FREQS)

	return genreTrainFreqs[genre][token]/allTrainFreqs[token]