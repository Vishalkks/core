from Constants import directories, values
from Constants.values import NUM_SENTS, SENT_NUMBER
from files import getJSONObject


def newSentDict():
	sentDict = dict()
	for sent in values.SENTS:
		sentDict[sent] = 0
	return sentDict


def getSentimentCount(words):
	sentCount = newSentDict()
	sentiment = getJSONObject(directories.SENTIMENT)

	for word in words:
		if word in sentiment:
			for sent in sentiment[word]:
				sentCount[sent] += 1

	return sentCount


def getSentimentVector(words):
	sentVec = [0]*NUM_SENTS
	sentiment = getJSONObject(directories.SENTIMENT)

	for word in words:
		if word in sentiment:
			for sent in sentiment[word]:
				sentVec[SENT_NUMBER[sent]] += 1

	return sentVec


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
			sentDict[word] = []
			sentDict[word].append('none')
		if val == 1:
			if 'none' in sentDict[word]:
				sentDict[word].remove('none')
			sentDict[word].append(sent)

	return sentDict

