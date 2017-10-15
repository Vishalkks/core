from core.main.Constants import directories
from core.main.Util.files import create, partitionFiles

#partitions the dataset into training, validation, and testing.

trainDir=directories.PATH_TRAIN
testDir=directories.PATH_TEST
valDir=directories.PATH_VAL

create(trainDir)
create(testDir)
create(valDir)

partitionFiles(trainDir, testDir, valDir, originalDir=directories.LYRICS_DIR, logfile=open(directories.LOG_PATH, 'w+'))
