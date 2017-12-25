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
