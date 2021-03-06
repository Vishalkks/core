import os
import numpy as np
from nltk import FreqDist

from core.main.Constants import values
from core.main.Constants.values import GENRES
from core.main.Util.files import getGenrePath, getJSONObject
from core.main.lib.sentiment import getSentimentVector, getSentimentCount
from core.main.lib.spanish import countLangWords
from core.main.Util.prob import classifyGenreSong
from core.main.Util.timing import timer


def createFeatureMatrix(spanishWords, germanWords, frenchWords, path, lyricStore, bigramTotality, trigramTotality, bigramSongFreqs, trigramSongFreqs):
	#print path
	#print os.getcwd()
	#print os.path.abspath(path)
	#print os.listdir(path)
	features, labels = [], []
	for genre in GENRES:
		print 'GENRE:', genre
		lyrics = getJSONObject(lyricStore[genre])
		bigramSongFreqsPerGenre = getJSONObject(bigramSongFreqs[genre])
		trigramSongFreqsPerGenre = getJSONObject(trigramSongFreqs[genre])
		for song, words in lyrics.items():
			#song = open(dirpath + "/" + file)
			#words = []
			#lineLengths = []
			#lines = 0
			#for line in song.readlines():
				#words += line.split(' ')
				#lineLengths.append(len(words))
				#lines += 1

			length = len(words)
			if length != 0:
				avgLen = sum([len(word) for word in words])/length
			else:
				avgLen = 0
			#if length != 0:
				#avgLineLength = sum([lineLen for lineLen in lineLengths])/lines
			#else:
				#avgLineLength = 0
			titleLen = len(song.split(" "))
			sentVec = getSentimentVector(words)
			numSpanish = countLangWords(words, spanishWords)
			numGerman = countLangWords(words, germanWords)
			numFrench = countLangWords(words, frenchWords)
			freqBigrams,freqTrigrams = bigramSongFreqsPerGenre[song], trigramSongFreqsPerGenre[song]
			#row = [length, lines, avgLineLength, avgLen, titleLen, numSpanish, numGerman, numFrench]
			row = [length, avgLen, titleLen, numSpanish, numGerman, numFrench]
			row += sentVec
			row += freqBigrams
			row +=freqTrigrams
			features.append(row)
			labels.append(values.GEN_NUMBER[genre])
			#print song, len(words)
			#print words

	return features, labels


@timer
def classifyMNB(results, genreFreqsTrain, allFreqsTrain, path):
	for genre in GENRES:
		print 'GENRE:', genre
		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			for file in files:
				song = open(dirpath + "/" + file)
				words = []
				for line in song.readlines():
					words += line.split(' ')
				songWords = words
				print file, len(songWords)
				pred = classifyGenreSong(songWords, genreFreqsTrain, allFreqsTrain)
				results[genre][pred] += 1
	return results


def createResultMatrix():
	matrix = dict()
	for genre in GENRES:
		matrix[genre] = dict()
		for compGenre in GENRES:
			matrix[genre][compGenre] = 0
	return matrix