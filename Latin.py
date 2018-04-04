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
VERB_FORM_KEYS = ['FSTSG', 'TRDPL', 'TRDSG', 'SNDPL', 'SNDSG', 'FSTPL']

# irregular verb conjugations
irreg = ["ire","esse","posse","velle","nolle","ferre"]
irePres = {"FSTSG":"eo","SNDSG":"is","TRDSG":"it","FSTPL":"imus","SNDPL":"itis","TRDPL":"eunt"}
ireImpf = {"FSTSG":"ibam","SNDSG":"ibas","TRDSG":"ibat","FSTPL":"ibamus","SNDPL":"ibatis","TRDPL":"ibant"}
ireFutr = {"FSTSG":"ibo","SNDSG":"ibis","TRDSG":"ibit","FSTPL":"ibimus","SNDPL":"ibitis","TRDPL":"ibunt"}
irePerf = {"FSTSG":"īvī","SNDSG":"īvisti","TRDSG":"īvit","FSTPL":"īvimus","SNDPL":"īvistis","TRDPL":"īverunt"}
irePlup = {"FSTSG":"īveram","SNDSG":"īveras","TRDSG":"īverat","FSTPL":"īveramus","SNDPL":"īveratis","TRDPL":"īverant"}
ireFutp = {"FSTSG":"īvero","SNDSG":"īveris","TRDSG":"īverit","FSTPL":"īverimus","SNDPL":"īveritis","TRDPL":"īverint"}
ireConj = {"PRES":irePres,"IMPF":ireImpf,"FUTR":ireFutr,"PERF":irePerf,"PLUP":irePlup,"FUTP":ireFutp}
ireAll = irePres.values() + ireImpf.values() + ireFutr.values() + irePerf.values() + irePlup.values() + ireFutp.values()

essePres = {"FSTSG":"sum","SNDSG":"es","TRDSG":"est","FSTPL":"sumus","SNDPL":"estis","TRDPL":"sunt"}
esseImpf = {"FSTSG":"eram","SNDSG":"eras","TRDSG":"erat","FSTPL":"eramus","SNDPL":"eratis","TRDPL":"erant"}
esseFutr = {"FSTSG":"ero","SNDSG":"eris","TRDSG":"erit","FSTPL":"erimus","SNDPL":"eritis","TRDPL":"erunt"}
essePerf = {"FSTSG":"fuī","SNDSG":"fuisti","TRDSG":"fuit","FSTPL":"fuimus","SNDPL":"fuistis","TRDPL":"fuerunt"}
essePlup = {"FSTSG":"fueram","SNDSG":"fueras","TRDSG":"fuerat","FSTPL":"fueramus","SNDPL":"fueratis","TRDPL":"fuerant"}
esseFutp = {"FSTSG":"fuero","SNDSG":"fueris","TRDSG":"fuerit","FSTPL":"fuerimus","SNDPL":"fueritis","TRDPL":"fuerint"}
esseConj = {"PRES":essePres,"IMPF":esseImpf,"FUTR":esseFutr,"PERF":essePerf,"PLUP":essePlup,"FUTP":esseFutp}
esseAll = essePres.values() + esseImpf.values() + esseFutr.values() + essePerf.values() + essePlup.values() + esseFutp.values()

possePresV = ['pos'+x if x[0]=='s' else 'pot'+x for x in essePres.values()]
posseImpfV = ['pos'+x if x[0]=='s' else 'pot'+x for x in esseImpf.values()]
posseFutrV = ['pos'+x if x[0]=='s' else 'pot'+x for x in esseFutr.values()]
possePerfV = ['pot'+x[1:] for x in essePerf.values()]
possePlupV = ['pot'+x[1:] for x in essePlup.values()]
posseFutpV = ['pot'+x[1:] for x in esseFutp.values()]
possePres = dict(zip(VERB_FORM_KEYS,possePresV))
posseImpf = dict(zip(VERB_FORM_KEYS,posseImpfV))
posseFutr = dict(zip(VERB_FORM_KEYS,posseFutrV))
possePerf = dict(zip(VERB_FORM_KEYS,possePerfV))
possePlup = dict(zip(VERB_FORM_KEYS,possePlupV))
posseFutp = dict(zip(VERB_FORM_KEYS,posseFutrV))
posseAll = possePres.values() + posseImpf.values() + posseFutr.values() + possePerf.values() + possePlup.values() + posseFutp.values()

vellePres = {"FSTSG":"volo","SNDSG":"vis","TRDSG":"vult","FSTPL":"volumus","SNDPL":"vultis","TRDPL":"volunt"}
velleImpf = {"FSTSG":"volēbam","SNDSG":"volēbas","TRDSG":"volēbat","FSTPL":"volēbamus","SNDPL":"volēbatis","TRDPL":"volēbant"}
velleFutr = {"FSTSG":"volam","SNDSG":"volēs","TRDSG":"volet","FSTPL":"volēmus","SNDPL":"volētis","TRDPL":"volent"}
vellePerf = {"FSTSG":"voluī","SNDSG":"voluisti","TRDSG":"voluit","FSTPL":"voluimus","SNDPL":"voluistis","TRDPL":"voluērunt"}
vellePlup = {"FSTSG":"volueram","SNDSG":"volueras","TRDSG":"voluerat","FSTPL":"volueramus","SNDPL":"volueratis","TRDPL":"voluerant"}
velleFutp = {"FSTSG":"voluero","SNDSG":"volueris","TRDSG":"voluerit","FSTPL":"voluerimus","SNDPL":"volueritis","TRDPL":"voluerint"}
velleConj = {"PRES":vellePres,"IMPF":velleImpf,"FUTR":velleFutr,"PERF":vellePerf,"PLUP":vellePlup,"FUTP":velleFutp}
velleAll = vellePres.values() + velleImpf.values() + velleFutr.values() + vellePerf.values() + vellePlup.values() + velleFutp.values()

nollePresV = ['pos'+x if x[0]=='s' else 'pot'+x for x in vellePres]
nolleImpfV = ['nō'+x[2:] for x in velleImpf]
nolleFutrV = ['nō'+x[2:] for x in velleFutr]
nollePerfV = ['nō'+x[2:] for x in vellePerf]
nollePlupV = ['nō'+x[2:] for x in vellePlup]
nolleFutpV = ['nō'+x[2:] for x in velleFutp]
nollePres = dict(zip(VERB_FORM_KEYS,nollePresV)) 
nolleImpf = dict(zip(VERB_FORM_KEYS,nolleImpfV)) 
nolleFutr = dict(zip(VERB_FORM_KEYS,nolleFutrV)) 
nollePerf = dict(zip(VERB_FORM_KEYS,nollePerfV)) 
nollePlup = dict(zip(VERB_FORM_KEYS,nollePlupV)) 
nolleFutp = dict(zip(VERB_FORM_KEYS,nolleFutrV)) 
nolleAll = nollePres.values() + nolleImpf.values() + nolleFutr.values() + nollePerf.values() + nollePlup.values() + nolleFutp.values()

ferrePres = {"FSTSG":"fero","SNDSG":"fers","TRDSG":"fert","FSTPL":"ferimus","SNDPL":"fertis","TRDPL":"ferunt"}
ferreImpf = {"FSTSG":"ferēbam","SNDSG":"ferēbas","TRDSG":"ferēbat","FSTPL":"ferēbamus","SNDPL":"ferēbatis","TRDPL":"ferēbant"}
ferreFutr = {"FSTSG":"feram","SNDSG":"ferēs","TRDSG":"feret","FSTPL":"ferēmus","SNDPL":"ferētis","TRDPL":"ferent"}
ferrePerf = {"FSTSG":"tulī","SNDSG":"tulisti","TRDSG":"tulit","FSTPL":"tulimus","SNDPL":"tulistis","TRDPL":"tulērunt"}
ferrePlup = {"FSTSG":"tuleram","SNDSG":"tuleras","TRDSG":"tulerat","FSTPL":"tuleramus","SNDPL":"tuleratis","TRDPL":"tulerant"}
ferreFutp = {"FSTSG":"tulero","SNDSG":"tuleris","TRDSG":"tulerit","FSTPL":"tulerimus","SNDPL":"tuleritis","TRDPL":"tulerint"}
ferreConj = {"PRES":ferrePres,"IMPF":ferreImpf,"FUTR":ferreFutr,"PERF":ferrePerf,"PLUP":ferrePlup,"FUTP":ferreFutp}
ferreAll = ferrePres.values() + ferreImpf.values() + ferreFutr.values() + ferrePerf.values() + ferrePlup.values() + ferreFutp.values()

irregPres = irePres.values()+essePres.values()+possePres.values()+vellePres.values()+nollePres.values()+ferrePres.values()
irregImpf = ireImpf.values()+esseImpf.values()+posseImpf.values()+velleImpf.values()+nolleImpf.values()+ferreImpf.values()
irregFutr = ireFutr.values()+esseFutr.values()+posseFutr.values()+velleFutr.values()+nolleFutr.values()+ferreFutr.values()
irregPerf = irePerf.values()+essePerf.values()+possePerf.values()+vellePerf.values()+nollePerf.values()+ferrePerf.values()
irregPlup = irePlup.values()+essePlup.values()+possePlup.values()+vellePlup.values()+nollePlup.values()+ferrePlup.values()
irregFutp = ireFutp.values()+esseFutp.values()+posseFutp.values()+velleFutp.values()+nolleFutp.values()+ferreFutp.values()
allIrreg = ireAll+esseAll+posseAll+velleAll+nolleAll+ferreAll

# verb endings
endings = {"FSTSG":"o","SNDSG":"s","TRDSG":"t","FSTPL":"mus","SNDPL":"tis","TRDPL":"nt"}
endingsV = {"FSTSG":"m","SNDSG":"s","TRDSG":"t","FSTPL":"mus","SNDPL":"tis","TRDPL":"nt"}
perfEndings = {"FSTSG":"ī","SNDSG":"isti","TRDSG":"it","FSTPL":"imus","SNDPL":"istis","TRDPL":"erunt"}
plupEndings = {"FSTSG":"eram","SNDSG":"eras","TRDSG":"erat","FSTPL":"eramus","SNDPL":"eratis","TRDPL":"erant"}
futpEndings = {"FSTSG":"ero","SNDSG":"eris","TRDSG":"erit","FSTPL":"erimus","SNDPL":"eritis","TRDPL":"erint"}

# -------------------------------------------------------------
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
# -------------------------------------------------------------
# VERBS
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
		return ireConj[tense][form]

	if inf == "esse":
		return esseConj[tense][form]

	if inf == "posse":
		temp = irregular("esse", "fuī", per, num, tense)
		if tense == "PRES" or tense == "IMPF" or tense == "FUTR":
			if temp[0] == "s":
				return "pos"+temp
			elif temp[0] == "e":
				return "pot"+temp
		else:
			return "pot"+temp[1:]

	if inf == "velle":
		return velleConj[tense][form]
		
	if inf == "nōlle":
		temp = irregular("velle", "voluī", per, num, tense)
		if tense == "PRES" and (form in ["SNDSG", "TRDSG", "SNDPL"]):
				return "non"+temp
		else:
			return "nō"+temp[2:]

	if inf == "ferre":
		return ferreConj[tense][form]

# takes infinitive, perfective, type, number, person, tense
def conjugate(inf, perf, t, per, num, tense):
	# active  voice
	if inf in irreg:
		# print('hi')
		return irregular(inf,perf,per,num,tense)
	elif tense == "PRES":
		# print('hi1')
		return presentTense(inf,t,per,num)
	elif tense == "IMPF":
		# print('hi2')
		return imperfectTense(inf,t,per,num)
	elif tense == "FUTR":
		# print('hi3')
		return futureTense(inf,t,per,num)
	elif tense == "PERF":
		# print('hi4')
		return perfectTense(perf,t,per,num)
	elif tense == "PLUP":
		# print('hi5')
		return pluperfectTense(perf,t,per,num)
	elif tense == "FUTP":
		# print('hi6')
		return futureperfectTense(perf,t,per,num)
	# else:
		# print('hi7')
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
		if not (inf in Roots.LatinV_inf): 		#ere 3rd IO/5th
			inf = root[:-4]+"ere"
			# print('hi5a')

	elif root[-3:] == "ant":
		tense = "PRES"
		inf = root[:-2]+"re" 	#are 1st
		# print('hi6')
	elif root[-4:] == "iunt":
		tense = "PRES"
		inf = root[:-3]+"re" 	#ire 4th
		if not (inf in Roots.LatinV_inf): 		#ere 3rd IO/5th
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
			tense = "PRES" 						# in 2nd conj

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

def findTenseIrreg(root):
	form = ""
	tense = ""
	if root in ireAll:
		inf = "ire"
		if root in irePres:
			tense = "PRES"
			form = irePres.keys()[irePres.values().index(root)]
		elif root in ireImpf:
			tense = "IMPF"
			form = ireImpf.keys()[ireImpf.values().index(root)]
		elif root in ireFutr:
			tense = "FUTR"
			form = ireFutr.keys()[ireFutr.values().index(root)]
		elif root in irePerf:
			tense = "PERF"
			form = irePerf.keys()[irePerf.values().index(root)]
		elif root in irePlup:
			tense = "PLUP"
			form = irePlup.keys()[irePlup.values().index(root)]
		elif root in ireFutp:
			tense = "FUTP"
			form = ireFutp.keys()[ireFutp.values().index(root)]
	elif root in esseAll:
		inf = "esse"
		if root in essePres:
			tense = "PRES"
			form = essePres.keys()[essePres.values().index(root)]
		elif root in esseImpf:
			tense = "IMPF"
			form = esseImpf.keys()[esseImpf.values().index(root)]
		elif root in esseFutr:
			tense = "FUTR"
			form = esseFutr.keys()[esseFutr.values().index(root)]
		elif root in essePerf:
			tense = "PERF"
			form = essePerf.keys()[essePerf.values().index(root)]
		elif root in essePlup:
			tense = "PLUP"
			form = essePlup.keys()[essePlup.values().index(root)]
		elif root in esseFutp:
			tense = "FUTP"
			form = esseFutp.keys()[esseFutp.values().index(root)]
	elif root in posseAll:
		inf = "posse"
		if root in possePres:
			tense = "PRES"
			form = possePres.keys()[possePres.values().index(root)]
		elif root in posseImpf:
			tense = "IMPF"
			form = posseImpf.keys()[posseImpf.values().index(root)]
		elif root in posseFutr:
			tense = "FUTR"
			form = posseFutr.keys()[posseFutr.values().index(root)]
		elif root in possePerf:
			tense = "PERF"
			form = possePerf.keys()[possePerf.values().index(root)]
		elif root in possePlup:
			tense = "PLUP"
			form = possePlup.keys()[possePlup.values().index(root)]
		elif root in posseFutp:
			tense = "FUTP"
			form = posseFutp.keys()[posseFutp.values().index(root)]
	elif root in velleAll:
		inf = "velle"
		if root in vellePres:
			tense = "PRES"
			form = vellePres.keys()[vellePres.values().index(root)]
		elif root in velleImpf:
			tense = "IMPF"
			form = velleImpf.keys()[velleImpf.values().index(root)]
		elif root in velleFutr:
			tense = "FUTR"
			form = velleFutr.keys()[velleFutr.values().index(root)]
		elif root in vellePerf:
			tense = "PERF"
			form = vellePerf.keys()[vellePerf.values().index(root)]
		elif root in vellePlup:
			tense = "PLUP"
			form = vellePlup.keys()[vellePlup.values().index(root)]
		elif root in velleFutp:
			tense = "FUTP"
			form = velleFutp.keys()[velleFutp.values().index(root)]
	elif root in nolleAll:
		inf = "nōlle"
		if root in nollePres:
			tense = "PRES"
			form = nollePres.keys()[nollePres.values().index(root)]
		elif root in nolleImpf:
			tense = "IMPF"
			form = nolleImpf.keys()[nolleImpf.values().index(root)]
		elif root in nolleFutr:
			tense = "FUTR"
			form = nolleFutr.keys()[nolleFutr.values().index(root)]
		elif root in nollePerf:
			tense = "PERF"
			form = nollePerf.keys()[nollePerf.values().index(root)]
		elif root in nollePlup:
			tense = "PLUP"
			form = nollePlup.keys()[nollePlup.values().index(root)]
		elif root in nolleFutp:
			tense = "FUTP"
			form = nolleFutp.keys()[nolleFutp.values().index(root)]
	elif root in ferreAll:
		inf = "ferre"
		if root in ferrePres:
			tense = "PRES"
			form = ferrePres.keys()[ferrePres.values().index(root)]
		elif root in ferreImpf:
			tense = "IMPF"
			form = ferreImpf.keys()[ferreImpf.values().index(root)]
		elif root in ferreFutr:
			tense = "FUTR"
			form = ferreFutr.keys()[ferreFutr.values().index(root)]
		elif root in ferrePerf:
			tense = "PERF"
			form = ferrePerf.keys()[ferrePerf.values().index(root)]
		elif root in ferrePlup:
			tense = "PLUP"
			form = ferrePlup.keys()[ferrePlup.values().index(root)]
		elif root in ferreFutp:
			tense = "FUTP"
			form = ferreFutp.keys()[ferreFutp.values().index(root)]

	num = form[-2:]
	per = form[:-2]
	perf = Roots.findPerfI(inf)
	return [inf,perf,per,num,tense]

def reverseConjugate(word):
	perf = False
	if word in allIrreg:
		return findTenseIrreg(word)

	elif word[-3:] == "mus":
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

# -------------------------------------------------------------
# -------------------------------------------------------------
# NOUNS
# -------------------------------------------------------------
# DECLENSION

def fstDecl(nom, gen, gender, num, case):
	# always feminine or masculine, same forms for both
	if num == "SG":
		if case == "NOM":
			return nom
		elif case == "GEN":
			return gen
		elif case == "DAT":
			return gen
		elif case == "ACC":
			return gen[:-2]+"am"
		elif case == "ABL":
			return gen[:-2]+"ā"
		elif case == "VOC":
			return nom

	elif num == "PL":
		if case == "NOM":
			return gen
		elif case == "GEN":
			return gen[:-2]+"ārum"
		elif case == "DAT":
			return gen[:-2]+"īs"
		elif case == "ACC":
			return gen[:-2]+"ās"
		elif case == "ABL":
			return gen[:-2]+"īs"
		elif case == "VOC":
			return gen

def sndDecl(nom, gen, gender, num, case):
	# always masculine or neuter	
	if gender == "N":
		if num == "SG":
			if case == "NOM":
				return nom
			elif case == "GEN":
				return gen
			elif case == "DAT":
				return gen[:-1]+"ō"
			elif case == "ACC":
				return nom
			elif case == "ABL":
				return gen[:-1]+"ō"
			elif case == "VOC":
				return nom

		elif num == "PL":
			if case == "NOM":
				return gen[:-1]+"a"
			elif case == "GEN":
				return gen[:-1]+"ōrum"
			elif case == "DAT":
				return gen[:-1]+"īs"
			elif case == "ACC":
				return gen[:-1]+"a"
			elif case == "ABL":
				return gen[:-1]+"īs"
			elif case == "VOC":
				return gen[:-1]+"a"

	elif gender == "M":
		if num ==  "SG":
			if case == "NOM":
				return nom
			elif case == "GEN":
				return gen
			elif case == "DAT":
				return gen[:-1]+"ō"
			elif case == "ACC":
				return gen[:-1]+"um"
			elif case == "ABL":
				return gen[:-1]+"ō"
			elif case == "VOC":
				if nom[-3:] == "ius":
					return gen[:-3]+"ī"
				elif nom[-2:] == "us":
					return gen[:-2]+"e"
				else:
					return nom

		elif num == "PL":
			if case == "NOM":
				return gen
			elif case == "GEN":
				return gen[:-2]+"ōrum"
			elif case == "DAT":
				return gen[:-2]+"īs"
			elif case == "ACC":
				return gen[:-2]+"ōs"
			elif case == "ABL":
				return gen[:-2]+"īs"
			elif case == "VOC":
				return gen

# def trdDecl(nom, gen, gender, num, case):
	# masculine and feminine share same forms; neuter is different

def forDecl(nom, gen, gender, num, case):
	# masculine and feminine share same forms; neuter is different
	if gender == "N":
		if num == "SG":
			if case == "NOM":
				return nom
			elif case == "GEN":
				return gen
			elif case == "DAT":
				return gen[:-2]+"ū"
			elif case == "ACC":
				return gen[:-2]+"ū"
			elif case == "ABL":
				return gen[:-2]+"ū"
			elif case == "VOC":
				return gen[:-2]+"ū"
		elif num == "PL":
			if case == "NOM":
				return gen[:-2]+"ua"
			elif case == "GEN":
				return gen[:-2]+"uum"
			elif case == "DAT":
				return gen[:-2]+"ibus"
			elif case == "ACC":
				return gen[:-2]+"ua"
			elif case == "ABL":
				return gen[:-2]+"ibus"
			elif case == "VOC":
				return gen[:-2]+"ua"
	else:
		if num == "SG":
			if case == "NOM":
				return nom
			elif case == "GEN":
				return gen
			elif case == "DAT":
				return gen[:-2]+"uī"
			elif case == "ACC":
				return gen[:-2]+"um"
			elif case == "ABL":
				return gen[:-2]+"ū"
			elif case == "VOC":
				return gen[:-2]+"us"
		elif num == "PL":
			if case == "NOM":
				return gen[:-2]+"ūs"
			elif case == "GEN":
				return gen[:-2]+"uum"
			elif case == "DAT":
				return gen[:-2]+"ibus"
			elif case == "ACC":
				return gen[:-2]+"ūs"
			elif case == "ABL":
				return gen[:-2]+"ibus"
			elif case == "VOC":
				return gen[:-2]+"ūs"

def fthDecl(nom, gen, gender, num, case):
	# mostly feminine, but masculine shares same forms; no neuter
	# i with macron (ī) is treated as 2 characters
	if num == "SG":
		if case == "NOM":
			return nom
		elif case == "GEN":
			return gen
		elif case == "DAT":
			return gen
		elif case == "ACC":
			return gen[:-3]+"em"
		elif case == "ABL":
			return gen[:-3]+"ē"
		elif case == "VOC":
			return gen[:-3]+"ēs"
	elif num == "PL":
		if case == "NOM":
			return gen[:-3]+"ēs"
		elif case == "GEN":
			return gen[:-3]+"ērum"
		elif case == "DAT":
			return gen[:-3]+"ēbus"
		elif case == "ACC":
			return gen[:-3]+"ēs"
		elif case == "ABL":
			return gen[:-3]+"ēbus"
		elif case == "VOC":
			return gen[:-3]+"ēs"

# takes nominativeS, genitiveS, declension d, number, person, tense
def decline(nom, gen, d, gender, case, num):
	if d == '1':
		return fstDecl(nom,gen,gender,num,case)
	elif d == '2':
		return sndDecl(nom,gen,gender,num,case)
	# elif d == '3':
		# return trdDecl(nom,gen,d,num,case)
	elif d == '4':
		return forDecl(nom,gen,gender,num,case)
	elif d == '5':
		return fthDecl(nom,gen,gender,num,case)

# -------------------------------------------------------------
