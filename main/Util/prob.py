from Constants import directories
from files import getObject
from timing import timer


def numTokensAll(freqdist):
	return sum(numTokens(freqdist, genre) for genre in freqdist)


def numTokens(freqdist, genre):
	return sum(freqdist[genre].values())


def getAggregate(numSongs):
	return sum(numSongs.values())


def genreProb(genre, numSongs):
	return float(numSongs[genre]/getAggregate(numSongs))


def tokenProb(token, genre, genreTrainFreqs, allTrainFreqs):
	if token in genreTrainFreqs[genre]:
		print token
		print '\tgen', token in genreTrainFreqs[genre]
		print '\tall', token in allTrainFreqs
		return float(genreTrainFreqs[genre][token]/allTrainFreqs[token])
	else:
		return 0.0


def songProb(songWords, genre, genreTrainFreqs, allTrainFreqs):
	return sum([tokenProb(token, genre, genreTrainFreqs, allTrainFreqs) for token in songWords])


def MNBProb(songWords, genre, numSongs, genreTrainFreqs, allTrainFreqs):
	return songProb(songWords, genre, genreTrainFreqs, allTrainFreqs)*genreProb(genre, numSongs)


#@timer
def classifyGenre(songWords, genres, numSongs, genreTrainFreqs, allTrainFreqs):
	return max([(g, 1 + MNBProb(songWords, g, numSongs, genreTrainFreqs, allTrainFreqs)) for g in genres], key=lambda x: x[1])[0]
