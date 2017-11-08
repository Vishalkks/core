from core.main.Util.files import saveJSONObject, create

from core.main.Constants import directories
from lib.data import getFrequencies
from lib.learn import evaluateFrequencies


create(directories.PICKLE_DIR)
genreFreqsTrain, allFreqsTrain, numSongsTrain = getFrequencies(directories.PATH_TRAIN)
saveJSONObject(numSongsTrain, directories.NUM_SONGS_TRAIN)
saveJSONObject(allFreqsTrain, directories.ALL_FREQS_TRAIN)
saveJSONObject(genreFreqsTrain, directories.GENRE_FREQS_TRAIN)

genreFreqsVal, allFreqsVal, numSongsVal = getFrequencies(directories.PATH_VAL)
saveJSONObject(genreFreqsVal, directories.GENRE_FREQS_VAL)
saveJSONObject(allFreqsVal, directories.ALL_FREQS_VAL)
saveJSONObject(numSongsVal, directories.NUM_SONGS_VAL)

genreFreqsTest, allFreqsTest, numSongsTest = getFrequencies(directories.PATH_TEST)
saveJSONObject(genreFreqsTest, directories.GENRE_FREQS_TEST)
saveJSONObject(allFreqsTest, directories.ALL_FREQS_TEST)
saveJSONObject(numSongsTest, directories.NUM_SONGS_TEST)

print 'done'
