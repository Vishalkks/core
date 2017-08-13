from Constants import directories
from files import getObject


def numTokensAll(freqdist):
	return sum(numTokens(freqdist, genre) for genre in freqdist)


def numTokens(freqdist, genre):
	return sum(freqdist[genre].values())


def getAggregate(numSongs):
	return sum(numSongs.values())


def genreProb(genre):
	numSongs = getObject(directories.NUM_SONGS_TRAIN)
	return float(numSongs[genre]/getAggregate(numSongs))


def tokenProb(token, genre):
	allTrainFreqs = getObject(directories.ALL_FREQS_TRAIN)
	genreTrainFreqs = getObject(directories.GENRE_FREQS_TRAIN)

	return float(genreTrainFreqs[genre][token]/allTrainFreqs[token])


def songProb(songWords, genre):
	return sum([tokenProb(token, genre) for token in songWords])

def MNBProb(songWords, genre):
	return songProb(songWords, genre)*genreProb(genre)


def classifyGenre(songWords, genres):
	return max([(g, 1 + MNBProb(songWords, g)) for g in genres], key=lambda x: x[1])[0]
