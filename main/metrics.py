def precision(matrix, genre):
	# tp/tp+fp
	truePositives = float(matrix[genre][genre])
	allPositives = float(sum([matrix[g][genre] for g in matrix.keys()]))

	if allPositives == 0.0:
		return float("inf")
	else:
		return truePositives / allPositives


def printAllPrecisions(matrix, filename):
	f = open(filename, "w+")
	for genre in matrix.keys():
		print 'Genre:', genre, 'Precision:', precision(matrix, genre)
		f.write('Genre:' + str(genre) + 'Precision:' + str(precision(matrix, genre)) + '\n')
	print 'Average Precision:', avgPrecision(matrix)
	f.write('Average Precision:' + str(avgPrecision(matrix)))


def recall(matrix, genre):
	# tp/tp+fn
	truePositives = float(matrix[genre][genre])
	allPositives = float(sum([matrix[genre][g] for g in matrix.keys()]))

	if allPositives == 0.0:
		return float("inf")
	else:
		return truePositives / allPositives


def printAllRecalls(matrix, filename):
	f = open(filename, "w+")

	for genre in matrix.keys():
		print 'Genre:', genre, 'Recall:', recall(matrix, genre)
		f.write(str('Genre:' + genre + 'Recall:' + str(recall(matrix, genre))) + '\n')
	print 'Average Recall:', avgRecall(matrix)
	f.write('Average Recall:' + str(avgRecall(matrix)))


def avgPrecision(matrix):
	li = [precision(matrix, genre) for genre in matrix.keys()]
	return float(sum(li))/float(len(li))


def avgRecall(matrix):
	li = [recall(matrix, genre) for genre in matrix.keys()]
	return float(sum(li))/float(len(li))