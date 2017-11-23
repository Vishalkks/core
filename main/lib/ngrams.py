from nltk import ngrams, FreqDist

from Constants.values import GENRES
from Util.files import getJSONObject, saveJSONObject, getJSONObjectCodec


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
