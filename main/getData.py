import os
import sys
from nltk.probability import FreqDist

from core.main.Util.files import getGenrePath, saveJSONObject, create

from core.main.Constants import directories


def extractData(genres, path):
	genreFreqs = dict()
	numSongs = dict()
	allWords = []
	for genre in genres:
		print 'GENRE:', genre
		genreFreqs[genre] = []
		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			genreWords = []

			for file in files:
				print file
				song = open(dirpath + "/" + file)
				words = []
				for line in song.readlines():
					words += line.split(' ')
				genreWords += words
				allWords += words

			genreFreqs[genre] = FreqDist(genreWords)
			numSongs[genre] = len(files)

	allFreqs = FreqDist(allWords)

	return genreFreqs, allFreqs, numSongs

sys.setrecursionlimit(10000)

logfile = open(directories.LOG_PATH, 'w+')
genres = os.listdir(directories.LYRICS_DIR)

x=1
saveJSONObject(x, 'x.json')

create(directories.PICKLE_DIR)
genreFreqsTrain, allFreqsTrain, numSongsTrain = extractData(genres, directories.PATH_TRAIN)
saveJSONObject(numSongsTrain, directories.NUM_SONGS_TRAIN)
saveJSONObject(allFreqsTrain, directories.ALL_FREQS_TRAIN)
saveJSONObject(genreFreqsTrain, directories.GENRE_FREQS_TRAIN)

genreFreqsVal, allFreqsVal, numSongsVal = extractData(genres, directories.PATH_VAL)
saveJSONObject(genreFreqsVal, directories.GENRE_FREQS_VAL)
saveJSONObject(allFreqsVal, directories.ALL_FREQS_VAL)
saveJSONObject(numSongsVal, directories.NUM_SONGS_VAL)

genreFreqsTest, allFreqsTest, numSongsTest = extractData(genres, directories.PATH_TEST)
saveJSONObject(genreFreqsTest, directories.GENRE_FREQS_TEST)
saveJSONObject(allFreqsTest, directories.ALL_FREQS_TEST)
saveJSONObject(numSongsTest, directories.NUM_SONGS_TEST)

print 'done'
