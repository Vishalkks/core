import os

from Constants import directories
from Constants.values import GENRES
from files import getGenrePath
from stringUtil import is_asciiList


def apply_filter(songs, path, uni, asc, err, filter):
	for song in songs:
		#print song
		try:
			lyr = open(path + "/" + song)
			words = []
			for line in lyr.readlines():
				words += line.split(' ')

			if filter(words):
				asc += 1
			else:
				uni += 1
				print path + "/" + song
				print words
				os.remove(path + "/" + song)

		except:
			err += 1
	return asc, uni, err


def filterData(path, filter, divided=False):
	asc, uni, err = 0, 0, 0
	for genre in GENRES:
		print genre
		genPath = getGenrePath(path, genre)
		for dirpath, dirnames, songs in os.walk(genPath):
			if divided:
				asc, uni, err = apply_filter(songs, dirpath, uni, asc, err, filter)
			else:
				for album in dirnames:
					albPath = genPath + "/" + album
					for di, dn, songs in os.walk(albPath):
						asc, uni, err = apply_filter(songs, albPath, uni, asc, err, filter)

	print asc, uni, err
	if asc != 0:
		print float(uni)/float(asc)*100, "%"
	else:
		print 'divide/0'

lyrics = directories.LYRICS_DIR

filterData(lyrics, divided=False)
filterData(directories.PATH_TRAIN, is_asciiList, divided=True)
filterData(directories.PATH_TEST, is_asciiList, divided=True)
filterData(directories.PATH_VAL, is_asciiList, divided=True)

