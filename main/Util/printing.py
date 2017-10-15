def printMatrix(matrix,filename):
    f = open(filename,"w+")
    f.write('%-6s' % '.')
    for key in matrix:
        f.write('%-6s' % key[:3])
    f.write("\n")
    for key in matrix:
        f.write('%-6s' % key[:3])
        for innerKey in matrix[key]:
            f.write('%-6s' % str(matrix[key][innerKey]))
        f.write("\n")
    f.close()
