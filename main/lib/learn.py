import os
import numpy as np
from nltk import FreqDist

from Constants import values
from Constants.values import GENRES
from core.main.Util.files import getGenrePath, getJSONObject
from lib.sentiment import getSentimentVector, getSentimentCount
from lib.spanish import countLangWords
from core.main.Util.prob import classifyGenreSong
from core.main.Util.timing import timer


def getLineIndices(words):
	return [index for index, word in enumerate(words) if '\n' in word]


def getAvgLineLen(indices):
	return [indices[0]] + [x - indices[i-1] for i,x in enumerate(indices)][1:]


def getAvgWordLen(words, length):
	if length == 0:
		return length

	return sum([len(word) for word in words])/length


def createFeatureMatrix(spanishWords, germanWords, frenchWords, path, lyricStore):
	features, labels = [], []

	for genre in GENRES:
		print 'GENRE:', genre
		lyrics = getJSONObject(lyricStore[genre])
		for song, words in lyrics.items():

			length = len(words)
			avgLen = getAvgWordLen(words, length)
			titleLen = len(song.split(" "))
			sentVec = getSentimentVector(words)
			numSpanish = countLangWords(words, spanishWords)
			numGerman = countLangWords(words, germanWords)
			numFrench = countLangWords(words, frenchWords)
			#bigrams = getBigramCounts(words)
			#trigrams = getTrigramCounts(words)

			indices = getLineIndices(words)
			lines = len(indices)
			avgLineLength = getAvgLineLen(indices)
			row = [length, lines, avgLineLength, avgLen, titleLen, numSpanish, numGerman, numFrench]
			row += sentVec
			features.append(row)
			labels.append(values.GEN_NUMBER[genre])

	return np.array(features, dtype=float), np.array(labels, dtype=float)


def _createFeatureMatrix(spanishWords, germanWords, frenchWords, path):
	features, labels = [], []

	for genre in GENRES:
		print 'GENRE:', genre
		for dirpath, dirnames, files in os.walk(getGenrePath(path, genre)):
			for file in files:
				song = open(dirpath + "/" + file)
				words = []
				lineLengths = []
				lines = 0
				for line in song.readlines():
					words += line.split(' ')
					lineLengths.append(len(words))
					lines += 1

				length = len(words)
				avgLen = getAvgWordLen(words, length)

				if lines != 0:
					avgLineLength = sum([lineLen for lineLen in lineLengths])/lines
				else:
					avgLineLength = 0
				titleLen = len(file.split(" "))
				sentVec = getSentimentVector(words)
				numSpanish = countLangWords(words, spanishWords)
				numGerman = countLangWords(words, germanWords)
				numFrench = countLangWords(words, frenchWords)
				row = [length, lines, avgLineLength, avgLen, titleLen, numSpanish, numGerman, numFrench]
				row += sentVec
				features.append(row)
				labels.append(values.GEN_NUMBER[genre])
				print file, len(words)
				print words

	return np.array(features, dtype=float), np.array(labels, dtype=float)


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