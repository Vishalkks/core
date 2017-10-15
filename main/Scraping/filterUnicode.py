import os

from Constants import directories
from Constants.values import GENRES
from files import getGenrePath
from stringUtil import is_asciiList


def perform_filter(songs, path, uni, asc, err):
	for song in songs:
		#print song
		try:
			lyr = open(path + "/" + song)
			words = []
			for line in lyr.readlines():
				words += line.split(' ')

			if not is_asciiList(words):
				uni += 1
				print path + "/" + song
				print words
				os.remove(path + "/" + song)
			else:
				asc += 1
		except:
			err += 1
	return asc, uni, err


def filter(path, divided=False):
	asc, uni, err = 0, 0, 0
	for genre in GENRES:
		print genre
		genPath = getGenrePath(path, genre)
		for dirpath, dirnames, songs in os.walk(genPath):
			if divided:
				asc, uni, err = perform_filter(songs, dirpath, uni, asc, err)
			else:
				for album in dirnames:
					albPath = genPath + "/" + album
					for di, dn, songs in os.walk(albPath):
						asc, uni, err = perform_filter(songs, albPath, uni, asc, err)

	print asc, uni, err
	if asc != 0:
		print float(uni)/float(asc)*100, "%"
	else:
		print 'divide/0'

lyrics = directories.LYRICS_DIR

#filter(lyrics, divided=False)
filter(directories.PATH_TRAIN, divided=True)
filter(directories.PATH_TEST, divided=True)
filter(directories.PATH_VAL, divided=True)