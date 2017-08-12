from Constants import directories
from files import getObject


def getAggregate(numSongs):
	return sum(numSongs.values())


def genreProb(genre):
	numSongs = getObject(directories.NUM_SONGS_TRAIN)
	return numSongs[genre]/getAggregate(numSongs)


def tokenProb(token, genre):
	allTrainFreqs = getObject(directories.ALL_FREQS_TRAIN)
	genreTrainFreqs = getObject(directories.GENRE_FREQS_TRAIN)

	return genreTrainFreqs[genre][token]/allTrainFreqs[token]