import os
from nltk.probability import FreqDist

from core.main.Util.files import getGenrePath, saveObject, writeToLog, removeExtension

from core.main.Constants import directories


def createMatrix(genres, path, logfile):

	genreMatrix = dict()
	songMatrix = dict()
	numTokens = dict()
	numSongs = dict()
	for genre in genres:
		print 'GENRE:', genre
		genreMatrix[genre] = []
		songMatrix[genre] = dict()
		allWords = []

		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			genreWords = []
			for file in files:
				song = open(dirpath + "/" + file)
				print file
				words = []
				for line in song.readlines():
					words = line.split(' ')
					if removeExtension(file) in songMatrix[genre]:
						writeToLog(logfile, "Duplicate:" + file)
					else:
						songMatrix[genre][removeExtension(file)] = FreqDist(words)
				genreWords += words

			allWords += genreWords
			genreMatrix[genre] = FreqDist(genreWords)
			numTokens[genre] = len(genreWords)
			numSongs[genre] = len(files)

		allFreqs = FreqDist(allWords)

	return genreMatrix, songMatrix, allFreqs, numTokens, numSongs


logfile = open(directories.LOG_PATH, 'w+')
genres = os.listdir(directories.LYRICS_DIR)

print 'TRAIN'
genreTrainFreqs, songTrainFreqs, allTrainFreqs, numTokensTrain, numSongsTrain = createMatrix(genres, directories.TRAIN_PATH, logfile)
print 'VAL'
genreValFreqs, songValFreqs, allValFreqs, numTokensVal, numSongsVal = createMatrix(genres, directories.VAL_PATH, logfile)
print 'TEST'
genreTestFreqs, songTestFreqs, allTestFreqs, numTokensTest, numSongsTest = createMatrix(genres, directories.TEST_PATH, logfile)


saveObject(genreTrainFreqs, directories.GENRE_TRAIN_FREQS)
saveObject(genreValFreqs, directories.GENRE_VAL_FREQS)
saveObject(genreTestFreqs, directories.GENRE_TEST_FREQS)
saveObject(songTrainFreqs, directories.SONG_TRAIN_FREQS)
saveObject(songValFreqs, directories.SONG_VAL_FREQS)
saveObject(songTestFreqs, directories.SONG_TEST_FREQS)
saveObject(allTrainFreqs, directories.ALL_TRAIN_FREQS)
saveObject(allValFreqs, directories.ALL_VAL_FREQS)
saveObject(allTestFreqs, directories.ALL_TEST_FREQS)
