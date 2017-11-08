from Constants import directories
from files import saveJSONObject
from lib.learn import createFeatureMatrix, _createFeatureMatrix

spanishWords = directories.SPANISH_WORD_SET
germanWords = directories.GERMAN_WORD_SET,
frenchWords = directories.FRENCH_WORD_SET

featuresTrain, labelsTrain = createFeatureMatrix(spanishWords, germanWords, frenchWords, path=directories.PATH_TRAIN,
												 lyricStore=directories.LYRICS_TRAIN)
saveJSONObject(featuresTrain, directories.FEATURE_MATRIX_TRAIN)
saveJSONObject(labelsTrain, directories.LABELS_TRAIN)

featuresVal, labelsVal = createFeatureMatrix(spanishWords, germanWords, frenchWords, path=directories.PATH_VAL,
											 lyricStore=directories.LYRICS_VAL)
saveJSONObject(featuresVal, directories.FEATURE_MATRIX_VAL)
saveJSONObject(labelsVal, directories.LABELS_VAL)
