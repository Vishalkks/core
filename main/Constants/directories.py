import os


def addRelPath(string):
	return '../../' + string

	#cwd = os.getcwd()
	#dir = cwd.split("\\")[-1].split('/')[-1]


	#if dir in ['main', 'test']:
	#	return '../../' + string
	#elif dir in ['Constants', 'Scraping', 'Util', 'lib', 'Printing']:
	#	return '../../../' + string
	#else:
	#	print 'Error for:', dir
	#'''

PATH_TRAIN = addRelPath('data/Lyrics/Training')
PATH_VAL = addRelPath('data/Lyrics/Validation')
PATH_TEST = addRelPath('data/Lyrics/Test')
LYRICS_DIR = addRelPath('data/Genre13')
LOG_PATH = addRelPath('data/log.txt')
PICKLE_DIR = addRelPath('data/objects')
SENTIMENT_FILE = addRelPath('data/NRC-Sentiment-Emotion-Lexicons/Lexicons/NRC-Emotion-Lexicon-v0.92/'
						'NRC-Emotion-Lexicon-Wordlevel-v0.92.txt')

ALL_FREQS_TRAIN = addRelPath('data/objects/allFreqsTrain.json')
ALL_FREQS_VAL = addRelPath('data/objects/allFreqsVal.json')
ALL_FREQS_TEST = addRelPath('data/objects/allFreqsTest.json')
GENRE_SONGS_TRAIN = addRelPath('data/objects/genreSongsTrain.json')
GENRE_SONGS_VAL = addRelPath('data/objects/genreSongsVal.json')
GENRE_SONGS_TEST = addRelPath('data/objects/genreSongsTest.json')
GENRE_FREQS_TRAIN = addRelPath('data/objects/genreFreqsTrain.json')
GENRE_FREQS_VAL = addRelPath('data/objects/genreFreqsVal.json')
GENRE_FREQS_TEST = addRelPath('data/objects/genreFreqsTest.json')
NUM_SONGS_TRAIN = addRelPath('data/objects/numSongsTrain.json')
NUM_SONGS_VAL = addRelPath('data/objects/numSongsVal.json')
NUM_SONGS_TEST = addRelPath('data/objects/numSongsTest.json')
RESULTS = addRelPath('data/objects/results.json')
SENTIMENT = addRelPath('data/objects/sentiment.json')

FEATURE_MATRIX = '../../data/objects/featureMatrix.json'
LABELS = '../../data/objects/labels.json'

MATRIX_OUTPUT = '../../data/output/confusionMatrix.txt'
PREC_OUTPUT = '../../data/output/precision.txt'
REC_OUTPUT = '../../data/output/recall.txt'