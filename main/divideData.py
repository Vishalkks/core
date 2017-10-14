import os.path
import random
from shutil import copyfile

from core.main.Constants import directories
from core.main.Util.files import getGenrePath, create, writeToLog

#divides the dataset into training, validation, and testing.


def moveFiles(li, path, logfile):
	for lyr in li:
		print lyr
		try:
			copyfile(lyr, path + '/' + lyr.split('/')[-1])
		except IOError:
			writeToLog(logfile, "Could not write:" + lyr +"\n")


def splitFiles(genres, logfile):
	for genre in genres:
		print genre
		lyrics = []

		genTrain = getGenrePath(directories.PATH_TRAIN, genre)
		genTest = getGenrePath(directories.PATH_TEST, genre)
		genVal = getGenrePath(directories.PATH_VAL, genre)
		artists = getGenrePath(directories.LYRICS_DIR, genre)

		print 'here'
		create(genTrain)
		create(genTest)
		create(genVal)

		print 'here2'
		for dirpath, dirnames, files in os.walk(artists):
			for file in files:
				lyrics.append(dirpath + '/' + file)

		random.shuffle(lyrics)
		train = lyrics[:int(len(lyrics)*0.6)]
		test = lyrics[int(len(lyrics)*0.6):int(len(lyrics)*0.8)]
		val = lyrics[int(len(lyrics)*0.8):]

		print 'here3'
		moveFiles(train, genTrain, logfile)
		print '\tdone'
		moveFiles(test, genTest, logfile)
		print '\tdone'
		moveFiles(val, genVal, logfile)
		print '\tdone'

genres = os.listdir(directories.LYRICS_DIR)
logfile = open(directories.LOG_PATH, 'w+')

create(directories.PATH_TRAIN)
create(directories.PATH_TEST)
create(directories.PATH_VAL)

splitFiles(genres, logfile)