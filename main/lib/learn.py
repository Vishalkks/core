import os
import numpy as np
from nltk import FreqDist

from Constants import values
from Constants.values import GENRES
from files import getGenrePath
from lib.sentiment import getSentimentVector, getSentimentCount
from prob import classifyGenreSong
from timing import timer


def createFeatureMatrix(path):
	print path
	print os.getcwd()
	print os.path.abspath(path)
	print os.listdir(path)
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
				if length != 0:
					avgLen = sum([len(word) for word in words])/length
				else:
					avgLen = 0
				if lines != 0:
					avgLineLength = sum([lineLen for lineLen in lineLengths])/lines
				else:
					avgLineLength = 0
				titleLen = len(file.split(" "))
				sentVec = getSentimentVector(words)

				row = [length, lines, avgLineLength, avgLen, titleLen]
				row += sentVec
				features.append(row)
				labels.append(values.GEN_NUMBER[genre])
				print file, len(words)

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


def evaluateFrequencies(path):
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


def createResultMatrix():
	matrix = dict()
	for genre in GENRES:
		matrix[genre] = dict()
		for compGenre in GENRES:
			matrix[genre][compGenre] = 0
	return matrix