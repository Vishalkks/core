import os
from nltk.probability import FreqDist

from core.main.Util.files import getGenrePath, saveObject, removeExtension, withoutRock, create

from core.main.Constants import directories


def extractData(genres, path):

	genreFreqs = dict()
	genreSongs = dict()
	numTokens = dict()
	numSongs = dict()
	allWords = []
	for genre in genres:
		print 'GENRE:', genre
		genreFreqs[genre] = []
		genreSongs[genre] = dict()
		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			genreWords = []

			for file in files:
				print file
				song = open(dirpath + "/" + file)
				words = []
				for line in song.readlines():
					words += line.split(' ')
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
saveObject(genreFreqsTrain, directories.GENRE_FREQS_TRAIN)
saveObject(genreSongsTrain, directories.GENRE_SONGS_TRAIN)
saveObject(allFreqsTrain, directories.ALL_FREQS_TRAIN)
saveObject(numSongsTrain, directories.NUM_SONGS_TRAIN)

genreFreqsVal, genreSongsVal, allFreqsVal, numSongsVal = extractData(genres, directories.PATH_VAL)
saveObject(genreFreqsVal, directories.GENRE_FREQS_VAL)
saveObject(genreSongsVal, directories.GENRE_SONGS_VAL)
saveObject(allFreqsVal, directories.ALL_FREQS_VAL)
saveObject(numSongsVal, directories.NUM_SONGS_VAL)

genreFreqsTest, genreSongsTest, allFreqsTest, numSongsTest = extractData(genres, directories.PATH_TEST)
create(directories.PICKLE_DIR)
saveObject(genreFreqsTest, directories.GENRE_FREQS_TEST)
saveObject(genreSongsTest, directories.GENRE_SONGS_TEST)
saveObject(allFreqsTest, directories.ALL_FREQS_TEST)
saveObject(numSongsTest, directories.NUM_SONGS_TEST)

print 'done'
