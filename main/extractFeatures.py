from Constants import directories
from files import saveJSONObject
from lib.learn import createFeatureMatrix


features, labels = createFeatureMatrix(path=directories.PATH_TRAIN)
saveJSONObject(features, directories.FEATURE_MATRIX)
saveJSONObject(labels, directories.LABELS)