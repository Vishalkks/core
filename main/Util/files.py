import os
import cPickle as pickle
import ujson as json
#import simplejson as json

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
		json.dump(obj, output, ensure_ascii=False)


def getPKLObject(filename):
	with open(filename, 'rb') as fp:
		return pickle.load(fp)


@timer
def getJSONObject(filename):
	with open(filename, 'rb') as fp:
		return json.load(fp)


def removeExtension(string):
	return ".".join(string.split('.')[:-1])


def create(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath, 0777)
		os.chmod(filepath, 0777)


def writeToLog(logfile, message):
	logfile.write(message)


def withoutRock(genres):
	return [g for g in genres if g != 'Rock']



