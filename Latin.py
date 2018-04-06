# Elizabeth Yam ey92
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
		inf = Roots.LfindInfP(perf)
	else: 
		perf = Roots.LfindPerfI(inf)
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
		inf = Roots.LfindInfP(perf)
	else: 
		# print(inf)
		perf = Roots.LfindPerfI(inf)
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
		inf = Roots.LfindInfP(perf)
	else: 
		# print(inf)
		perf = Roots.LfindPerfI(inf)
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
		inf = Roots.LfindInfP(perf)
	else: 
		# print(inf)
		perf = Roots.LfindPerfI(inf)
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
		inf = Roots.LfindInfP(perf)
	else: 
		# print(inf)
		perf = Roots.LfindPerfI(inf)
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
		inf = Roots.LfindInfFS(root)

	if (perf):
		if tense == "PERF":
			perf = root
		elif root[-4] == "e":
			perf = root[:-4]+"ī"
		elif root[-3] == "e":
			perf = root[:-3]+"ī"
		inf = Roots.LfindInfP(perf)
	else: 
		# print(inf)
		perf = Roots.LfindPerfI(inf)
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
	perf = Roots.LfindPerfI(inf)
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

def trdDecl(nom, gen, t, gender, num, case):
	# masculine and feminine share same forms; neuter is different
	if gender == "N":
		if num == "SG":
			if case == "NOM":
				return nom
			elif case == "GEN":
				return gen
			elif case == "DAT":
				return gen[:-2]+"ī"
			elif case == "ACC":
				return nom
			elif case == "ABL":
				if t[1] == 'i':
					return gen[:-2]+"ī"
				else:
					return gen[:-2]+"e"
			elif case == "VOC":
				return nom
		elif num == "PL":
			if case == "NOM":
				if t[1] == 'i':
					return gen[:-2]+"ia"
				else:
					return gen[:-2]+"a"
			elif case == "GEN":
				if t[0] == 'i':
					return gen[:-2]+"ium"
				else:
					return gen[:-2]+"um"
			elif case == "DAT":
				return gen[:-2]+"ibus"
			elif case == "ACC":
				if t[1] == 'i':
					return gen[:-2]+"ia"
				else:
					return gen[:-2]+"a"
			elif case == "ABL":
				return gen[:-2]+"ibus"
			elif case == "VOC":
				if t[1] == 'i':
					return gen[:-2]+"ia"
				else:
					return gen[:-2]+"a"
	else:
		if num == "SG":
			if case == "NOM":
				return nom
			elif case == "GEN":
				return gen
			elif case == "DAT":
				return gen[:-2]+"ī"
			elif case == "ACC":
				return gen[:-2]+"em"
			elif case == "ABL":
				if t[1] == 'i':
					return gen[:-2]+"ī"
				else:
					return gen[:-2]+"e"
			elif case == "VOC":
				return nom
		elif num == "PL":
			if case == "NOM":
				return gen[:-2]+"ēs"
			elif case == "GEN":
				if t[0] == 'i':
					return gen[:-2]+"ium"
				else:
					return gen[:-2]+"um"
			elif case == "DAT":
				return gen[:-2]+"ibus"
			elif case == "ACC":
				return gen[:-2]+"ēs"
			elif case == "ABL":
				return gen[:-2]+"ibus"
			elif case == "VOC":
				return gen[:-2]+"ēs"

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

# takes nominativeS, genitiveS, declension d, gender, case, number
def decline(nom, gen, d, gender, case, num):
	if d == '1':
		return fstDecl(nom,gen,gender,num,case)
	elif d == '2':
		return sndDecl(nom,gen,gender,num,case)
	elif d[0] == '3':
		return trdDecl(nom,gen,d[1:],gender,num,case)
	elif d == '4':
		return forDecl(nom,gen,gender,num,case)
	elif d == '5':
		return fthDecl(nom,gen,gender,num,case)

# -------------------------------------------------------------
# REVERSE DECLENSION

def findDeclNomS(root):
	num = "SG"
	case = "NOM"
	gen = ""
	nom = ""

	if root in Roots.LatinN_ns:
		nom = root

	gen = Roots.LfindGenN(nom)
	return [nom,gen,case,num]

def findDeclAccS(root):
	num = "SG"
	case = "ACC"
	gen = ""
	nom = ""

	# 1st decl
	if root[-2:] == "am":
		gen = root[:-2]+"ae"

	# 3rd/5th decl
	elif root[-2:] == "em":
		gen = root[:-2]+"ēī" 					# 5th decl
		if not (gen in Roots.LatinN_gs): 		# 3rd decl
			gen = root[:-2]+"is"

	# 2nd/4th decl
	elif root[-2:] == "um":
		gen = root[:-2]+"ī" 					# 2nd decl
		if gen in Roots.LatinN_gs and Roots.LisNG(gen): 	# if N, more likely nom sg
			return findDeclNomS(root)
		elif not (gen in Roots.LatinN_gs): 		# 4th decl
			gen = root[:-2]+"ūs"

	nom  = Roots.LfindNomG(gen)
	return [nom,gen,case,num]

def findDeclNomAccP(root):
	num = "PL"
	case = "NOM/ACC"
	gen = ""
	nom = ""

	# 1st decl
	if root[-2:] == "ae": 		# 1st decl nom pl
		case = "NOM"
		gen = root
	elif root[-3:] == "ās": 	# 1st decl acc pl
		case = "ACC"
		gen = root[:-3]+"ae"

	# 3rd/5th decl
	elif root[-3:] == "ēs":
		gen = root[:-3]+"is" 				# 3rd decl
		if not (gen in Roots.LatinN_gs): 	# 5th decl
			gen = root[:-3]+"ēī"
	elif root[-2:] == "ia":
		gen = root[:-2]+"is" 	# 3rd decl i stem

	# 4th decl
	elif root[-3:] == "ūs":
		gen = root 				# 4th decl nom/acc pl = gen sg
	elif root[-2:] == "ua": 	# 4th decl N pl
		gen = root[:-2]+"ūs"

	# 2nd decl
	elif root[-2:] == "ī": 		# 2nd decl nom pl
		case = "NOM"
		gen = root 				# 2nd decl nom pl = gen sg
	elif root[-3:] == "ōs": 	# 2nd decl acc pl
		case = "ACC"
		gen = root[:-3]+"ī"
	
	elif root[-1] == "a": 		# 2nd,3rd decl N nom/acc pl
		gen = root[:-1]+"ī" 	# 2nd decl
		if root in Roots.LatinN_ns:
			return findDeclNomS(root)
		if not (gen in Roots.LatinN_gs): 	# in 3rd decl
			gen = root[:-1]+"is"

	nom  = Roots.LfindNomG(gen)
	return [nom,gen,case,num]

def findDeclGenS(root):
	num = "SG"
	case = "GEN"
	gen = ""
	nom = ""

	# 1st decl
	# if root[-2:] == "ae":
		# 1st decl gen "ae" more common as 1st decl nom pl

	# 4th decl
	# elif root[-3:] == "ūs":
		# 4th decl gen "ūs" more common as 4th decl nom pl

	# 5th decl
	if root[-4:] == "ēī":
		gen = root

	# 2nd decl
	elif root[-2:] == "ī":
		# 2nd decl gen "ī" more common as 2nd decl nom pl unless N
		gen = root
		if gen in Roots.LatinN_gs and not (Roots.LisNG(gen)): 	# if not N, go to 2nd decl nom pl
			return findDeclNomAccP(root)

	# 3rd decl
	elif root[-2:] == "is":
		gen = root
		if gen in Roots.LatinN_gs and (gen in Roots.LatinN_ns): 	# if is a nom sg, that is more common
			return findDeclNomS(root)

	nom  = Roots.LfindNomG(gen)
	return [nom,gen,case,num]

def findDeclGenP(root):
	num = "PL"
	case = "GEN"
	gen = ""
	nom = ""

	# 1st decl
	if root[-5:] == "ārum":
		gen = root[:-5]+"ae"

	# 2nd decl
	elif root[-5:] == "ōrum":
		gen = root[:-5]+"ī"

	# 4th decl
	elif root[-3:] == "uum":
		gen = root[:-3]+"ūs"

	# 5th decl
	elif root[-5:] == "ērum":
		gen = root[:-5]+"ēī"

	# 3rd decl
	elif root[-3:] == "ium":
		gen = root[:-3]+"is"
	elif root[-2:] == "um":
		gen = root[:-2]+"is"
		if not (gen in Roots.LatinN_gs): 	# could also be 2nd/4th decl acc sg
			case = "ACC"
			num = "SG"
			gen = root[:-2]+"ūs" 			# 4th decl
			if not(gen in Roots.LatinN_gs): # if 2nd decl
				gen = root[:-2]+"ī"
				if Roots.LisNG(gen): 		# could also be 2nd decl N nom/acc sg
					return findDeclAccS(root)

	nom  = Roots.LfindNomG(gen)
	return [nom,gen,case,num]

def findDeclDAblS(root):
	num = "SG"
	case = "DAT/ABL"
	nom = ""
	gen = ""

	# 1st decl
	if root[-2:] == "ā":
		gen = root[:-2]+"ae" 	# 1st decl gen
		case = "ABL"
	elif root[-2:] == "ae":
		# 1st decl dat "ae" more common as 1st decl nom pl
		return findDeclNomAccP(root)

	# 2nd decl
	elif root[-2:] == "ō": 		# same ending dat/abl
		gen = root[:-2]+"ī" 	# 2nd decl gen

	# 4th decl
	elif root[-2:] == "ū": 		# 4th decl abl
		gen = root[:-2]+"ūs"
		case = "ABL"
	elif root[-3:] == "uī": 	# 4th decl dat
		gen = root[:-3]+"ūs"
		case = "DAT"

	# 5th decl
	elif root[-2:] == "ē": 		# 5th decl abl
		gen = root[:-2]+"ēī"
		case = "ABL"
	# elif root[-4:] == "ēī":
		# 5th decl dat "ēī" more common as 5th decl gen sg

	# 3rd decl
	elif root[-1:] == "e":					# 3rd decl cons and i stem abl
		gen = root[:-1]+"is"
		case = "ABL"
		if not(gen in Roots.LatinN_gs): 	# could also be 2nd decl voc
			case = "VOC"
			gen = root[:-1]+"ī"
	elif root[-2:] == "ī": 		# 3rd decl i stem
		gen = root[:-2]+"is"
		if not (gen in Roots.LatinN_gs): 	# could also be 2nd decl nom pl
			return findDeclGenS(root)
		elif not Roots.Lis3iistemG(gen): 	# 3rd decl ii stem same ending dat/abl
			case = "DAT" 		 			# 3rd decl cons and i stem dat

	nom  = Roots.LfindNomG(gen)
	return [nom,gen,case,num]

def findDeclDAblP(root):
	num = "PL"
	case = "DAT/ABL"
	nom = ""
	gen = ""
	
	# 1st or 2nd decl
	if root[-3:] == "īs":
		gen = root[:-3]+"ae" 		# 1st decl gen
		if not (gen in Roots.LatinN_gs):
			gen = root[:-3]+"ī" 	# 2nd decl gen

	# 3rd or 4th decl
	elif root[-4:] == "ibus":
		gen = root[:-4]+"ūs" 		# 4th decl gen
		if not (gen in Roots.LatinN_gs):
			gen = root[:-4]+"is" 	# 3rd decl gen

	# 5th decl
	elif root[-5:] == "ēbus":
		gen = root[:-5]+"ēī" 		# 5th decl gen

	nom  = Roots.LfindNomG(gen)
	return [nom,gen,case,num]

def reverseDecline(word):
	# NOM SG
	if word in Roots.LatinN_ns:
		return findDeclNomS(word)
	# DAT/ABL PL
	elif (len(word) > 3 and word [-3:] == "īs") or (len(word) > 4 and word[-4:] == "ibus") or (len(word) > 5 and word[-5:] == "ēbus"):
		return findDeclDAblP(word)
	# DAT/ABL SG
	elif word[-2:] in ['ā','ē','ī','ō','ū'] or word[-1] == "e" or (len(word) > 2 and word[-3:] == "uī"):
		return findDeclDAblS(word)
	# GEN PL
	elif (len(word) > 5 and word[-5:] in ["ārum","ērum","ōrum"]) or (len(word) > 3 and word[-3:] in ["ium","uum"]) or word[-2:] == "um":
		return findDeclGenP(word)
	# GEN SG
	elif (len(word) > 3 and word[-4:] == "ēī") or (word[-2:] == "ī" or word[-2:] == "is"):
		return findDeclGenS(word)
	# NOM/ACC PL
	elif (len(word) > 2 and word[-3:] in ["ās","ōs","ēs","ūs"]) or word[-2:] in ["ae","ua","ī"] or word[-1] == "a":
		return findDeclNomAccP(word)
	# ACC SG
	elif word[-2:] in ["am","um","em"]:
		return findDeclAccS(word)
	# NOM SG
	else:
		return findDeclNomS(word)

# -------------------------------------------------------------
# -------------------------------------------------------------
# ADJECTIVES
# -------------------------------------------------------------
# DECLENSION

# takes nomM, genitive/nomF (root), declension d, gender, case, number
def declineA(nomM, root, d, gender, case, num):
	if d == "12":
		if gender == "F":
			d = "1"
			nom = root[:-1]+"a"
			gen = root[:-1]+"ae"
			return decline(nom,gen,d,gender,case,num)
		else:
			d = "2"
			if gender == "M":
				gen = root[:-1]+"ī"
				return decline(nomM,gen,d,gender,case,num)
			elif gender == "N":
				nom = root[:-1]+"um"
				gen = root[:-1]+"ī"
				return decline(nom,gen,d,gender,case,num)
	elif d == "3a":
		if gender == "N":
			d = "3ii"
			nom = root[:-2]+"e"
			gen = root
			return decline(nom,gen,d,gender,case,num)
		else:
			d = "3ii"
			gen = root
			if gender == 'F':
				nom = root
			elif gender == 'M':
				nom = nomM
			return decline(nom,gen,d,gender,case,num)
	elif d == "3b":
		if gender == "N":
			d = "3ii"
			nom = nomM
			gen = root
			return decline(nom,gen,d,gender,case,num)
		else:
			d = "3ii"
			return decline(nomM,root,d,gender,case,num)

# -------------------------------------------------------------
# REVERSE DECLENSION

def findDeclNomSA(root, gender):
	num = "SG"
	case = "NOM"
	gender = "F/M/N" if gender == None else gender
	rt = ""
	nom = ""

	if root in Roots.LatinA_fr:
		rt = root
		nom = Roots.LfindMascR(rt)
	elif root in Roots.LatinN_ns:
		nom = root
		rt = Roots.LfindRootNM(nom)
	elif root[-2:] == "um":
		rt = root[:-2]+"a"
		gender = "N"
	elif root[-1] == "e":
		rt = root[:-1]+"is"
		gender = "N"
	
	return [nom,rt,case,num, gender]

def findDeclAccSA(root, gender):
	num = "SG"
	case = "ACC"
	gender = "F/M/N" if gender == None else gender
	rt = ""
	nom = ""

	# 1st decl
	if root[-2:] == "am":
		rt = root[:-1]
		gender = 'F'

	# 3rd decl
	elif root[-2:] == "em":
		rt = root[:-2]+"is"	# 3rd decl

	# 2nd decl
	elif root[-2:] == "um":
		rt = root[:-2]+"a" 			# if M, must be 2nd decl acc sg
		if gender[0] != 'M': 		# could be nom sg N
			case = "NOM/ACC"
			if len(gender) > 1:
				gender = 'M/N'

	nom  = Roots.LfindMascR(rt)
	return [nom,rt,case,num, gender]

def findDeclNomAccPA(root, gender):
	num = "PL"
	case = "NOM/ACC"
	gender = "F/M/N" if gender == None else gender
	rt = ""
	nom = ""

	# 1st decl
	if root[-2:] == "ae": 		# 1st decl nom pl
		case = "NOM"
		rt = root[:-1]
		gender = "F"
	elif root[-3:] == "ās": 	# 1st decl acc pl
		case = "ACC"
		rt = root[:-3]+"a"
		gender = "F"

	# 3rd decl
	elif root[-3:] == "ēs":
		rt = root[:-3]+"is" 	# 3rd decl
		if len(gender) > 1:
			gender = "F/M"
	elif root[-2:] == "ia":
		rt = root[:-2]+"is" 	# 3rd decl i stem
		gender = "N"

	# 2nd decl
	elif root[-2:] == "ī": 		# 2nd decl nom pl
		case = "NOM"
		rt = root[:-2]+"a"		# 2nd decl nom pl = rt sg
		gender = "M"
	elif root[-3:] == "ōs": 	# 2nd decl acc pl
		case = "ACC"
		rt = root[:-3]+"a"
		gender = "M"
	
	elif root[-1] == "a": 		# 2nd decl nom/acc pl N
		if gender[0] == 'N':
			rt = root 		 		# 2nd decl
		else: 					# 1st decl nom sg F more common
			return findDeclNomSA(root)
		
	nom  = Roots.LfindMascR(rt)
	return [nom,rt,case,num,gender]

def findDeclGenSA(root, gender):
	num = "SG"
	case = "GEN"
	gender = "F/M/N" if gender == None else gender
	gen = ""
	nom = ""

	# 1st decl
	# if root[-2:] == "ae":
		# 1st decl gen "ae" more common as 1st decl nom pl

	# 2nd decl
	if root[-2:] == "ī":
		# 3rd decl dat/abl "ī" should have already been taken care of
		# 2nd decl gen "ī" more common as 2nd decl nom pl unless N
		if gender[0] == "N":
			gen = root[:-2]+"a"
		else: 	# if not N, go to 2nd decl nom pl
			return findDeclNomAccPA(root,gender)

	# 3rd decl
	elif root[-2:] == "is":
		gen = root
		if gen in Roots.LatinN_gs and (gen in Roots.LatinN_ns): 	# if is a nom sg, that is more common
			return findDeclNomSA(root)

	nom  = Roots.LfindMascR(gen)
	return [nom,gen,case,num]

def findDeclGenPA(root, gender):
	num = "PL"
	case = "GEN"
	gender = "F/M/N" if gender == None else gender
	gen = ""
	nom = ""

	# 1st decl
	if root[-5:] == "ārum":
		gen = root[:-5]+"a"
		gender = "F"

	# 2nd decl
	elif root[-5:] == "ōrum":
		gen = root[:-5]+"a"
		if gender[0] == 'F':
			gender = "M/N"

	# 3rd decl
	elif root[-3:] == "ium":
		gen = root[:-3]+"is"

	nom  = Roots.LfindMascR(gen)
	return [nom,gen,case,num,gender]

def findDeclDAblSA(root, gender):
	num = "SG"
	case = "DAT/ABL"
	gender = "F/M/N" if gender == None else gender
	nom = ""
	rt = ""

	# 1st decl
	if root[-2:] == "ā":
		rt = root[:-2]+"a" 	# 1st decl rt
		case = "ABL"
		gender = "F"
	elif root[-2:] == "ae":
		# 1st decl dat "ae" more common as 1st decl nom pl
		return findDeclNomAccPA(root)

	# 2nd decl
	elif root[-2:] == "ō": 		# same ending dat/abl
		rt = root[:-2]+"a" 	# 2nd decl rt
		if gender[0] == 'F':
			gender = "M/N"

	# 3rd decl
	elif root[-2:] == "ī": 		# 3rd decl i stem
		rt = root[:-2]+"is"
		if not (rt in Roots.LatinA_fr): 	# could also be 2nd decl nom pl
			return findDeclGenSA(root,gender)

	nom  = Roots.LfindMascR(rt)
	return [nom,rt,case,num, gender]

def findDeclDAblPA(root, gender):
	num = "PL"
	case = "DAT/ABL"
	gender = "F/M/N" if gender == None else gender
	nom = ""
	rt = ""
	
	# 1st or 2nd decl
	if root[-3:] == "īs":
		rt = root[:-3]+"a" 		# 1st/2nd decl root

	# 3rd decl
	elif root[-4:] == "ibus":
		rt = root[:-4]+"is" 	# 3rd decl rt

	nom  = Roots.LfindMascR(rt)
	return [nom,rt,case,num,gender]

def reverseDeclineA(word, gender=None):
	# NOM SG
	if word in Roots.LatinN_ns:
		return findDeclNomSA(word,gender)
	# DAT/ABL PL
	elif (len(word) > 3 and word [-3:] == "īs") or (len(word) > 4 and word[-4:] == "ibus"):
		return findDeclDAblPA(word,gender)
	# DAT/ABL SG
	elif word[-2:] in ['ā','ī','ō']:
		return findDeclDAblSA(word,gender)
	# GEN PL
	elif (len(word) > 5 and word[-5:] in ["ārum","ōrum"]) or (len(word) > 3 and word[-3:] in ["ium"]):
		return findDeclGenPA(word,gender)
	# GEN SG
	elif word[-2:] == "ī" or word[-2:] == "is":
		return findDeclGenSA(word,gender)
	# NOM/ACC PL
	elif (len(word) > 2 and word[-3:] in ["ās","ōs","ēs"]) or word[-2:] in ["ae","ī"] or word[-1] == "a":
		return findDeclNomAccPA(word,gender)
	# ACC SG
	elif word[-2:] in ["am","um","em"]:
		return findDeclAccSA(word,gender)
	# NOM SG
	else:
		return findDeclNomSA(word,gender)

# -------------------------------------------------------------
# -------------------------------------------------------------
# NOUNS AND ADJECTIVES
# -------------------------------------------------------------
# DECLINE NOUNS AND ADJECTIVES

def declineAN(nom, root, d, gender, case, num, AN):
	if AN == 'A':
		return declineA(nom,root,d,gender,case,num)
	elif AN == 'N':
		return decline(nom,root,d,gender,case,num)

# REVERSE NOUNS AND ADJECTIVES
def reversedeclineAN(word):
	try:
		return reverseDecline(word)+['N']
	except:
		try:
			return reverseDeclineA(word)+['A']
		except:
			return None