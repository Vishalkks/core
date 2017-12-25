from nltk import ngrams, FreqDist

from core.main.Constants.values import GENRES
from core.main.Util.files import getJSONObject, saveJSONObject, getJSONObjectCodec


def saveNGramDists(lyricStore, bigramStoreTotality, trigramStoreTotality):
	for genre in GENRES:
		print 'GENRE:', genre
		lyrics = getJSONObjectCodec(lyricStore[genre])
		bigrams = []
		trigrams = []
		for song, words in lyrics.items():
			bigrams += list(ngrams(words, 2))
			trigrams += list(ngrams(words, 3))

		bigramDist = FreqDist(bigrams)
		trigramDist = FreqDist(trigrams)

		saveJSONObject(bigramDist, bigramStoreTotality[genre])
		saveJSONObject(trigramDist, trigramStoreTotality[genre])


'''
def _getFrequenciesGenre(words,bigramStoreTotality,trigramStoreTotality):
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


def _getFreqsByGenre(lyricsStore,bigramStoreTotality,trigramStoreTotality,bigramFreqsStore,trigramFreqsStore):
	for genre in GENRES:
		songCountsBigram = {}
		songCountsTrigram = {}
		lyrics = getJSONObject(lyricsStore[genre])
		print(len(lyrics.items()))

		for song, words in lyrics.items():
			freqBigrams, freqTrigrams = _getFrequenciesGenre(words, bigramStoreTotality, trigramStoreTotality)
			songCountsBigram[song] = freqBigrams
			songCountsTrigram[song] = freqTrigrams
		print(songCountsBigram,songCountsTrigram)
		saveJSONObject(songCountsBigram,bigramFreqsStore[genre])
		saveJSONObject(songCountsTrigram,trigramFreqsStore[genre])
'''


def getFreqsByGenre(lyricsStore, bigramStoreTotality, trigramStoreTotality, bigramFreqsStore, trigramFreqsStore):
	for genre in GENRES:
		bigramFrequencies = {}
		trigramFrequencies = {}
		lyrics = getJSONObject(lyricsStore[genre])
		print(len(lyrics.items()))

		for genre in GENRES:
			bigramStoreTotalityObj = getJSONObject(bigramStoreTotality[genre])
			trigramStoreTotalityObj = getJSONObject(trigramStoreTotality[genre])

			for song, words in lyrics.items():
				if song not in bigramFrequencies:
					bigramFrequencies[song] = [0] * len(GENRES)

				if song not in trigramFrequencies:
					trigramFrequencies[song] = [0] * len(GENRES)

				bigrams = list(ngrams(words, 2))
				trigrams = list(ngrams(words, 3))

				for bigram in bigrams:
					if bigram in bigramStoreTotalityObj:
						bigramFrequencies[song][GENRES.index(genre)] += bigramStoreTotalityObj[bigram]

				for trigram in trigrams:
					if trigram in trigramStoreTotalityObj:
						trigramFrequencies[song][GENRES.index(genre)] += trigramStoreTotalityObj[trigram]

		print(bigramFrequencies, trigramFrequencies)
		saveJSONObject(bigramFrequencies, bigramFreqsStore[genre])
		saveJSONObject(trigramFrequencies, trigramFreqsStore[genre])
