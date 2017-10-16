def is_ascii(s):
	return all(ord(c) < 128 for c in s)


def is_asciiList(li):
	return all(is_ascii(w) for w in li)


def isNotEmpty(li):
	return len(li)


def punctuate(string):
	string = string.replace("__backslash__", "\\")
	string = string.replace("__forwardslash__", "/")
	string = string.replace("__colon__", ":")
	string = string.replace("__qmark__", "?")
	string = string.replace("__quote__", "\"")
	string = string.replace("__greaterthan__", ">")
	string = string.replace("__lesserthan__", "<")
	string = string.replace("__star__", "*")
	string = string.replace("__bitwiseor__", "|")
	string = string.replace(' ', '%20')
	# string = string.replace("%", "%25")
	return string


def unpunctuate(string):
	string = string.replace("\\", "__backslash__")
	string = string.replace("/", "__forwardslash__")
	string = string.replace(":", "__colon__")
	string = string.replace("?", "__qmark__")
	string = string.replace("\"", "__quote__")
	string = string.replace(">", "__greaterthan__")
	string = string.replace("<", "__lesserthan__")
	string = string.replace("*", "__star__")
	string = string.replace("|", "__bitwiseor__")
	# string = string.replace("%25", "%")
	return string
