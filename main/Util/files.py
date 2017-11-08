import os
import cPickle as pickle
#import ujson as json
import simplejson as json
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
	with open(filename, 'wb') as output:
		json.dump(obj, output, indent=4, sort_keys=True)


def getPKLObject(filename):
	with open(filename, 'rb') as fp:
		return pickle.load(fp)


#@timer
def getJSONObject(filename):
	with open(filename, 'rb') as fp:
		print filename
		return json.load(fp, ensure)


def removeExtension(string):
	return ".".join(string.split('.')[:-1])


def create(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath, 0777)
		os.chmod(filepath, 0777)


def writeToLog(logfile, message):
	logfile.write(message)


def withoutRock():
	return [g for g in GENRES if g != 'Rock']


def moveFiles(li, path, logfile):
	for lyr in li:
		print lyr
		try:
			copyfile(lyr, path + '/' + lyr.split('/')[-1])
		except IOError:
			writeToLog(logfile, "Could not write:" + lyr +"\n")


def partitionFiles(trainDir, testDir, valDir, originalDir, logfile):
	for genre in GENRES:
		print genre
		lyrics = []

		genTrain = getGenrePath(trainDir, genre)
		genTest = getGenrePath(testDir, genre)
		genVal = getGenrePath(valDir, genre)
		artists = getGenrePath(originalDir, genre)

		#print 'here'
		create(genTrain)
		create(genTest)
		create(genVal)

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
