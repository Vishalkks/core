from Constants import directories, values
from files import getJSONObject


def newSentVector():
	sentDict = dict()
	for sent in values.SENTS:
		sentDict[sent] = 0
	return sentDict


def getSentimentVector(words):
	sentVec = newSentVector()
	sentiment = getJSONObject(directories.SENTIMENT)

	for word in words:
		for sent in sentiment[word]:
			sentVec[sent] += 1

	return sentVec
