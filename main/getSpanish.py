import codecs

from Constants import directories
from core.main.Util.files import saveJSONObject
from lib.data import getWords

spanishWordFile = directories.SPANISH_WORD_FILE
spanishWords = getWords(spanishWordFile)

saveJSONObject(spanishWords, directories.SPANISH_WORD_SET)

germanWordFile = directories.GERMAN_WORD_FILE
germanWords = getWords(germanWordFile)

frenchWordFile = directories.FRENCH_WORD_FILE
frenchWords = getWords(frenchWordFile)

saveJSONObject(germanWords, directories.GERMAN_WORD_SET)
saveJSONObject(frenchWords, directories.FRENCH_WORD_SET)

