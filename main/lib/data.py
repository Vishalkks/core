import os
import sys

from nltk import FreqDist, ngrams

from Constants.values import GENRES, GEN_NUMBER
from Util.files import getGenrePath, saveJSONObject, flattened


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


def createLyricsObjects(path, lyricstore):
	for genre in GENRES:
		createLyricsObjectGenre(path, lyricstore, genre)


def createLyricsObjectGenre(path, lyricStore, genre):
	sys.setrecursionlimit(100000)
	reload(sys)
	sys.setdefaultencoding('utf-8')
	lyricObj = dict()
	print 'GENRE:', genre
	norm = 0
	err = 0

	for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
		for file in files:
			try:
				song = open(dirpath + "/" + file)
				words = []
				for line in song.readlines():
					words += line.split(' ')
				words = [unicode(w, 'utf8') for w in words]
				lyricObj[file] = words
				norm += 1
				song.close()
			except:
				err += 1

	print 'norm', norm
	print 'err', err

	saveJSONObject(lyricObj, lyricStore[genre])


def saveLyricsAndNGramDists(path, lyricStore, bigramStoreTotality, trigramStoreTotality):
	sys.setrecursionlimit(100000)
	reload(sys)
	sys.setdefaultencoding('utf-8')
	for genre in GENRES:
		lyricObj = dict()
		print 'GENRE:', genre
		norm = 0
		err = 0
		bigrams = []
		trigrams = []

		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			for file in files:
				try:
					song = open(dirpath + "/" + file)
					words = []
					for line in song.readlines():
						words += line.split(' ')
					words = map(lambda w: unicode(w, 'utf8'), words)
					bigrams += list(ngrams(words, 2))
					trigrams += list(ngrams(words, 3))
					lyricObj[file] = words
					norm += 1
					song.close()
				except:
					err += 1

		print 'norm', norm
		print 'err', err

		saveJSONObject(lyricObj, lyricStore[genre])

		#bigrams = map(lambda b: unicode(b), bigrams)
		#bigramDist = dict(FreqDist(bigrams))
		#saveJSONObject(bigramDist, bigramStoreTotality[genre])
		saveJSONObject(dict(FreqDist(map(lambda b: unicode(b), bigrams))), bigramStoreTotality[genre])

		#trigrams = map(lambda t: unicode(t), trigrams)
		#trigramDist = dict(FreqDist(trigrams))
		#saveJSONObject(trigramDist, trigramStoreTotality[genre])
		saveJSONObject(dict(FreqDist(map(lambda t: unicode(t), trigrams))), trigramStoreTotality[genre])


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
