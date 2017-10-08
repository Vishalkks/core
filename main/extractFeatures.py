from gevent import os

from Constants import directories
from files import getJSONObject, getGenrePath


def classify(path, genres, results, numSongs, genreFreqsTrain, allFreqsTrain):
	for genre in genres:
		print 'GENRE:', genre
		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			for file in files:
				song = open(dirpath + "/" + file)
				words = []
				lineLengths = []
				for line in song.readlines():
					words += line.split(' ')
					lineLengths += len(words)
					for word in words:
						x=1
				length = len(words)
				avgLen = sum([len(word) for word in words])/len(words)
				lines = len(song.readlines())
				avgLineLength = sum([lineLen for lineLen in lineLengths])/len(lineLengths)

				print file, len(words)
	return results

numSongs = getJSONObject(directories.NUM_SONGS_TRAIN)
genreFreqsTrain = getJSONObject(directories.GENRE_FREQS_TRAIN)
allFreqsTrain = getJSONObject(directories.ALL_FREQS_TRAIN)

genres = os.listdir(directories.LYRICS_DIR)
path = directories.PATH_VAL

results = classify(path, genres, createResultMatrix(genres), numSongs, genreFreqsTrain, allFreqsTrain)
