import gc

import itertools
from nltk import ngrams, FreqDist

from core.main.Constants.values import GENRES
from core.main.Util.files import getJSONObject, saveJSONObject, getJSONObjectCodec

'''
def saveNGramDists(lyricStore, bigramStoreTotality, trigramStoreTotality):
	for genre in GENRES:
		print 'GENRE:', genre
		lyrics = getJSONObject(lyricStore[genre])
		bigrams = []
		trigrams = []
		for song, words in lyrics.items():
			bigrams += list(ngrams(words, 2))
			trigrams += list(ngrams(words, 3))

		bigramDist = FreqDist(bigrams)
		saveJSONObject(bigramDist, bigramStoreTotality[genre])

		trigramDist = FreqDist(trigrams)
		saveJSONObject(trigramDist, trigramStoreTotality[genre])
'''

'''
def saveNGramDists(lyricStore, bigramStoreTotality, trigramStoreTotality):
	for genre in GENRES:
		print 'GENRE:', genre
		lyrics = getJSONObject(lyricStore[genre])
		bigrams = []
		trigrams = []
		for song, words in lyrics.items():
			bigrams += list(ngrams(words, 2))
			#print [w for w in words]
			#print [type(w) for w in words]
			#print [b for b in bigrams]
			#print [type(b) for b in bigrams]
			#print [(a[0], a[1]) for a in [b for b in bigrams]]
			#print [(type(a[0]), type(a[1])) for a in [b for b in bigrams]]
			#print '\n\n\n'

		bigramDist = FreqDist(bigrams)
		saveJSONObject(bigramDist, bigramStoreTotality[genre])

		for song, words in lyrics.items():
			trigrams += list(ngrams(words, 3))

		trigramDist = FreqDist(trigrams)
		saveJSONObject(trigramDist, trigramStoreTotality[genre])
'''


def saveNGramDistsBigrams(lyricStore, bigramStoreTotality):
	for genre in GENRES:
		saveNGramDistsBigramsGenre(lyricStore, bigramStoreTotality, genre)


def saveNGramDistsBigramsGenre(lyricStore, bigramStoreTotality, genre):
	gc.collect()
	print 'GENRE:', genre
	lyrics = getJSONObject(lyricStore[genre])
	bigrams = []
	for song, words in lyrics.items():
		bigrams += map(lambda b: unicode(b), list(ngrams(words, 2)))

	#bigrams = map(lambda b: unicode(b), bigrams)
	#bigramDist = FreqDist(bigrams)
	saveJSONObject(FreqDist(bigrams), bigramStoreTotality[genre])


def saveNGramDistsTrigrams(lyricStore, trigramStoreTotality):
	for genre in GENRES:
		saveNGramDistsTrigramsGenre(lyricStore, trigramStoreTotality, genre)


def saveNGramDistsTrigramsGenre(lyricStore, trigramStoreTotality, genre):
	gc.collect()
	print 'GENRE:', genre
	lyrics = getJSONObject(lyricStore[genre])

	trigrams = list(itertools.chain.from_iterable(map(lambda (song, words): map(lambda t: unicode(t), ngrams(words, 3)), lyrics.items())))

	saveJSONObject(FreqDist(trigrams), trigramStoreTotality[genre])



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


def getNGramFreqs(lyricsStore, bigramStoreTotality, trigramStoreTotality, bigramFreqsStore, trigramFreqsStore):
	for genre in GENRES:
		print(genre)
		getNGramFreqsGenre(lyricsStore, bigramStoreTotality, trigramStoreTotality, bigramFreqsStore, trigramFreqsStore, genre)


def getNGramFreqsGenre(lyricsStore, bigramStoreTotality, trigramStoreTotality, bigramFreqsStore, trigramFreqsStore, genreToStore):
	bigramFrequencies = {}
	trigramFrequencies = {}
	lyrics = getJSONObject(lyricsStore[genreToStore])
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
				if unicode(bigram) in bigramStoreTotalityObj:
					bigramFrequencies[song][GENRES.index(genre)] += bigramStoreTotalityObj[unicode(bigram)]

			for trigram in trigrams:
				if unicode(trigram) in trigramStoreTotalityObj:
					trigramFrequencies[song][GENRES.index(genre)] += trigramStoreTotalityObj[unicode(trigram)]

	print(bigramFrequencies, trigramFrequencies)
	saveJSONObject(bigramFrequencies, bigramFreqsStore[genreToStore])
	saveJSONObject(trigramFrequencies, trigramFreqsStore[genreToStore])
