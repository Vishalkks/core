from core.main.Constants import directories

from core.main.Util.files import getObject, saveObject
from prob import classifyGenre


def createResultMatrix(genres):
	matrix = dict()
	for genre in genres:
		matrix[genre] = dict()
		for genre in genres:
			matrix[genre] = 0
	return matrix


def classify(genreSongs, results):
	for genre in genreSongs:
		print 'GENRE:', genre
		genre = genreSongs[genre]
		for song in genre:
			print song
			songWords = genre[song]
			pred = classifyGenre(songWords, genreSongs.keys())
			results[genre][pred] += 1
	return results

genreSongsTrain = getObject(directories.GENRE_SONGS_TRAIN)
genreSongsVal = getObject(directories.GENRE_SONGS_VAL)

results = classify(genreSongsTrain, createResultMatrix(genreSongsTrain.keys()))
saveObject(results, directories.RESULTS)