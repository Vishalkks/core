import os

from core.main.Constants import directories

from core.main.Util.helper import printMatrix
from core.main.Util.prob import classifyGenre, classifyGenreSong
from files import getJSONObject, saveJSONObject, getGenrePath
from metrics import printAllRecalls, printAllPrecisions
from timing import timer


def createResultMatrix(genres):
	matrix = dict()
	for genre in genres:
		matrix[genre] = dict()
		for compGenre in genres:
			matrix[genre][compGenre] = 0
	return matrix

@timer
def classify(path, genres, results, numSongs, genreFreqsTrain, allFreqsTrain):
	for genre in genres:
		print 'GENRE:', genre
		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			for file in files:
				song = open(dirpath + "/" + file)
				words = []
				for line in song.readlines():
					words += line.split(' ')
				songWords = words
				print file, len(songWords)
				#pred = classifyGenre(songWords, genres, numSongs, genreFreqsTrain, allFreqsTrain)
				pred = classifyGenreSong(songWords, genres, genreFreqsTrain, allFreqsTrain)
				results[genre][pred] += 1
	return results

numSongs = getJSONObject(directories.NUM_SONGS_TRAIN)
genreFreqsTrain = getJSONObject(directories.GENRE_FREQS_TRAIN)
allFreqsTrain = getJSONObject(directories.ALL_FREQS_TRAIN)

genres = os.listdir(directories.LYRICS_DIR)
path = directories.PATH_VAL

results = classify(path, genres, createResultMatrix(genres), numSongs, genreFreqsTrain, allFreqsTrain)
saveJSONObject(results, directories.RESULTS)
printMatrix(results, directories.MATRIX_OUTPUT)

printAllPrecisions(results, directories.PREC_OUTPUT)
printAllRecalls(results, directories.REC_OUTPUT)
