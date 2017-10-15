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
			#sentDict[word]['none'] = 1
			sentDict[word].append('none')
		if val == 1:
			#sentDict[word][sent] = 1
			#sentDict[word].pop('none', None)
			if 'none' in sentDict[word]:
				sentDict[word].remove('none')
			sentDict[word].append(sent)

	return sentDict
