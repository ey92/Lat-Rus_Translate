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
irreg = ["ire","esse","posse","velle","nelle","ferre"]

# endings
endings = {"FSTSG":"o","SNDSG":"s","TRDSG":"t","FSTPL":"mus","SNDPL":"tis","TRDPL":"nt"}
endingsV = {"FSTSG":"m","SNDSG":"s","TRDSG":"t","FSTPL":"mus","SNDPL":"tis","TRDPL":"nt"}
perfEndings = {"FSTSG":"ī","SNDSG":"isti","TRDSG":"it","FSTPL":"imus","SNDPL":"istis","TRDPL":"erunt"}
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
		stem = inf[:-3]+"e"
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

def irregular(inf, perf, per, num, tense):
	form = per+num
	if inf == "ire":
		if tense == "PRES":
			if form == "FSTSG":
				return "eo"
			elif form == "SNDSG":
				return "is"
			elif form == "TRDSG":
				return "it"
			elif form == "FSTPL":
				return "imus"
			elif form == "SNDPL":
				return "itis"
			elif form == "TRDPL":
				return "eunt"
		elif tense == "IMPF":
			if form == "FSTSG":
				return "ibam"
			elif form == "SNDSG":
				return "ibas"
			elif form == "TRDSG":
				return "ibat"
			elif form == "FSTPL":
				return "ibamus"
			elif form == "SNDPL":
				return "ibatis"
			elif form == "TRDPL":
				return "ibant"
		elif tense == "FUTR":
			if form == "FSTSG":
				return "ibo"
			elif form == "SNDSG":
				return "ibis"
			elif form == "TRDSG":
				return "ibit"
			elif form == "FSTPL":
				return "ibimus"
			elif form == "SNDPL":
				return "ibitis"
			elif form == "TRDPL":
				return "ibunt"
		elif tense == "PERF":
			if form == "FSTSG":
				return "īvī"
			elif form == "SNDSG":
				return "īvisti"
			elif form == "TRDSG":
				return "īvit"
			elif form == "FSTPL":
				return "īvimus"
			elif form == "SNDPL":
				return "īvistis"
			elif form == "TRDPL":
				return "īverunt"
		elif tense == "PLUP":
			if form == "FSTSG":
				return "īveram"
			elif form == "SNDSG":
				return "īveras"
			elif form == "TRDSG":
				return "īverat"
			elif form == "FSTPL":
				return "īveramus"
			elif form == "SNDPL":
				return "īveratis"
			elif form == "TRDPL":
				return "īverant"
		elif tense == "FUTP":
			if form == "FSTSG":
				return "īvero"
			elif form == "SNDSG":
				return "īveris"
			elif form == "TRDSG":
				return "īverit"
			elif form == "FSTPL":
				return "īverimus"
			elif form == "SNDPL":
				return "īveritis"
			elif form == "TRDPL":
				return "īverint"
	if inf == "esse":
		if tense == "PRES":
			if form == "FSTSG":
				return "sum"
			elif form == "SNDSG":
				return "es"
			elif form == "TRDSG":
				return "est"
			elif form == "FSTPL":
				return "sumus"
			elif form == "SNDPL":
				return "estis"
			elif form == "TRDPL":
				return "sunt"
		elif tense == "IMPF":
			if form == "FSTSG":
				return "eram"
			elif form == "SNDSG":
				return "eras"
			elif form == "TRDSG":
				return "erat"
			elif form == "FSTPL":
				return "eramus"
			elif form == "SNDPL":
				return "eratis"
			elif form == "TRDPL":
				return "erant"
		elif tense == "FUTR":
			if form == "FSTSG":
				return "ero"
			elif form == "SNDSG":
				return "eris"
			elif form == "TRDSG":
				return "erit"
			elif form == "FSTPL":
				return "erimus"
			elif form == "SNDPL":
				return "eritis"
			elif form == "TRDPL":
				return "erunt"
		elif tense == "FUTR":
			if form == "FSTSG":
				return "fuī"
			elif form == "SNDSG":
				return "fuisti"
			elif form == "TRDSG":
				return "fuit"
			elif form == "FSTPL":
				return "fuimus"
			elif form == "SNDPL":
				return "fuistis"
			elif form == "TRDPL":
				return "fuerunt"
		elif tense == "PLUP":
			if form == "FSTSG":
				return "fueram"
			elif form == "SNDSG":
				return "fueras"
			elif form == "TRDSG":
				return "fuerat"
			elif form == "FSTPL":
				return "fueramus"
			elif form == "SNDPL":
				return "fueratis"
			elif form == "TRDPL":
				print('tense')
				return "fuerant"
		elif tense == "FUTP":
			if form == "FSTSG":
				return "fuero"
			elif form == "SNDSG":
				return "fueris"
			elif form == "TRDSG":
				return "fuerit"
			elif form == "FSTPL":
				return "fuerimus"
			elif form == "SNDPL":
				return "fueritis"
			elif form == "TRDPL":
				return "fuerint"
	if inf == "posse":
		temp = irregular("sum", "esse", per, num, tense)
		if tense == "PRES" or tense == "IMPF" or tense == "FUTR":
			if temp[0] == "s":
				return "pos"+temp
			elif temp[0] == "e":
				return "pot"+temp
		else:
			return "pot"+temp[1:]

# takes infinitive, perfective, type, number, person, tense
def conjugate(inf, perf, t, per, num, tense):
	# active  voice
	if inf in irreg:
		print('hi')
		return irregular(inf,perf,per,num,tense)
	elif tense == "PRES":
		print('hi1')
		return presentTense(inf,t,per,num)
	elif tense == "IMPF":
		print('hi2')
		return imperfectTense(inf,t,per,num)
	elif tense == "FUTR":
		print('hi3')
		return futureTense(inf,t,per,num)
	elif tense == "PERF":
		print('hi4')
		return perfectTense(perf,t,per,num)
	elif tense == "PLUP":
		print('hi5')
		return pluperfectTense(perf,t,per,num)
	elif tense == "FUTP":
		print('hi6')
		return futureperfectTense(perf,t,per,num)
	else:
		print('hi7')
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
		if root[:-2]+"re" in Roots.LatinV_inf:	# if 3rd conj
			tense = "FUTR"
		else:
			inf = root[:-3]+"ēre"
			tense = "PRES" 							# in 2nd conj

	if (perf):
		perf = root[:-5]+"ī" 	# perf
		inf = Roots.findInfP(perf)
	else: 
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def findTense3S(root, per, num, perf):
	if root[-3:] == "bat":
		tense = "IMPF"
		if root[-5:-3] == "ie":
			inf = root[:-4]+"re"	 	#ire 4th
			if not(inf in Roots.LatinV_inf):
				inf = root[:-5]+"ere" 	#ere 3rd IO/5th
		else:
			inf = root[:-3]+"re"
		# print('hi4')

	elif root[-3:] == "bit":
		tense = "FUTR"
		inf = root[:-3]+"re"
		# print('hi8')
	elif root[-3:] == "iet":
		tense = "FUTR"
		inf = root[:-2]+"re" 	#ire 4th
		# print('hi5')
		if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-3]+"ere"
			# print('hi5a')

	elif root[-4:] == "erit":
		tense = "FUTP"
		perf = True
		# print('hi3')
	elif root[-2:] == "it":
		if root[:-2]+"ī" in Roots.LatinV_perf:
			tense = "PERF"
			perf = True
		else:
			tense = "PRES"
			inf = root[:-1]+"re" 	#ire 4th
			if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
				inf = root[:-2]+"ere"
			# print('hi7')
		# print('hi1')
	elif root[-4:] == "erat":
		tense = "PLUP"
		perf = True
		# print('hi2')

	elif root[-2:] == "at":
		tense = "PRES"
		inf = root[:-1]+"re" 	#are 1st
		# print('hi6')
	elif root[-2:] == "it":
		tense = "PRES"
		inf = root[:-1]+"re" 	#ire 4th
		if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-2]+"ere"
		# print('hi7')

	elif root[-2:] == "et": 	# could be future(3rd) or present(2nd)
		inf = root[:-1]+"re"
		if root[:-1]+"re" in Roots.LatinV_inf:	# if 3rd conj
			tense = "FUTR"
		else:
			inf = root[:-2]+"ēre"
			tense = "PRES" 							# in 2nd conj

	if (perf):
		perf = root[:-2]+"ī"
		if root[-4] == "e":
			perf = root[:-4]+"ī"
		# print(perf)
		inf = Roots.findInfP(perf)
	else: 
		# print(inf)
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def findTense2P(root, per, num, perf):
	if root[-5:] == "istis":
		tense = "PERF"
		perf = True
	elif root[-6:] == "eratis":
		tense = "PLUP"
		perf = True
	elif root[-6:] == "eritis":
		tense = "FUTP"
		perf = True

	elif root[-5:] == "batis":
		tense = "IMPF"
		if root[-7:-5] == "ie":
			inf = root[:-6]+"re"	 	#ire 4th
			if not(inf in Roots.LatinV_inf):
				inf = root[:-7]+"ere" 	#ere 3rd IO/5th
		else:
			inf = root[:-5]+"re"

	elif root[-5:] == "bitis":
		tense = "FUTR"
		inf = root[:-5]+"re"
	elif root[-5:] == "ietis":
		tense = "FUTR"
		inf = root[:-4]+"re" 	#ire 4th
		if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-5]+"ere"

	elif root[-4:] == "etis":
		tense = "FUTR"
		inf = root[:-3]+"re" 	#ere 3rd fut
		if not(inf in Roots.LatinV_inf): 	#ēre 2nd pres
			tense = "PRES"
			inf = root[:-4]+"ēre"

	elif root[-3:] == "tis":
		tense = "PRES"
		inf = root[:-3]+"re"
		if not(inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-4]+"ere"

	if (perf):
		perf = root[:-5]+"ī"
		if root[-6] == "e":
			perf = root[:-6]+"ī"
		# print(perf)
		inf = Roots.findInfP(perf)
	else: 
		# print(inf)
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def findTense2S(root, per, num, perf):
	if root[-4:] == "isti":
		tense = "PERF"
		perf = True
		# print('hi1')
	elif root[-4:] == "eras":
		tense = "PLUP"
		perf = True
	elif root[-4:] == "eris":
		tense = "FUTP"
		perf = True

	elif root[-3:] == "bas":
		tense = "IMPF"
		if root[-5:-3] == "ie":
			inf = root[:-4]+"re"	 	#ire 4th
			if not(inf in Roots.LatinV_inf):
				inf = root[:-5]+"ere" 	#ere 3rd IO/5th
		else:
			inf = root[:-3]+"re"

	elif root[-3:] == "bis":
		tense = "FUTR"
		inf = root[:-3]+"re"
	elif root[-3:] == "ies":
		tense = "FUTR"
		inf = root[:-2]+"re" 	#ire 4th
		if not (inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-3]+"ere"

	elif root[-2:] == "es":
		tense = "FUTR"
		inf = root[:-1]+"re" 	#ere 3rd fut
		if not(inf in Roots.LatinV_inf): 	#ēre 2nd pres
			tense = "PRES"
			inf = root[:-2]+"ēre"

	elif root[-1] == "s":
		# print('hi8')
		tense = "PRES"
		inf = root[:-1]+"re"
		if not(inf in Roots.LatinV_inf): 	#ere 3rd IO/5th
			inf = root[:-2]+"ere"

	if (perf):
		perf = root[:-4]+"ī"
		# print(perf)
		inf = Roots.findInfP(perf)
	else: 
		# print(inf)
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def findTense1P(root, per, num, perf):
	if root[-6:] == "eramus":
		tense = "PLUP"
		perf = True
	elif root[-6:] == "erimus":
		tense = "FUTP"
		perf = True

	elif root[-5:] == "bimus":
		tense = "FUTR"
		inf = root[:-5]+"re"

	elif root[-4:] == "imus":
		if (root[:-4]+"ī") in Roots.LatinV_perf:
			tense = "PERF"
			perf = True
		else:
			perf = False
			tense = "PRES"
			inf = root[:-3]+"re" 		#ire 4th pres
			if not(inf in Roots.LatinV_inf):
				inf = root[:-4]+"ere"	#ere 3rd or 3rd IO/5th pres

	elif root[-5:] == "bamus":
		tense = "IMPF"
		if root[-7:-5] == "ie":
			inf = root[:-6]+"re"	 	#ire 4th
			if not(inf in Roots.LatinV_inf):
				inf = root[:-7]+"ere" 	#ere 3rd IO/5th
		else:
			inf = root[:-5]+"re"

	elif root[-5:] == "iemus":	 		#4th, 3rd IO/5th fut
		tense = "FUTR"
		inf = root[:-4]+"re" 			#ire 4th
		if not(inf in Roots.LatinV_inf):
			inf = root[:-5]+"ere" 		#ere 3rd IO/5th

	elif root[-4:] == "emus":
		inf = root[:-4]+"ēre"
		if inf in Roots.LatinV_inf: 	#2nd pres
			tense = "PRES"
		else: 							#3rd fut
			tense = "FUTR" 
			inf = root[:-3]+"re"

	elif root[-3:] == "mus": 			# 1st, 2nd pres
		tense = "PRES"
		inf = root[:-3]+"re"

	if (perf):
		perf = root[:-4]+"ī"
		if root[-6] == "e":
			perf = root[:-6]+"ī"
		# print(perf)
		inf = Roots.findInfP(perf)
	else: 
		# print(inf)
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def findTense1S(root, per, num, perf):
	if root in Roots.LatinV_perf:
		tense = "PERF"
		perf = True
	elif root[-4:] == "eram":
		tense = "PLUP"
		perf = True
	elif root[-3:] == "ero":
		tense = "FUTP"
		perf = True

	elif root[-3:] == "bam":
		tense = "IMPF"
		if root[-5:-3] == "ie": 
			inf = root[:-4]+"re" 		#ire 4th
			if not(inf in Roots.LatinV_inf):
				inf = root[:-5]+"ere"	#ere 3rd IO/5th
		else:
			inf = root[:-3]+"re" 		#1st,2nd,3rd

	elif root[-2:] == "bo":
		tense = "FUTR"
		inf = root[:-2]+"re"
	elif root[-3:] == "iam":
		tense = "FUTR"
		inf = root[:-2]+"re" 		#ire 4th
		if not(inf in Roots.LatinV_inf):
			inf = root[:-3]+"ere" 	#ere 3rd IO/5th

	elif root[-2:] == "am":
		tense = "FUTR"
		inf = root[:-2]+"ere" 		#ere 3rd

	elif root[-1] == "o":			#pres
		tense = "PRES"
		inf = Roots.findInfFS(root)

	if (perf):
		if tense == "PERF":
			perf = root
		elif root[-4] == "e":
			perf = root[:-4]+"ī"
		elif root[-3] == "e":
			perf = root[:-3]+"ī"
		inf = Roots.findInfP(perf)
	else: 
		# print(inf)
		perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def reverseConjugate(word):
	perf = False

	if word[-3:] == "mus":
		per = "FST"
		num = "PL"
		return findTense1P(word,per,num,perf)

	elif word[-1] == "s" or word[-3:] == "sti":
		per = "SND"
		if word[-3:] == "tis" and len(word) > 5:
			num = "PL"
			return findTense2P(word,per,num,perf)
		else:
			num = "SG"
			return findTense2S(word,per,num,perf)
	elif word[-1] == "t":
		per = "TRD"
		if word[-2:] == "nt":
			num = "PL"
			return findTense3P(word,per,num,perf)
		else:
			num = "SG"
			return findTense3S(word,per,num,perf)

	# unicode macron issues
	# elif word[-1] == "o" or word[-1] == "m" or word[-2] == "ī":
	else:
		per = "FST"
		num = "SG"
		return findTense1S(word,per,num,perf)

