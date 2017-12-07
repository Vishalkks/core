import os

from core.main.Constants.values import GENRES

PATH_TRAIN = '../../data/Lyrics/Training'
PATH_VAL = '../../data/Lyrics/Validation'
PATH_TEST = '../../data/Lyrics/Test'

LYRIC_PATH = {'train': PATH_TRAIN, 'val': PATH_VAL, 'test': PATH_TEST}

LYRICS_DIR = '../../data/Genre13'
LOG_PATH = '../../data/log.txt'
PICKLE_DIR = '../../data/objects'
SENTIMENT_FILE = '../../data/NRC-Sentiment-Emotion-Lexicons/Lexicons/NRC-Emotion-Lexicon-v0.92/' \
				 'NRC-Emotion-Lexicon-Wordlevel-v0.92.txt'
SPANISH_WORD_FILE = '../../data/espanol/espanol.txt'
GERMAN_WORD_FILE = '../../data/deutsch/deutsch.txt'
FRENCH_WORD_FILE = '../../data/francais/francais.txt'

SPANISH_WORD_SET = '../../data/objects/spanishWords.json'
GERMAN_WORD_SET = '../../data/objects/germanWords.json'
FRENCH_WORD_SET = '../../data/objects/frenchWords.json'

ALL_FREQS_TRAIN = '../../data/objects/allFreqsTrain.json'
ALL_FREQS_VAL = '../../data/objects/allFreqsVal.json'
ALL_FREQS_TEST = '../../data/objects/allFreqsTest.json'
GENRE_SONGS_TRAIN = '../../data/objects/genreSongsTrain.json'
GENRE_SONGS_VAL = '../../data/objects/genreSongsVal.json'
GENRE_SONGS_TEST = '../../data/objects/genreSongsTest.json'
GENRE_FREQS_TRAIN = '../../data/objects/genreFreqsTrain.json'
GENRE_FREQS_VAL = '../../data/objects/genreFreqsVal.json'
GENRE_FREQS_TEST = '../../data/objects/genreFreqsTest.json'
NUM_SONGS_TRAIN = '../../data/objects/numSongsTrain.json'
NUM_SONGS_VAL = '../../data/objects/numSongsVal.json'
NUM_SONGS_TEST = '../../data/objects/numSongsTest.json'
CONFUSION_MATRIX = '../../data/objects/confusionMatrix.json'
RESULTS = '../../data/objects/results.json'
SENTIMENT = '../../data/objects/sentiment.json'

FEATURE_MATRIX_TRAIN = '../../data/objects/featureMatrixTrain.json'
FEATURE_MATRIX_VAL = '../../data/objects/featureMatrixVal.json'
FEATURE_MATRIX_TEST = '../../data/objects/featureMatrixTest.json'
LABELS = '../../data/objects/labels.json'
LABELS_TRAIN = '../../data/objects/labelsTrain.json'
LABELS_VAL = '../../data/objects/labelsVal.json'
LABELS_TEST = '../../data/objects/labelsTest.json'

MATRIX_OUTPUT = '../../data/output/confusionMatrix.txt'
PREC_OUTPUT = '../../data/output/precision.txt'
REC_OUTPUT = '../../data/output/recall.txt'


def addGenre(string, genre):
	return string + '/' + genre + '.json'


LYRICS_STORE_DIR_TRAIN = '../../data/objects/lyrics/train'
LYRICS_STORE_DIR_VAL = '../../data/objects/lyrics/val'
LYRICS_STORE_DIR_TEST = '../../data/objects/lyrics/test'

LYRICS_STORE_TRAIN = {genre: addGenre(LYRICS_STORE_DIR_TRAIN, genre) for genre in GENRES}
LYRICS_STORE_VAL = {genre: addGenre(LYRICS_STORE_DIR_VAL, genre) for genre in GENRES}
LYRICS_STORE_TEST = {genre: addGenre(LYRICS_STORE_DIR_TEST, genre) for genre in GENRES}

LYRICS_STORE = {'train': LYRICS_STORE_TRAIN, 'val': LYRICS_STORE_VAL, 'test': LYRICS_STORE_TEST}

BIGRAMS_TOTALITY_DIR_TRAIN = '../../data/objects/ngrams/bigrams/totality/train'
BIGRAMS_TOTALITY_DIR_VAL = '../../data/objects/ngrams/bigrams/totality/val'
BIGRAMS_TOTALITY_DIR_TEST = '../../data/objects/ngrams/bigrams/totality/test'

BIGRAMS_TOTALITY_TRAIN = {genre: addGenre(BIGRAMS_TOTALITY_DIR_TRAIN, genre) for genre in GENRES}
BIGRAMS_TOTALITY_VAL = {genre: addGenre(BIGRAMS_TOTALITY_DIR_VAL, genre) for genre in GENRES}
BIGRAMS_TOTALITY_TEST = {genre: addGenre(BIGRAMS_TOTALITY_DIR_TEST, genre) for genre in GENRES}

BIGRAMS_TOTALITY = {'train': BIGRAMS_TOTALITY_TRAIN, 'val': BIGRAMS_TOTALITY_VAL, 'test': BIGRAMS_TOTALITY_TEST}

TRIGRAMS_TOTALITY_DIR_TRAIN = '../../data/objects/ngrams/trigrams/totality/train'
TRIGRAMS_TOTALITY_DIR_VAL = '../../data/objects/ngrams/trigrams/totality/val'
TRIGRAMS_TOTALITY_DIR_TEST = '../../data/objects/ngrams/trigrams/totality/test'

TRIGRAMS_TOTALITY_TRAIN = {genre: addGenre(TRIGRAMS_TOTALITY_DIR_TRAIN, genre) for genre in GENRES}
TRIGRAMS_TOTALITY_VAL = {genre: addGenre(TRIGRAMS_TOTALITY_DIR_VAL, genre) for genre in GENRES}
TRIGRAMS_TOTALITY_TEST = {genre: addGenre(TRIGRAMS_TOTALITY_DIR_TEST, genre) for genre in GENRES}

TRIGRAMS_TOTALITY = {'train': TRIGRAMS_TOTALITY_TRAIN, 'val': TRIGRAMS_TOTALITY_VAL, 'test': TRIGRAMS_TOTALITY_TEST}

BIGRAMS_SONG_FREQS_DIR_TRAIN = '../../data/objects/ngrams/bigrams/freqs/train'
BIGRAMS_SONG_FREQS_DIR_VAL = '../../data/objects/ngrams/bigrams/freqs/val'
BIGRAMS_SONG_FREQS_DIR_TEST = '../../data/objects/ngrams/bigrams/freqs/test'

'''
BIGRAMS_SONG_FREQS_TRAIN = {genre: addGenre(BIGRAMS_SONG_FREQS_DIR_TRAIN, genre) for genre in GENRES}
BIGRAMS_SONG_FREQS_VAL = {genre: addGenre(BIGRAMS_SONG_FREQS_DIR_VAL, genre) for genre in GENRES}
BIGRAMS_SONG_FREQS_TEST = {genre: addGenre(BIGRAMS_SONG_FREQS_DIR_TEST, genre) for genre in GENRES}
'''

BIGRAMS_FREQS = {'train': "../../data/objects/ngrams/bigrams/freqs/train.json", 'val': "../../data/objects/ngrams/bigrams/freqs/val.json", 'test': "../../data/objects/ngrams/bigrams/freqs/test.json"}

TRIGRAMS_SONG_FREQS_DIR_TRAIN = '../../data/objects/ngrams/trigrams/freqs/train'
TRIGRAMS_SONG_FREQS_DIR_VAL = '../../data/objects/ngrams/trigrams/freqs/val'
TRIGRAMS_SONG_FREQS_DIR_TEST = '../../data/objects/ngrams/trigrams/freqs/test'

'''
TRIGRAMS_SONG_FREQS_TRAIN = {genre: addGenre(TRIGRAMS_SONG_FREQS_DIR_TRAIN, genre) for genre in GENRES}
TRIGRAMS_SONG_FREQS_VAL = {genre: addGenre(TRIGRAMS_SONG_FREQS_DIR_VAL, genre) for genre in GENRES}
TRIGRAMS_SONG_FREQS_TEST = {genre: addGenre(TRIGRAMS_SONG_FREQS_DIR_TEST, genre) for genre in GENRES}
'''

TRIGRAMS_FREQS = {'train': "../../data/objects/ngrams/trigrams/freqs/train.json", 'val': "../../data/objects/ngrams/trigrams/freqs/val.json", 'test': "../../data/objects/ngrams/trigrams/freqs/test.json"}

BIGRAMS_SONG_STORE_DIR_TRAIN = '../../data/objects/ngrams/bigrams/songs/train'
BIGRAMS_SONG_STORE_DIR_VAL = '../../data/objects/ngrams/bigrams/songs/val'
BIGRAMS_SONG_STORE_DIR_TEST = '../../data/objects/ngrams/bigrams/songs/test'

BIGRAMS_SONG_STORE_TRAIN = {genre: addGenre(BIGRAMS_SONG_STORE_DIR_TRAIN, genre) for genre in GENRES}
BIGRAMS_SONG_STORE_VAL = {genre: addGenre(BIGRAMS_SONG_STORE_DIR_VAL, genre) for genre in GENRES}
BIGRAMS_SONG_STORE_TEST = {genre: addGenre(BIGRAMS_SONG_STORE_DIR_TEST, genre) for genre in GENRES}

BIGRAMS_SONG_STORE = {'train': BIGRAMS_SONG_STORE_TRAIN, 'val': BIGRAMS_SONG_STORE_VAL, 'test': BIGRAMS_SONG_STORE_TEST}

TRIGRAMS_SONG_STORE_DIR_TRAIN = '../../data/objects/ngrams/trigrams/songs/train'
TRIGRAMS_SONG_STORE_DIR_VAL = '../../data/objects/ngrams/trigrams/songs/val'
TRIGRAMS_SONG_STORE_DIR_TEST = '../../data/objects/ngrams/trigrams/songs/test'

TRIGRAMS_SONG_STORE_TRAIN = {genre: addGenre(TRIGRAMS_SONG_STORE_DIR_TRAIN, genre) for genre in GENRES}
TRIGRAMS_SONG_STORE_VAL = {genre: addGenre(TRIGRAMS_SONG_STORE_DIR_VAL, genre) for genre in GENRES}
TRIGRAMS_SONG_STORE_TEST = {genre: addGenre(TRIGRAMS_SONG_STORE_DIR_TEST, genre) for genre in GENRES}

TRIGRAMS_SONG_STORE = {'train': TRIGRAMS_SONG_STORE_TRAIN, 'val': TRIGRAMS_SONG_STORE_VAL, 'test': TRIGRAMS_SONG_STORE_TEST}