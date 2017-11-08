SENTS = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust', 'none']

SENT_NUMBER = dict({sent: SENTS.index(sent) for sent in SENTS})

NUM_SENTS = 11

GENRES = ['Alternative_Rock', 'Black_Metal', 'Blues', 'Christian', 'Country', 'Dance',
			'Death_Metal', 'Folk', 'Heavy_Metal', 'Hip_Hop', 'House', 'Industrial', 'Jazz',
			'Pop', 'Progressive_Rock', 'Punk_Rock', 'Rock', 'Samba', 'Soundtrack', 'Trance']

GEN_NUMBER = {genre: GENRES.index(genre) for genre in GENRES}
