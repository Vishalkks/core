import os
from nltk.probability import FreqDist

from core.main.Util.files import getGenrePath, saveObject, removeExtension, withoutRock

from core.main.Constants import directories


def extractData(genres, path):

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
				print file
				song = open(dirpath + "/" + file)
				for line in song.readlines():
					words = line.split(' ')
					genreSongs[genre][removeExtension(file)] = words
					genreWords += words
					allWords += words

			genreFreqs[genre] = FreqDist(genreWords)
			numSongs[genre] = len(files)

		allFreqs = FreqDist(allWords)

	return genreFreqs, genreSongs, allFreqs, numSongs


logfile = open(directories.LOG_PATH, 'w+')
genres = os.listdir(directories.LYRICS_DIR)


genreFreqsTrain, genreSongsTrain, allFreqsTrain, numSongsTrain = extractData(genres, directories.PATH_TRAIN)
genreFreqsVal, genreSongsVal, allFreqsVal, numSongsVal = extractData(genres, directories.PATH_VAL)
genreFreqsTest, genreSongsTest, allFreqsTest, numSongsTest = extractData(genres, directories.PATH_TEST)


saveObject(genreFreqsTrain, directories.GENRE_FREQS_TRAIN)
saveObject(genreFreqsVal, directories.GENRE_FREQS_VAL)
saveObject(genreFreqsTest, directories.GENRE_FREQS_TEST)
saveObject(genreSongsTrain, directories.GENRE_SONGS_TRAIN)
saveObject(genreSongsVal, directories.GENRE_SONGS_VAL)
saveObject(genreSongsTest, directories.GENRE_SONGS_TEST)
saveObject(allFreqsTrain, directories.ALL_FREQS_TRAIN)
saveObject(allFreqsVal, directories.ALL_FREQS_VAL)
saveObject(allFreqsTest, directories.ALL_FREQS_TEST)
saveObject(numSongsTrain, directories.NUM_SONGS_TRAIN)
saveObject(numSongsVal, directories.NUM_SONGS_VAL)
saveObject(numSongsTest, directories.NUM_SONGS_TEST)
