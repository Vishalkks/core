import math
def numTokensAll(freqdist):
	return sum(numTokens(freqdist, genre) for genre in freqdist)


def numTokens(freqdist, genre):
	return sum(freqdist[genre].values())


def getAggregate(numSongs):
	return sum(numSongs.values())


def genreProb(genre, numSongs):
	return float(numSongs[genre]/getAggregate(numSongs))


def tokenProb(token, genre, genreFreqsTrain, allFreqsTrain):
	if token in genreFreqsTrain[genre]:
		return math.log((float(genreFreqsTrain[genre][token]))/float(allFreqsTrain[token]))
	else:
		return 0.0


def songProb(songWords, genre, genreFreqsTrain, allFreqsTrain):
	return sum([tokenProb(token, genre, genreFreqsTrain, allFreqsTrain) for token in songWords])


def MNBProb(songWords, genre, numSongs, genreFreqsTrain, allFreqsTrain):
	return songProb(songWords, genre, genreFreqsTrain, allFreqsTrain)*genreProb(genre, numSongs)


def classifyGenre(songWords, genres, numSongs, genreFreqsTrain, allFreqsTrain):
	return max([(g, MNBProb(songWords, g, numSongs, genreFreqsTrain, allFreqsTrain)) for g in genres], key=lambda x: x[1])[0]
