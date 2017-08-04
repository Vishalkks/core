import os
import pickle


def getGenrePath(dir, genre):
	return dir + '/' + genre


def saveObject(obj, filename):
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def getObject(filename):
	with open(filename, 'rb') as fp:
		return pickle.load(fp)


def create(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath, 0777)
		os.chmod(filepath, 0777)


def write_to_log(logfile, message):
	logfile.write(message)
