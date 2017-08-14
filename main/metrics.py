def precision(matrix,genre):
    #tp/tp+fp
    truePositives = float(matrix[genre][genre])
    allPositives = float(sum([matrix[g][genre] for g in matrix.keys()]))
    return truePositives/allPositives

def printAllPrecisions(matrix):
    for genre in matrix.keys():
        print 'Genre:', genre, precision(matrix, genre)

def precisionForAll():
    pass

def recall(matrix, genre):
    #tp/tp+fn
    truePositives = float(matrix[genre][genre])
    allPositives = float(sum([matrix[genre][g] for g in matrix.keys()]))
    return truePositives/allPositives

def printAllRecalls(matrix):
    for genre in matrix.keys():
        print 'Genre:', genre, recall(matrix, genre)

def recallForAll():
    pass