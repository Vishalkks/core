import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from core.main.Constants import directories
from files import getJSONObject, saveJSONObject


X = getJSONObject(directories.FEATURE_MATRIX_TRAIN)
Y = getJSONObject(directories.LABELS_TRAIN)
M = getJSONObject(directories.FEATURE_MATRIX_VAL)
N = getJSONObject(directories.LABELS_VAL)

X = np.array(X)
Y = np.array(Y)
M = np.array(M)
N = np.array(N)

print X.shape
print M.shape

lr = LogisticRegression(solver='lbfgs')
lr.fit(X, Y)
pred = lr.predict(M)
saveJSONObject(pred, directories.RESULTS)

print accuracy_score(N, pred)
