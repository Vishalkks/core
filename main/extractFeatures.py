import numpy as np
import os


from Constants import directories, values
from files import getJSONObject, getGenrePath, saveJSONObject
from sentiment import getSentimentVector


def createFeatureMatrix(path, genres, numSongs, genreFreqsTrain, allFreqsTrain):
	features, labels = [], []
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
				length = len(words)
				avgLen = sum([len(word) for word in words])/len(words)
				lines = len(song.readlines())
				avgLineLength = sum([lineLen for lineLen in lineLengths])/len(lineLengths)
				sentVec = getSentimentVector(words)

				row = [length, lines, avgLineLength, avgLen]
				row += sentVec
				features.append(row)
				labels.append(values.GEN_NUMBER[genre])
				print file, len(words)

	return np.array(features), np.array(labels)

numSongs = getJSONObject(directories.NUM_SONGS_TRAIN)
genreFreqsTrain = getJSONObject(directories.GENRE_FREQS_TRAIN)
allFreqsTrain = getJSONObject(directories.ALL_FREQS_TRAIN)

genres = os.listdir(directories.LYRICS_DIR)
path = directories.PATH_VAL

features, labels = createFeatureMatrix(path, genres, numSongs, genreFreqsTrain, allFreqsTrain)
saveJSONObject(features, directories.FEATURE_MATRIX)
saveJSONObject(labels, directories.LABELS)