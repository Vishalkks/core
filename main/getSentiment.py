import os

from Constants import directories
from files import saveJSONObject


def extractSentiment(file):
	print file
	sentFile = open(file)
	sentDict = dict()
	for line in sentFile.readlines():
		li = line.split('\t')
		word, sent, val = li
		val = int(val.split('\n')[0])
		print word, sent, val

		if word not in sentDict:
			sentDict[word] = dict()
			sentDict[word]['none'] = 1
		if val == 1:
			sentDict[word][sent] = 1
			sentDict[word].pop('none', None)

	return sentDict

sentiment = extractSentiment(directories.SENTIMENT_DIR)
saveJSONObject(sentiment, directories.SENTIMENT)
print sentiment
