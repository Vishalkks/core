from nltk import ngrams, FreqDist

from core.main.Constants.values import GENRES
from core.main.Util.files import getJSONObject, saveJSONObject, getJSONObjectCodec


def saveNgramDists(lyricStore, bigramStoreTotality, trigramStoreTotality):
	for genre in GENRES:
		saveNgramDistsGenre(lyricStore, bigramStoreTotality, trigramStoreTotality, genre)


def saveNgramDistsGenre(lyricStore, bigramStoreTotality, trigramStoreTotality, genre):
	print 'GENRE:', genre
	lyrics = getJSONObjectCodec(lyricStore[genre])
	bigrams = []
	trigrams = []
	for song, words in lyrics.items():
		bigrams += list(ngrams(words, 2))
		#trigrams += list(ngrams(words, 3))

	bigramDist = FreqDist(bigrams)
	#trigramDist = FreqDist(trigrams)

	saveJSONObject(bigramDist, bigramStoreTotality[genre])
	#saveJSONObject(trigramDist, trigramStoreTotality[genre])

def getFrequenciesGenre(words,bigramStoreTotality,trigramStoreTotality):
	bigrams = list(ngrams(words,2))
	trigrams = list(ngrams(words,3))

	frequencyVecBigrams = [0]*len(GENRES)
	frequencyVecTrigrams = [0] * len(GENRES)
	for genre in GENRES:
		bigramStoreTotalityObj = getJSONObject(bigramStoreTotality[genre])
		for bigram in bigrams:
			if bigram in bigramStoreTotalityObj:
				frequencyVecBigrams[GENRES.index(genre)] += bigramStoreTotalityObj[bigram]

		trigramStoreTotalityObj = getJSONObject(trigramStoreTotality[genre])
		for trigram in trigrams:
			if trigram in trigramStoreTotalityObj:
				frequencyVecTrigrams[GENRES.index(genre)] += trigramStoreTotalityObj[trigram]

	return frequencyVecBigrams,frequencyVecTrigrams

'''
def getCountsEachSong(lyricStore, bigramStoreFreqs, trigramStoreFreqs):
	for genre in GENRES:
		print 'GENRE:', genre
		lyrics = getJSONObjectCodec(lyricStore[genre])
		bigramCounts = {}
		trigramCounts = {}
		for song, words in lyrics.items():
			bigrams = FreqDist(list(ngrams(words, 2)))
			trigrams = FreqDist(list(ngrams(words, 3)))
			bigramCounts[song] = bigrams
			trigramCounts[song] = trigrams
		print(bigramCounts)
		saveJSONObject(bigramCounts, bigramStoreFreqs[genre])
		saveJSONObject(trigramCounts, trigramStoreFreqs[genre])
'''

def getFreqsByGenre(lyricsStore,bigramStoreTotality,trigramStoreTotality,bigramFreqsStore,trigramFreqsStore):
	for genre in GENRES:
		songCountsBigram = {}
		songCountsTrigram = {}
		lyrics = getJSONObject(lyricsStore[genre])
		print(len(lyrics.items()))
		for song, words in lyrics.items():
			freqBigrams, freqTrigrams = getFrequenciesGenre(words, bigramStoreTotality, trigramStoreTotality)
			songCountsBigram[song] = freqBigrams
			songCountsTrigram[song] = freqTrigrams
		print(songCountsBigram,songCountsTrigram)
		saveJSONObject(songCountsBigram,bigramFreqsStore[genre])
		saveJSONObject(songCountsTrigram,trigramFreqsStore[genre])



