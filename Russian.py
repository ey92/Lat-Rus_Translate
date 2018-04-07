# Elizabeth Yam ey92
# -*- coding: utf-8 -*-
import Roots

vowLow = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowCap = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
vow = vowLow+vowCap
consLow = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь']
consCap = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь']
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
VERB_FORM_KEYS = ['FSTSG', 'SNDSG', 'TRDSG', 'FSTPL', 'SNDPL', 'TRDPL','M','F','N']

# verb endings
endings1vlst = ['ю','ешь','ет','ем','ете','ют']
endings1clst = ['у','ёшь','ёт','ём','ёте','ут']
endings2vlst = ['ю','ишь','ит','им','ите','ят']
endings2clst = ['у','ищь','ит','им','ите','ат']
endings1v = dict(zip(VERB_FORM_KEYS,endingsNPvlst))
endings1c = dict(zip(VERB_FORM_KEYS,endingsNPclst))
endings2v = dict(zip(VERB_FORM_KEYS,endingsPvlst))
endings2c = dict(zip(VERB_FORM_KEYS,endingsPclst))

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

# -------------------------------------------------------------
# -------------------------------------------------------------
# VERBS
# -------------------------------------------------------------
# CONJUGATION

def nonPastTense(inf, t, per, num, perf):
	form = per+num
	root = Roots.Rf
	end = ''

	if perf:
		stem = Roots.RfindP3PPInf(inf)
	else:
		stem = Roots.RfindI3PIInf(inf)

	# if looking for 3P, done
	if form == 'TRDPL':
		return stem

	# take off 3P ending for stem
	stem = stem [:-4]

	# if 1st conj
	if t[0] == '1':
		# if vowel stem
		if t[1] == 'v':
			end = endings1v[form]
		# if cons stem
		elif t[1] == 'c':
			end = endings1c[form]
	# if 2nd conj
	elif t[0] == '2':
		# if vowel stem
		if t[1] == 'v':
			end = endings2v[form]
		# if cons stem
		elif t[1] == 'c':
			end = endings2c[form]

	return stem+end

# def pastTense(inf, t, per, num, perf):

# def futureTense(inf, t, per, num):


def conjugate (inf, per, num, tense):
	
	# PRES,IMPF,FUTR need impf inf
	if tense in ['PRES','IMPF','FUTR']:
		perf = False

		# find impf inf if given perf inf
		if inf in Roots.RussianV_perf_inf:
			inf = Roots.RfindIInfP(inf)
		
		# if impf inf
		if inf in Roots.RussianV_impf_inf:
			# t = conjugation
			t = Roots.RfindIConjIInf(inf)

			if tense == 'PRES':
				return nonPastTense(inf,t,per,num, perf)
			elif tense == 'IMPF':
				return pastTense(inf,t,per,num, perf)
			elif tense == 'FUTR':
				return futureTense(inf,t,per,num)

	# PERF, FUTP tenses need PERF inf
	elif tense in ['PERF','FUTP']:
		perf = True

		# find impf inf if given
		if inf in Roots.RussianV_impf_inf:
			inf = Roots.RfindPInfI(inf)

		# inf perf inf
		if perf in Roots.RussianV_perf_inf:
			# t = conjugation
			t = Roots.RfindPConjPInf(inf)

			if tense == 'PERF':
				return pastTense(inf,t,per,num, perf)
			elif tense == 'FUTP':
				return nonPastTense(inf,t,per,num, perf)