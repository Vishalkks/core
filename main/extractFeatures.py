from Constants import directories
from files import getJSONObject, saveJSONObject
from lib.learn import createFeatureMatrix


features, labels = createFeatureMatrix(path=directories.PATH_VAL)
saveJSONObject(features, directories.FEATURE_MATRIX)
saveJSONObject(labels, directories.LABELS)