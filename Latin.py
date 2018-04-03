# -*- coding: utf-8 -*-
vowLow = ['a', 'e', 'i', 'o', 'u']
vowCap = ['A', 'E', 'I', 'O', 'U']
vow = vowLow+vowCap
consLow = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
consCap = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
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

endings = {"FSTSG":"o","SNDSG":"s","TRDSG":"t","FSTPL":"mus","SNDPL":"tis","TRDPL":"nt"}
endingsV = {"FSTSG":"m","SNDSG":"s","TRDSG":"t","FSTPL":"mus","SNDPL":"tis","TRDPL":"nt"}
perfEndings = {"FSTSG":"i","SNDSG":"isti","TRDSG":"it","FSTPL":"imus","SNDPL":"istis","TRDPL":"erunt"}
plupEndings = {"FSTSG":"eram","SNDSG":"eras","TRDSG":"erat","FSTPL":"eramus","SNDPL":"eratis","TRDPL":"erant"}
futpEndings = {"FSTSG":"ero","SNDSG":"eris","TRDSG":"erit","FSTPL":"erimus","SNDPL":"eritis","TRDPL":"erint"}

def getIndexL(letter):
	return letters.index(letter)

def getIndex(word):
	lst = []
	for i in range(len(word)):
		lst.append(getIndexL(word[i]))
	return lst

def toUpperL(letter):
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
# CONJUGATION

def presentTense(inf, t, per, num):
	# 1st Conjugations
	if t[0] == "1":
		if (per+num) == "FSTSG":
			stem = inf[:-3]
		else:
			stem = inf[:-2] 	# cutoff "re" from ending (ama)
	elif t[0] == "2":
		stem = inf[:-2]
	elif t[0] == "3":
		if (per+num) == "FSTSG":
			stem = inf[:-3]
		elif (per+num) == "TRDPL":
			stem = inf[:-3]+"u"
		else:
			stem = inf[:-3]+"i"
	elif t[0] == "4":
		if (per+num) == "TRDPL":
			stem = inf[:-2]+"u"
		else:
			stem = inf[:-2]
	elif t[0] == "5":
		stem = inf[:-3]+"i"
		if (per+num) == "TRDPL":
			stem +="u"

	end = endings[per+num]
	return stem+end

def imperfectTense(inf, t, per, num):
	if t[0] =="1" or t[0] == "2" or t[0] == "3":
		stem = inf[:-2]
	if t[0] =="4" or t[0] == "5":
		stem = inf[:-3]+"ie"

	end = endingsV[per+num]
	return stem+"ba"+end

def futureTense(inf, t, per, num):
	if t[0] == "1" or t[0] == "2":
		if (per+num) == "FSTSG":
			stem = inf[:-2]+"b"
		elif (per+num) == "TRDPL":
			stem = inf[:-2]+"bu"
		else:
			stem = inf[:-2]+"bi"
		
		end = endings[per+num]

	else:
		if t[0] == "3":
			if (per+num) == "FSTSG":
				stem = inf[:-3]+"a"
			else:
				stem = inf[:-2]
		elif t[0] == "4" or t[0] == "5":
			stem = inf[:-3]
			if (per+num) == "FSTSG":
				stem += "ia"
			else:
				stem += "ie"

		end = endingsV[per+num]

	return stem+end

def perfectTense(perf, t, per, num):
	stem = perf[:-1]
	end = perfEndings[per+num]
	return stem+end

def pluperfectTense(perf, t, per, num):
	stem = perf[:-1]
	end = plupEndings[per+num]
	return stem+end

def futureperfectTense(perf, t, per, num):
	stem = perf[:-1]
	end = futpEndings[per+num]
	return stem+end	

# takes infinitive, perfective, type, number, person, tense
def conjugate(inf, perf, t, per, num, tense):
	if tense == "PRES":
		return presentTense(inf,t,per,num)
	elif tense == "IMPF":
		return imperfectTense(inf,t,per,num)
	elif tense == "FUTR":
		return futureTense(inf,t,per,num)
	elif tense == "PERF":
		return perfectTense(perf,t,per,num)
	elif tense == "PLUP":
		return pluperfectTense(perf,t,per,num)
	elif tense == "FUTP":
		return futureperfectTense(perf,t,per,num)

# -------------------------------------------------------------
# REVERSE CONJUGATION