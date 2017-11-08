import os

from Constants import directories
from Constants.values import GENRES
from files import getJSONObject, getGenrePath, saveJSONObject
from lib.data import createLyricsObjects

trainDir = directories.PATH_TRAIN
valDir = directories.PATH_VAL
testDir = directories.PATH_TEST

lyricsStoreTrain = directories.LYRICS_TRAIN
lyricsStoreVal = directories.LYRICS_VAL
lyricsStoreTest = directories.LYRICS_TEST

createLyricsObjects(trainDir, lyricsStoreTrain)
createLyricsObjects(valDir, lyricsStoreVal)
createLyricsObjects(testDir, lyricsStoreTest)