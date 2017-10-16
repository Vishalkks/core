from sklearn.linear_model import LogisticRegression

from core.main.Constants import directories
from files import getJSONObject, saveJSONObject
from lib.learn import classifyMNB, createResultMatrix


#MNB

#results = classifyMNB(createResultMatrix(), genreFreqsTrain=getJSONObject(directories.GENRE_FREQS_TRAIN), \
# allFreqsTrain=getJSONObject(directories.ALL_FREQS_TRAIN), path=directories.PATH_VAL)

#saveJSONObject(results, directories.RESULTS)

####


X = getJSONObject(directories.FEATURE_MATRIX_TRAIN)
Y = getJSONObject(directories.LABELS_TRAIN)
Z = getJSONObject(directories.FEATURE_MATRIX_VAL)

lr = LogisticRegression()
lr.fit(X, Y)
pred = lr.predict(Z)
saveJSONObject(pred, directories.RESULTS)

print pred