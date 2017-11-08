def countLangWords(words, spanishSet):
	count = 0
	for word in words:
		if word in spanishSet:
			count += 1

	return count
