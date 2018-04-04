# -*- coding: utf-8 -*-
import Roots

# vowels, consonants, letters
vowLow = ['a', 'e', 'i', 'o', 'u', 'ā', 'ē', 'ī', 'ō', 'ū']
vowCap = ['A', 'E', 'I', 'O', 'U', 'Ā', 'Ē', 'Ī', 'Ō', 'Ū']
macronLow = ['ā', 'ē', 'ī', 'ō', 'ū']
macronCap = ['Ā', 'Ē', 'Ī', 'Ō', 'Ū']
macrons = macronLow+macronCap
vow = vowLow+vowCap
consLow = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
consCap = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
cons = consLow+consCap
lettersLow = vowLow+consLow
lettersCap = vowCap+consCap
letters = lettersLow+lettersCap

# constant values
NUM_VOW = len(vow)
NUM_VOW_CAP = len(vowCap)
NUM_CONS = len(cons)
NUM_CONS_CAP = len(consCap)
NUM_LETTERS = len(letters)
NUM_LETTERS_CAP = len(lettersCap)

# endings
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
	# active  voice
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
	# passive voice
	# imperative

# -------------------------------------------------------------
# REVERSE CONJUGATION
def findTense3P(root, per, num, perf):
	if root[-5:] == "erunt":
		tense = "PERF"
		perf = True
		# print('hi1')
	elif root[-5:] == "erant":
		tense = "PLUP"
		perf = True
		# print('hi2')
	elif root[-5:] == "erint":
		tense = "FUTP"
		perf = True
		# print('hi3')

	elif root[-4:] == "bant":
		tense = "IMPF"
		if root[-6:-4] == "ie":
			inf = root[:-5]+"re"	 	#ire 4th
			if not(inf in Roots.LatinV_inf):
				inf = root[:-6]+"ere" 	#ere 3rd IO/5th
		else:
			inf = root[:-4]+"re"
		# print('hi4')

	elif root[-4:] == "bunt":
		tense = "FUTR"
		inf = root[:-4]+"re"
		# print('hi5')
	elif root[-4:] == "ient":
		tense = "FUTR"
		inf = root[:-3]+"re" 	#ire 4th
		# print('hi5')
		if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-4]+"ere"
			# print('hi5a')

	elif root[-3:] == "ant":
		tense = "PRES"
		inf = root[:-2]+"re" 	#are 1st
		# print('hi6')
	elif root[-4:] == "iunt":
		tense = "PRES"
		inf = root[:-3]+"re" 	#ire 4th
		if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-4]+"ere"
		# print('hi7')
	elif root[-3:] == "unt":
		tense = "PRES"
		inf = root[:-3]+"ere" 	#ere 3rd
		# print('hi8')

	elif root[-3:] == "ent": 	# could be future(3rd) or present(2nd)
		inf = root[:-2]+"re"
		if Roots.findConjI(root[:-2]+"re") == 3:	# if 3rd conj
			tense = "FUTR"
		else:
			tense = "PRES" 							# in 2nd conj

	if (perf):
		perf = root[:-5]+"i"
		if root[-6] == "i":
			perf = root[:-5]
		inf = Roots.findInfP(perf)
	else: 
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def findTense3S(root, per, num, perf):
	if root[-2:] == "it":
		if root[:-1] in Roots.LatinV_perf:
			tense = "PERF"
			perf = True
		else:
			tense = "PRES"
		# print('hi1')
	elif root[-4:] == "erat":
		tense = "PLUP"
		perf = True
		# print('hi2')
	elif root[-4:] == "erit":
		tense = "FUTP"
		perf = True
		# print('hi3')

# def findTense1P(root, per, num, perf):

def reverseConjugate(word):
	per = ""
	num = ""
	root = ""
	perf = False

	if word[-3:] == "mus":
		per = "FST"
		num = "PL"
		return findTense1P(word,per,num,perf)

	elif word[-1] == "s":
		per = "SND"
		if word[-3:] == "tis":
			num = "PL"
		else:
			num = "SG"
	elif word[-1] == "t":
		per = "TRD"
		if word[-2:] == "nt":
			num = "PL"
			return findTense3P(word,per,num,perf)
		else:
			num = "SG"
			return findTense3S(word,per,num,perf)

	elif word[-1] == "o" or word[-1] == "m":
		per = "FST"
		num = "SG"

