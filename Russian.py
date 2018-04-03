# -*- coding: utf-8 -*-
class Russian:
	vowLow = [u'а', u'е', u'ё', u'и', u'о', u'у', u'ы', u'э', u'ю', u'я']
	vowCap = [u'А', u'Е', u'Ё', u'И', u'О', u'У', u'Ы', u'Э', u'Ю', u'Я']
	vow = vowLow+vowCap
	consLow = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'к', u'л', u'м', u'н', u'п', u'р', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ъ', u'ь']
	consCap = [u'Б', u'В', u'Г', u'Д', u'Ж', u'З', u'Й', u'К', u'Л', u'М', u'Н', u'П', u'Р', u'С', u'Т', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ь']
	cons = consLow+consCap
	lettersLow = vowLow+consLow
	lettersCap = vowCap+consCap
	letters = lettersLow+lettersCap

	NUM_VOW = len(vow)
	NUM_VOW_CAP = len(vowCap)
	NUM_CONS = len(cons)
	NUM_CONS_CAP = len(consCap)
	NUM_LETTERS = len(letters)
	NUM_LETTERS_CAP = len(lettersCap)

	def takeRaw(word):
		return word.decode('utf8')

	def getIndexL(letter):
		#letter = takeRaw(letter)
		return letters.index(letter)

	def getIndex(word):
		word = takeRaw(word)
		lst = []
		for i in range(len(word)):
			lst.append(getIndexL(word[i]))
		return lst

	# map(x if consonants.index(letter) > -1 else CONSONANTS[consonants.index(letter)], word)
	def toUpperL(letter):
		#letter = takeRaw(letter)
		return letters[(getIndexL(letter)+(NUM_LETTERS/2))%NUM_LETTERS]

	def toUpper(word):
		word = takeRaw(word)
		lst = []
		for i in range(len(word)):
			lst.append(toUpperL(word[i]))
		return lst

	def toLowerL(letter):
		toUpperL(letter)

	def toLower(word):
		toUpper(word)

	def morphology(input):
		#stuff