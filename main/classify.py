import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from Constants.values import GEN_NUMBER
from core.main.Constants import directories
from Util.files import getJSONObject, saveJSONObject


def getIndices(li, val):
	return [index for index, value in enumerate(li) if value == val]


def getValsByIndex(li, indices):
	return [li[i] for i in indices]


def genreSplice(data, labels, genreList):
	splicedData = []
	splicedLabels = []
	for genre in genreList:
		genIndices = getIndices(labels, GEN_NUMBER[genre])
		splicedLabels += getValsByIndex(labels, genIndices)
		splicedData += getValsByIndex(data, genIndices)

	return splicedData, splicedLabels

if __name__ == '__main__':
	X = getJSONObject(directories.FEATURE_MATRIX_TRAIN)
	Y = getJSONObject(directories.LABELS_TRAIN)
	M = getJSONObject(directories.FEATURE_MATRIX_VAL)
	N = getJSONObject(directories.LABELS_VAL)

	#X, Y = genreSplice(X, Y, ['Death_Metal', 'Country', 'Samba', 'Trance', 'Soundtrack', 'Rock'])
	#M, N = genreSplice(M, N, ['Death_Metal', 'Country', 'Samba', 'Trance', 'Soundtrack', 'Rock'])

	X = np.array(X)
	Y = np.array(Y)
	M = np.array(M)
	N = np.array(N)

	print X.shape
	print M.shape

	'''
	lr = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=1000, n_jobs=-1)
	lr.fit(X, Y)
	pred = lr.predict(M)
	#saveJSONObject(pred, directories.RESULTS)
	'''

	#clf = SVC()

	#lin_clf = sklearn.svm.LinearSVC()
	#lin_clf.fit(X, Y)
	#pred = lin_clf.predict(M)

	clf = MLPClassifier(activation='logistic')
	clf.fit(X, Y)
	pred = clf.predict(M)
	saveJSONObject(pred, directories.RESULTS)

	print accuracy_score(N, pred)

