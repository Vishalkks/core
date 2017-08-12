import os
from nltk.probability import FreqDist

from core.main.Util.files import getGenrePath, saveObject, writeToLog, removeExtension

from core.main.Constants import directories


def createMatrix(genres, path, logfile):

	genreFreqs = dict()
	genreSongs = dict()
	numTokens = dict()
	numSongs = dict()
	for genre in genres:
		print 'GENRE:', genre
		genreFreqs[genre] = []
		genreSongs[genre] = dict()
		allWords = []

		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			genreWords = []
			for file in files:
				song = open(dirpath + "/" + file)
				print file
				words = []
				for line in song.readlines():
					words = line.split(' ')
					if removeExtension(file) in genreSongs[genre]:
						writeToLog(logfile, "Duplicate:" + file)
					else:
						genreSongs[genre][removeExtension(file)] = words
				genreWords += words

			allWords += genreWords
			genreFreqs[genre] = FreqDist(genreWords)
			numTokens[genre] = len(genreWords)
			numSongs[genre] = len(files)

		allFreqs = FreqDist(allWords)

	return genreFreqs, genreSongs, allFreqs, numTokens, numSongs


logfile = open(directories.LOG_PATH, 'w+')
genres = os.listdir(directories.LYRICS_DIR)

genreFreqsTrain, genreSongsTrain, allFreqsTrain, numTokensTrain, numSongsTrain = createMatrix(genres, directories.TRAIN_PATH, logfile)
genreFreqsVal, genreSongsVal, allFreqsVal, numTokensVal, numSongsVal = createMatrix(genres, directories.VAL_PATH, logfile)
genreFreqsTest, genreSongsTest, allFreqsTest, numTokensTest, numSongsTest = createMatrix(genres, directories.TEST_PATH, logfile)


saveObject(genreFreqsTrain, directories.GENRE_FREQS_TRAIN)
saveObject(genreFreqsVal, directories.GENRE_FREQS_VAL)
saveObject(genreFreqsTest, directories.GENRE_FREQS_TEST)
saveObject(genreSongsTrain, directories.GENRE_SONGS_TRAIN)
saveObject(genreSongsVal, directories.GENRE_SONGS_VAL)
saveObject(genreSongsTest, directories.GENRE_SONGS_TEST)
saveObject(allFreqsTrain, directories.ALL_FREQS_TRAIN)
saveObject(allFreqsVal, directories.ALL_FREQS_VAL)
saveObject(allFreqsTest, directories.ALL_FREQS_TEST)
