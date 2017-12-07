from Constants import directories
from Constants.values import GENRES
from Util.files import getLyrics, create, partitionFiles
from lib.data import createLyricsObjects
from lib.ngrams import saveNgramDists, getCountsEachSong


lyricsDir = directories.LYRIC_PATH
lyricsStore = directories.LYRICS_STORE
bigramTotality = directories.BIGRAMS_TOTALITY
trigramTotality = directories.TRIGRAMS_TOTALITY
bigramFreqs = directories.BIGRAMS_FREQS
trigramFreqs = directories.TRIGRAMS_FREQS
#bigramSongDict = directories.BIGRAMS_SONG_STORE
#trigramSongDict = directories.TRIGRAMS_SONG_STORE


#for key in ['train', 'val', 'test']:
	#for genre in GENRES:
		#create(lyricsStore[key][genre])
		#create(bigramTotality[key][genre])
		#create(trigramTotality[key][genre])

#partitionFiles(lyricsDir, directories.PATH_TRAIN, directories.PATH_VAL, directories.PATH_TEST, directories.LOG_PATH)

for key in ['train', 'val', 'test']:
	#createLyricsObjects(lyricsDir[key], lyricsStore[key], bigramTotality[key], trigramTotality[key])
	#saveNgramDists(lyricsStore[key], bigramTotality[key], trigramTotality[key])
	getCountsEachSong(lyricsStore[key], bigramFreqs[key],trigramFreqs[key])
