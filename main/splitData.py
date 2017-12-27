from core.main.Constants import directories
from core.main.Util.files import createDir, partitionFiles

#partitions the dataset into training, validation, and testing.

trainDir=directories.PATH_TRAIN
testDir=directories.PATH_TEST
valDir=directories.PATH_VAL

createDir(trainDir)
createDir(testDir)
createDir(valDir)

partitionFiles(directories.LYRICS_DIR, trainDir, testDir, valDir , logfile=open(directories.LOG_PATH, 'w+'))
