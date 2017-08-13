import time

from core.main.Constants import directories

from core.main.Util.files import getObject, saveObject
from prob import classifyGenre


def createResultMatrix(genres):
	matrix = dict()
	for genre in genres:
		matrix[genre] = dict()
		for compGenre in genres:
			matrix[genre][compGenre] = 0
	return matrix


def classify(genreSongs, results, numSongs, genreFreqsTrain, allFreqsTrain):
	for genreName in genreSongs:
		print 'GENRE:', genreName
		genre = genreSongs[genreName]
		for song in genre:
			songWords = genre[song]
			print song, len(songWords)
			pred = classifyGenre(songWords, genreSongs.keys(), numSongs, genreFreqsTrain, allFreqsTrain)
			#print 'genre', genreName
			#print 'pred', pred
			#print 'res', results[genreName][pred]
			results[genreName][pred] += 1
	return results

genreSongsTrain = getObject(directories.GENRE_SONGS_TRAIN)
genreSongsVal = getObject(directories.GENRE_SONGS_VAL)
numSongs = getObject(directories.NUM_SONGS_TRAIN)
genreFreqsTrain = getObject(directories.GENRE_FREQS_TRAIN)
allFreqsTrain = getObject(directories.ALL_FREQS_TRAIN)

#print genreSongsVal.keys()

results = classify(genreSongsVal, createResultMatrix(genreSongsTrain.keys()), numSongs, genreFreqsTrain, allFreqsTrain)
saveObject(results, directories.RESULTS)

print results
