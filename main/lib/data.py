import os
import traceback

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


def createLyricsObjects(path, lyricstore, bigramStoreTotality, trigramStoreTotality):
	for genre in GENRES:
		createGenreLyricsObject(path, lyricstore, bigramStoreTotality, trigramStoreTotality, genre)

'''
def createGenreLyricsObject(path, lyricStore, bigramStoreTotality, trigramStoreTotality, genre):
	lyricObj = dict()
	print 'GENRE:', genre
	#bigrams = []
	#trigrams = []
	norm = 0
	err = 0
	for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
		for file in files:
			song = open(dirpath + "/" + file)
			words = []
			for line in song.readlines():
				words += line.split(' ')
			try:
				norm += 1
				words = [w.encode('utf8') for w in words]
				lyricObj[file] = words
			except:
				err += 1
			song.close()

	print 'norm', norm
	print 'err', err
	saveJSONObject(lyricObj, lyricStore[genre])
'''

def createGenreLyricsObject(path, lyricStore, bigramStoreTotality, trigramStoreTotality, genre):
	lyricObj = dict()
	print 'GENRE:', genre
	allWords = []
	for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
		for file in files:
			song = open(dirpath + "/" + file)
			words = []
			for line in song.readlines():
				words += line.split(' ')
			lyricObj[file] = words
			allWords += words
			#print words
			song.close()

	bigramWords = ngrams(allWords, 2)
	trigramWords = ngrams(allWords, 2)
	saveJSONObject(lyricObj, lyricStore[genre])
	saveJSONObject(bigramWords, bigramStoreTotality[genre])
	saveJSONObject(trigramWords, trigramStoreTotality[genre])


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
