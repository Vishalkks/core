from Constants import directories
from Constants.values import GENRES
from lib.data import createLyricsObjects, saveLyricsAndNGramDists, createLyricsObjectGenre
from lib.ngrams import saveNGramDistsBigrams, saveNGramDistsTrigrams, getNGramFreqsGenre, \
	saveNGramDistsTrigramsGenre, saveNGramDistsBigramsGenre, getNGramFreqs

lyricsDir = directories.LYRIC_PATH
lyricsStore = directories.LYRICS_STORE
bigramTotality = directories.BIGRAMS_TOTALITY
trigramTotality = directories.TRIGRAMS_TOTALITY
bigramFreqs = directories.BIGRAMS_FREQS
trigramFreqs = directories.TRIGRAMS_FREQS
#partitionFiles(lyricsDir, directories.PATH_TRAIN, directories.PATH_VAL, directories.PATH_TEST, directories.LOG_PATH)


for key in ['train', 'val', 'test']:
	for genre in GENRES[GENRES.index('Hip_Hop'):]:
		#createLyricsObjectGenre(lyricsDir[key], lyricsStore[key], genre)
		saveNGramDistsTrigramsGenre(lyricsStore[key], trigramTotality[key], genre)
		#saveNGramDistsBigramsGenre(lyricsStore[key], bigramTotality[key], genre)
	#getNGramFreqs(lyricsStore[key], bigramTotality[key], trigramTotality[key], bigramFreqs[key], trigramFreqs[key])
