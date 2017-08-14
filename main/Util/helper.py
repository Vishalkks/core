def printMatrix(matrix,filename):
    f = open(filename,"w+")
    f.write("\t")
    for key in matrix:
        f.write(key[:3]+"\t")
    f.write("\n")
    for key in matrix:
        f.write(key[:3]+"\t")
        for innerKey in matrix[key]:
            f.write(str(matrix[key][innerKey])+"\t")
        f.write("\n")
    f.close()