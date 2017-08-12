import os
from nltk.probability import FreqDist

from core.main.Util.util import getGenrePath, saveObject, write_to_log

from core.main.Constants import directories
from core.main.Util.strings import remove_extension


def create_matrix(genres, path, logfile):
	allMatrix = dict()
	songMatrix = dict()
	for genre in genres:
		print 'GENRE:', genre
		genDir = getGenrePath(path, genre)
		allMatrix[genre] = []
		songMatrix[genre] = dict()
		for dirpath, dirnames, files in os.walk(genDir):
			genreWords = []
			for file in files:
				song = open(dirpath + "/" + file)
				print file
				words = []
				for line in song.readlines():
					words = line.split(' ')
					if remove_extension(file) in songMatrix[genre]:
						write_to_log(logfile, "Duplicate:" + file)
					else:
						songMatrix[genre][remove_extension(file)] = FreqDist(words)
				genreWords += words

			allMatrix[genre].append(FreqDist(genreWords))

	return allMatrix, songMatrix


logfile = open(directories.LOG_PATH, 'w+')

genres = os.listdir(directories.LYRICS_DIR)
print 'TRAIN'
allTrainFreqs, songTrainFreqs = create_matrix(genres, directories.TRAIN_PATH, logfile)
print 'VAL'
allValFreqs, songValFreqs = create_matrix(genres, directories.VAL_PATH, logfile)
print 'TEST'
allTestFreqs, songTestFreqs = create_matrix(genres, directories.TEST_PATH, logfile)

saveObject(allTrainFreqs, directories.TRAIN_FREQS)
saveObject(allValFreqs, directories.VAL_FREQS)
saveObject(allTestFreqs, directories.TEST_FREQS)
saveObject(songTrainFreqs, directories.TRAIN_FREQS)
saveObject(songValFreqs, directories.VAL_FREQS)
saveObject(songTestFreqs, directories.TEST_FREQS)
