import os

from nltk import FreqDist

from Constants.values import GENRES
from files import getGenrePath, saveJSONObject


def getFrequencies(path):
	genreFreqs = dict()
	numSongs = dict()
	allWords = []
	for genre in GENRES:
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



def createLyricsObjects(path, store):
	lyricDict = dict()
	for genre in GENRES:
		createGenreLyricsObject(path, store, genre)


def createGenreLyricsObject(path, lyricStore, genre):
	lyricObj = dict()
	print 'GENRE:', genre
	for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
		for file in files:
			song = open(dirpath + "/" + file)
			words = []
			for line in song.readlines():
				words += line.split(' ')
			lyricObj[file] = words
			#print words
			song.close()

	saveJSONObject(lyricObj, lyricStore[genre])


def getWords(wordFile):
	words = open(wordFile)
	#words = codecs.open(wordFile, encoding='utf-8')

	wordSet = set()

	for line in words.readlines():
		#print repr(line)

		word = line.split('\n')[0]
		#print word

		wordSet.add(word)

	#print wordSet
	return wordSet
