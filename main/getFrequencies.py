import os
from nltk.probability import FreqDist

from core.main.Util.util import getGenrePath, saveObject

from core.main.Constants import directories


def create_matrix(genres, path):
	matrix = dict()
	for genre in genres:
		genDir = getGenrePath(path, genre)
		matrix[genre] = []
		for dirpath, dirnames, files in os.walk(genDir):
			genreWords = []
			for file in files:
				song = open(dirpath + "/" + file)
				print file
				words = []
				for line in song.readlines():
					words += line.split(' ')
				genreWords += words

			matrix[genre].append(FreqDist(genreWords))

	return matrix


genres = os.listdir(directories.LYRICS_DIR)
trainFreqs = create_matrix(genres, directories.TRAIN_PATH)
valFreqs = create_matrix(genres, directories.VAL_PATH)
testFreqs = create_matrix(genres, directories.TEST_PATH)

saveObject(trainFreqs, directories.TRAIN_FREQS)
saveObject(valFreqs, directories.VAL_FREQS)
saveObject(testFreqs, directories.TEST_FREQS)
