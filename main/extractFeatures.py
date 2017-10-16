from Constants import directories
from files import saveJSONObject
from lib.learn import createFeatureMatrix


featuresTrain, labelsTrain = createFeatureMatrix(path=directories.PATH_TRAIN)
saveJSONObject(featuresTrain, directories.FEATURE_MATRIX_TRAIN)
saveJSONObject(labelsTrain, directories.LABELS_TRAIN)

featuresVal, labelsVal = createFeatureMatrix(path=directories.PATH_VAL)
saveJSONObject(featuresVal, directories.FEATURE_MATRIX_VAL)
saveJSONObject(labelsVal, directories.LABELS_VAL)
