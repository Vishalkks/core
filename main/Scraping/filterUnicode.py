import os

from Constants import directories
from files import getGenrePath
from stringUtil import is_ascii, is_asciiList


def filter(genres, path):
	asc, uni, err = 0, 0, 0
	for genre in genres:
		print genre
		genPath = getGenrePath(path, genre)
		for dirpath, dirnames, files in os.walk(genPath):
			for album in dirnames:
				albPath = genPath + "/" + album
				for di, dn, songs in os.walk(albPath):
					for song in songs:
						#print albPath + "/" + song
						print song
						try:
							lyr = open(dirpath + "/" + file)
							words = []
							for line in lyr.readlines():
								words += line.split(' ')

							if not is_asciiList(words):
								uni += 1
							else:
								asc += 1
						except:
							err += 1

	print asc, uni, err
	print float(uni)/float(asc)*100, "%"

lyrics = directories.LYRICS_DIR
genres = os.listdir(lyrics)

filter(genres, lyrics)