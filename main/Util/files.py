import codecs
import os
import cPickle as pickle
import random
import nltk
from nltk import ngrams
import json
#import ujson as json
#import simplejson as json
from shutil import copyfile

from Constants.values import GENRES
from timing import timer


def getGenrePath(dir, genre):
	return dir + '/' + genre


def savePKLObject(obj, filename):
	print 'saving...'
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def saveJSONObject(obj, filename):
	print 'saving...'
	print filename
	with open(filename, 'wb') as output:
		json.dump(obj, output, indent=4, sort_keys=True)
	output.close()


def getPKLObject(filename):
	with open(filename, 'rb') as fp:
		return pickle.load(fp)


#@timer
def getJSONObject(filename):
	with open(filename, 'rb') as fp:
		return json.load(fp)


def getJSONObjectCodec(filename):
	with codecs.open(filename, 'rb', encoding='utf8') as fp:
		return json.load(fp)


def removeExtension(string):
	return ".".join(string.split('.')[:-1])


def createDir(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath, 0777)
		os.chmod(filepath, 0777)


def writeToLog(logfile, message):
	log = open(logfile, 'a+')
	log.write(message)


def withoutRock():
	return [g for g in GENRES if g != 'Rock']


def moveFiles(li, path, logfile):
	norm = 0
	err = 0
	for lyr in li:
		#print 'lyr', lyr
		try:
			copyfile(lyr, path + '/' + lyr.split('/')[-1])
			norm += 1
		except IOError:
			writeToLog(logfile, "Could not write:" + lyr +"\n")
			err += 1

	print 'norm', norm
	print 'err', err


def partitionFiles(originalDir, trainDir, valDir, testDir, logfile):
	for genre in GENRES:
		print genre
		lyrics = []

		genTrain = getGenrePath(trainDir, genre)
		genTest = getGenrePath(testDir, genre)
		genVal = getGenrePath(valDir, genre)
		artists = getGenrePath(originalDir, genre)

		#print 'here'
		createDir(genTrain)
		createDir(genTest)
		createDir(genVal)

		#print 'here2'
		for dirpath, dirnames, files in os.walk(artists):
			for file in files:
				lyrics.append(dirpath + '/' + file)

		random.shuffle(lyrics)
		train = lyrics[:int(len(lyrics)*0.6)]
		test = lyrics[int(len(lyrics)*0.6):int(len(lyrics)*0.8)]
		val = lyrics[int(len(lyrics)*0.8):]

		#print 'here3'
		moveFiles(train, genTrain, logfile)
		#print '\tdone'
		moveFiles(test, genTest, logfile)
		#print '\tdone'
		moveFiles(val, genVal, logfile)
		#print '\tdone'


def getLyrics(originalDir, lyricStore, bigramStoreTotality, trigramStoreTotality):
	for genre in GENRES:
		print 'GENRE:', genre
		getLyricsGenre(originalDir, lyricStore, bigramStoreTotality, trigramStoreTotality, genre)


def flattened(list_of_lists):
	return [val for sublist in list_of_lists for val in sublist]


def getLyricsGenre(originalDir, lyricStore, bigramStoreTotality, trigramStoreTotality, genre):
	lyricsDict = dict()
	bigramSongDict = dict()
	trigramSongDict = dict()
	songs = dict()
	lyricsObject = dict()
	allLyrics = dict()
	bigramTotality = dict()
	trigramTotality = dict()
	bigramSongs = dict()
	trigramSongs = dict()
	datatypes = ['train', 'val', 'test']
	allSongs = []

	artists = getGenrePath(originalDir, genre)
	normcount = 0
	errorcount = 0
	#print artists
	for dirpath, dirnames, files in os.walk(artists):
		for file in files:
			#print dirpath, file
			try:
				songtext = open(dirpath + '/' + file)
				allSongs.append(file)

				words = []
				for line in songtext.readlines():
					words += line.split(' ')
				#print words
				lyricsDict[file] = words
				#bigramSongDict[songname] = ngrams(words, 2)
				#trigramSongDict[songname] = ngrams(words, 3)
				file.close()
				normcount += 1
			except:
				errorcount += 1

	print 'normcount', normcount
	print 'errorcount', errorcount
	random.shuffle(allSongs)

	songs['train'] = allSongs[:int(len(allSongs) * 0.6)]
	songs['val'] = allSongs[int(len(allSongs) * 0.6):int(len(allSongs) * 0.8)]
	songs['test'] = allSongs[int(len(allSongs) * 0.8):]

	for key in datatypes:
		lyricsObject[key] = {song: lyricsDict[song] for song in songs[key]}
		saveJSONObject(lyricsObject[key], lyricStore[key][genre])

		allLyrics[key] = flattened(lyricsObject[key].values())
		bigramTotality[key] = ngrams(allLyrics[key], 2)
		saveJSONObject(bigramTotality[key], bigramStoreTotality[key[genre]])

		trigramTotality[key] = ngrams(allLyrics[key], 3)
		saveJSONObject(trigramTotality[key], trigramStoreTotality[key][genre])

		#bigramSongs[key] = {song: bigramSongDict[song] for song in songs[key]}
		#trigramSongs[key] = {song: trigramSongDict[song] for song in songs[key]}

		#saveJSONObject(bigramSongs[key], bigramStoreSong[key][genre])
		#saveJSONObject(trigramSongs[key], trigramStoreSong[key][genre])