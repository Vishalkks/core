from core.main.Constants import directories
from files import getJSONObject, saveJSONObject
from lib.learn import classifyMNB, createResultMatrix


results = classifyMNB(createResultMatrix(), genreFreqsTrain=getJSONObject(directories.GENRE_FREQS_TRAIN),
					allFreqsTrain=getJSONObject(directories.ALL_FREQS_TRAIN), path=directories.PATH_VAL)

saveJSONObject(results, directories.RESULTS)