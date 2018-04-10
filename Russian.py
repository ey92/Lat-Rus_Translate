# Elizabeth Yam ey92
# -*- coding: utf-8 -*-
import Roots

vowLow = ['а','е','ё','и','о','у','ы','э','ю','я']
vowCap = ['А','Е','Ё','И','О','У','Ы','Э','Ю','Я']
vow = vowLow+vowCap
consLow = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','ъ','ь']
consCap = ['Б','В','Г','Д','Ж','З','Й','К','Л','М','Н','П','Р','С','Т','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ь']
consPal = ['ж','ц','ч','ш','щ']
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
VERB_FORM_KEYS = ['FSTSG', 'SNDSG', 'TRDSG', 'FSTPL', 'SNDPL', 'TRDPL']
PAST_VERB_KEYS = ['M','F','N','PL']

# irregular verb conjugations
irreg = ['мочь','дать','есть','брать','класть','ждать','жить','ехать','идти','хотеть']
mochPreslst = ['могу','можешь','может','можем','можете','могут']
mochFutplst = ['смогу','сможешь','сможет','сможем','сможете','смогут']
mochImpflst = ['мог','могла','могло','могли']
mochPerflst = ['смог','смогла','смогло','смогли']
mochPres = dict(zip(VERB_FORM_KEYS,mochPreslst))
mochFutp = dict(zip(VERB_FORM_KEYS,mochFutplst))
mochImpf = dict(zip(PAST_VERB_KEYS,mochImpflst))
mochPerf = dict(zip(PAST_VERB_KEYS,mochPerflst))
mochConj = {'PRES':mochPres,'FUTP':mochFutp,'IMPF':mochImpf,'PERF':mochPerf}
mochAll = mochPreslst+mochFutplst+mochImpflst+mochPerflst

datPreslst = ['даю','даёшь','даёт','даём','даёте','дают']
datFutplst = ['дам','дашь','даст','дадим','дадите','дадут']
datImpflst = ['давал','давала','давало','давали']
datPerflst = ['дал','дала','дало','дали']
datPres = dict(zip(VERB_FORM_KEYS,datPreslst))
datFutp = dict(zip(VERB_FORM_KEYS,datFutplst))
datImpf = dict(zip(PAST_VERB_KEYS,datImpflst))
datPerf = dict(zip(PAST_VERB_KEYS,datPerflst))
datConj = {'PRES':datPres,'FUTP':datFutp,'IMPF':datImpf,'PERF':datPerf}
datAll = datPreslst+datFutplst+datImpflst+datPerflst

estPreslst = ['ем','ешь','ест','едим','едите','едят']
estFutplst = ['съем','съешь','съест','съедим','съедите','съедят']
estImpflst = ['ел','ела','ело','ели']
estPerflst = ['съел','съели','съела','съело']
estPres = dict(zip(VERB_FORM_KEYS,estPreslst))
estFutp = dict(zip(VERB_FORM_KEYS,estFutplst))
estImpf = dict(zip(PAST_VERB_KEYS,estImpflst))
estPerf = dict(zip(PAST_VERB_KEYS,estPerflst))
estConj = {'PRES':estPres,'FUTP':estFutp,'IMPF':estImpf,'PERF':estPerf}
estAll = estPreslst+estFutplst+estImpflst+estPerflst

bratPreslst = ['беру','берёшь','берёт','берём','берёте','берут']
bratFutplst = ['возьму','возьмёшь','возьмёт','возьмём','возьмёте','возьмут']
bratImpflst = ['брал','брала','брало','брали']
bratPerflst = ['взял','взяла','взяло','взяли']
bratPres = dict(zip(VERB_FORM_KEYS,bratPreslst))
bratFutp = dict(zip(VERB_FORM_KEYS,bratFutplst))
bratImpf = dict(zip(PAST_VERB_KEYS,bratImpflst))
bratPerf = dict(zip(PAST_VERB_KEYS,bratPerflst))
bratConj = {'PRES':bratPres,'FUTP':bratFutp,'IMPF':bratImpf,'PERF':bratPerf}
bratAll = bratPreslst+bratFutplst+bratImpflst+bratPerflst

klastPreslst = ['кладу','кладёшь','кладёт','кладём','кладёте','кладут']
klastFutplst = ['положу','положишь','положит','положим','положите','положат']
klastImpflst = ['клал','клала','клало','клали']
klastPerflst = ['положил','положила','положило','положили']
klastPres = dict(zip(VERB_FORM_KEYS,klastPreslst))
klastFutp = dict(zip(VERB_FORM_KEYS,klastFutplst))
klastImpf = dict(zip(PAST_VERB_KEYS,klastImpflst))
klastPerf = dict(zip(PAST_VERB_KEYS,klastPerflst))
klastConj = {'PRES':klastPres,'FUTP':klastFutp,'IMPF':klastImpf,'PERF':klastPerf}
klastAll = klastPreslst+klastFutplst+klastImpflst+klastPerflst

zhdatPreslst = ['жду','ждёшь','ждёт','ждём','ждёте','ждут']
zhdatFutplst = ['подожду','подождёшь','подождёт','подождём','подождёте','подождут']
zhdatImpflst = ['ждал','ждала','ждало','ждали']
zhdatPerflst = ['подождал','подождала','подождало','подождали']
zhdatPres = dict(zip(VERB_FORM_KEYS,zhdatPreslst))
zhdatFutp = dict(zip(VERB_FORM_KEYS,zhdatFutplst))
zhdatImpf = dict(zip(PAST_VERB_KEYS,zhdatImpflst))
zhdatPerf = dict(zip(PAST_VERB_KEYS,zhdatPerflst))
zhdatConj = {'PRES':zhdatPres,'FUTP':zhdatFutp,'IMPF':zhdatImpf,'PERF':zhdatPerf}
zhdatAll = zhdatPreslst+zhdatFutplst+zhdatImpflst+zhdatPerflst

zhitPreslst = ['живу','живёшь','живёт','живём','живёте','живут']
zhitFutplst = ['проживу','проживёшь','проживёт','проживём','проживёте','проживут']
zhitImpflst = ['жил','жила','жило','жили']
zhitPerflst = ['прожил','прожила','прожило','прожили']
zhitPres = dict(zip(VERB_FORM_KEYS,zhitPreslst))
zhitFutp = dict(zip(VERB_FORM_KEYS,zhitFutplst))
zhitImpf = dict(zip(PAST_VERB_KEYS,zhitImpflst))
zhitPerf = dict(zip(PAST_VERB_KEYS,zhitPerflst))
zhitConj = {'PRES':zhitPres,'FUTP':zhitFutp,'IMPF':zhitImpf,'PERF':zhitPerf}
zhitAll = zhitPreslst+zhitFutplst+zhitImpflst+zhitPerflst

exatPreslst = ['еду','едешь','едет','едем','едете','едут']
exatFutplst = ['поеду','поедешь','поедет','поедем','поедете','поедут']
exatImpflst = ['ехал','ехала','ехало','ехали']
exatPerflst = ['поехал','поехала','поехало','поехали']
exatPres = dict(zip(VERB_FORM_KEYS,exatPreslst))
exatFutp = dict(zip(VERB_FORM_KEYS,exatFutplst))
exatImpf = dict(zip(PAST_VERB_KEYS,exatImpflst))
exatPerf = dict(zip(PAST_VERB_KEYS,exatPerflst))
exatConj = {'PRES':exatPres,'FUTP':exatFutp,'IMPF':exatImpf,'PERF':exatPerf}
exatAll = exatPreslst+exatFutplst+exatImpflst+exatPerflst

idtiPreslst = ['иду','идёшь','идёт','идём','идёте','идут']
idtiFutplst = ['пойду','пойдёшь','пойдёт','пойдём','пойдёте','пойдут']
idtiImpflst = ['шёл','шла','шло','шли']
idtiPerflst = ['пошёл','пошла','пошло','пошли']
idtiPres = dict(zip(VERB_FORM_KEYS,idtiPreslst))
idtiFutp = dict(zip(VERB_FORM_KEYS,idtiFutplst))
idtiImpf = dict(zip(PAST_VERB_KEYS,idtiImpflst))
idtiPerf = dict(zip(PAST_VERB_KEYS,idtiPerflst))
idtiConj = {'PRES':idtiPres,'FUTP':idtiFutp,'IMPF':idtiImpf,'PERF':idtiPerf}
idtiAll = idtiPreslst+idtiFutplst+idtiImpflst+idtiPerflst

xotetPreslst = ['хочу','хочешь','хочет','хотим','хотите','хотят']
xotetFutplst = ['захочу','захочешь','захочет','захотим','захотите','захотят']
xotetImpflst = ['хотел','хотела','хотело','хотели']
xotetPerflst = ['захотел','захотела','захотело','захотели']
xotetPres = dict(zip(VERB_FORM_KEYS,xotetPreslst))
xotetFutp = dict(zip(VERB_FORM_KEYS,xotetFutplst))
xotetImpf = dict(zip(PAST_VERB_KEYS,xotetImpflst))
xotetPerf = dict(zip(PAST_VERB_KEYS,xotetPerflst))
xotetConj = {'PRES':xotetPres,'FUTP':xotetFutp,'IMPF':xotetImpf,'PERF':xotetPerf}
xotetAll = xotetPreslst+xotetFutplst+xotetImpflst+xotetPerflst

irregPres = mochPreslst+datPreslst+estPreslst+bratPreslst+klastPreslst+zhdatPreslst+zhitPreslst+exatPreslst+idtiPreslst+xotetPreslst
irregFutp = mochFutplst+datFutplst+estFutplst+bratFutplst+klastFutplst+zhdatFutplst+zhitFutplst+exatFutplst+idtiFutplst+xotetFutplst
irregImpf = mochImpflst+datImpflst+estImpflst+bratImpflst+klastImpflst+zhdatImpflst+zhitImpflst+exatImpflst+idtiImpflst+xotetImpflst
irregPerf = mochPerflst+datPerflst+estPerflst+bratPerflst+klastPerflst+zhdatPerflst+zhitPerflst+exatPerflst+idtiPerflst+xotetPerflst
irregAll = irregPres+irregFutp+irregImpf+irregPerf

# verb endings
endings1vlst = ['ю','ешь','ет','ем','ете','ют']
endings1clst = ['у','ёшь','ёт','ём','ёте','ут']
endings1cplst = ['у','ешь','ет','ем','ете','ут']
endings2vlst = ['ю','ишь','ит','им','ите','ят']
endings2clst = ['у','ишь','ит','им','ите','ат']
endingsPastlst = ['л','ла','ло','ли']
endingsFuturelst = ['буду_','будешь_','будет_','будем_','будете_','будут_']
endings1v = dict(zip(VERB_FORM_KEYS,endings1vlst))
endings1c = dict(zip(VERB_FORM_KEYS,endings1clst))
endings1cp = dict(zip(VERB_FORM_KEYS,endings1cplst))
endings2v = dict(zip(VERB_FORM_KEYS,endings2vlst))
endings2c = dict(zip(VERB_FORM_KEYS,endings2clst))
endingsPast = dict(zip(PAST_VERB_KEYS,endingsPastlst))
endingsFuture = dict(zip(VERB_FORM_KEYS,endingsFuturelst))

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
			if stem[-2:] in consPal:
				end = endings1cp[form]
			else:
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

def pastTense(inf, t, gender, num, perf):
	form = num if num=='PL' else gender
	end = endingsPast[form]

	# stem for past tense is infinitive without 'ть' ending
	stem = inf[:-4]

	return stem+end

def futureTense(inf, t, per, num):
	form = per+num
	return endingsFuture[form]+inf

def irregular(inf, per, num, gender, tense):
	if tense == 'FUTR':
		return futureTense(inf,'ir',per,num)
	
	form = ''
	if tense in ['IMPF','PERF']:
		if num == 'SG':
			form = gender
		elif num == 'PL':
			form = num
	else:
		form = per+num

	if inf == 'мочь':
		return mochConj[tense][form]
	elif inf == 'дать':
		return datConj[tense][form]
	elif inf == 'есть':
		return estConj[tense][form]
	elif inf == 'брать':
		return bratConj[tense][form]
	elif inf == 'класть':
		return klastConj[tense][form]
	elif inf == 'ждать':
		return zhdatConj[tense][form]
	elif inf == 'жить':
		return zhitConj[tense][form]
	elif inf == 'ехать':
		return exatConj[tense][form]
	elif inf == 'идти':
		return idtiConj[tense][form]
	elif inf == 'хотеть':
		return xotetConj[tense][form]

# takes either infinitive form, person, number, and tense
def conjugate (inf, per, num, gender, tense):
	# check for irreg verbs
	impf_inf = inf
	if inf in Roots.RussianV_perf_inf:
			impf_inf = Roots.RfindIInfP(inf)
	if impf_inf in irreg:
		return irregular(impf_inf,per,num,gender,tense)

	# FUTR same for all verbs
	# rqures impf inf
	if tense == 'FUTR':
		perf = False

		# find impf inf if given perf inf
		if inf in Roots.RussianV_perf_inf:
			inf = Roots.RfindIInfP(inf)

		# if impf inf
		if inf in Roots.RussianV_impf_inf:
			# t = conjugation
			t = Roots.RfindIConjIInf(inf)
			return futureTense(inf,t,per,num)

	# PRES,IMPF need impf inf
	elif tense in ['PRES','IMPF']:
		perf = False

		# find impf inf if given perf inf
		if inf in Roots.RussianV_perf_inf:
			inf = Roots.RfindIInfP(inf)
		
		# if impf inf
		if inf in Roots.RussianV_impf_inf:
			# t = conjugation
			t = Roots.RfindIConjIInf(inf)

			if tense == 'PRES':
				return nonPastTense(inf,t,per,num,perf)
			elif tense == 'IMPF':
				return pastTense(inf,t,gender,num,perf)

	# PERF, FUTP tenses need PERF inf
	elif tense in ['PERF','FUTP']:
		perf = True

		# find impf inf if given
		if inf in Roots.RussianV_impf_inf:
			inf = Roots.RfindPInfI(inf)

		# inf perf inf
		if inf in Roots.RussianV_perf_inf:
			# t = conjugation
			t = Roots.RfindPConjPInf(inf)

			if tense == 'PERF':
				return pastTense(inf,t,gender,num,perf)
			elif tense == 'FUTP':
				return nonPastTense(inf,t,per,num,perf)

# -------------------------------------------------------------
# REVERSE CONJUGATION

def findRoot(stem):
	P3 = ''
	inf = ''
	pinf = ''
	perf = False

	# stem ends in palalatalized consonant
	P3form = 'TRDPL'
	if stem[-2:] in (consPal):
		# try 1st conj
		P3 = stem+endings1c[P3form]
		# try 2nd conj
		if not P3 in Roots.RussianV_3p:
			P3 = stem+endings2c[P3form]

	# stem ends in non-palatalized consonant
	else:
		# try 1st conj
		P3 = stem+endings1v[P3form]
		# try 2nd conj
		if not P3 in Roots.RussianV_3p:
			P3 = stem+endings2v[P3form]

	if P3 in Roots.RussianV_impf_3p:
		inf = Roots.RfindIInf3PI(P3)
		pinf = Roots.RfindPInfI(inf)
		perf = False
	elif P3 in Roots.RussianV_perf_3p:
		pinf = Roots.RfindPInf3PP(P3)
		inf = Roots.RfindIInfP(pinf)
		perf = True

	return (inf,pinf,perf)

# finds per/num form and inf
def findForm(root):
	per = ''
	num = ''
	stem = ''

	# 1S
	if root[-2:] in ['у','ю']:
		per = 'FST'
		num = 'SG'
		stem = root[:-2]

	# 2S
	elif root[-4:] == 'шь':
		per = 'SND'
		num = 'SG'
		stem = root[:-6]

	# 3S
	elif root[-4:] in ['ет','ит','ёт']:
		per = 'TRD'
		num = 'SG'
		stem = root[:-4]

	# 1P
	elif root[-2:] == 'м':
		per = 'FST'
		num = 'PL'
		stem = root[:-4]

	# 2P
	elif root[-4:] == 'те':
		per = 'SND'
		num = 'PL'
		stem = root[:-6]

	# 3P
	elif root[-4:] in ['ут','ат','ют','ят']:
		per = 'TRD'
		num = 'PL'
		stem = root[:-4]

	(inf,pinf,perf) = findRoot(stem)
	return (inf,pinf,per,num,perf)

def futrFindForm(root):
	gender = ''
	tense = 'FUTR'
	ind = root.index('_')
	pref = root[:ind]
	
	(inf,pinf,per,num,perf) = findForm(pref)
	inf = root[ind+1:] 
	
	pinf = Roots.RfindPInfI(inf)
	return [inf,pinf,per,num,gender,tense]

def nonpastFindForm(root):
	gender = ''
	(inf,pinf,per,num,perf) = findForm(root)

	tense = 'FUTP' if perf else 'PRES'

	return [inf,pinf,per,num,gender,tense]

def pastFindForm(root):
	per = 'FST/SND/TRD'
	gender = ''
	num = ''
	stem = ''
	tense = ''
	inf = ''
	pinf = ''
	
	if root[-2:] == 'л':
		gender = 'M'
		num = 'SG'
		stem = root[:-2]
	elif root[-4:] == 'ла':
		gender = 'F'
		num = 'SG'
		stem = root[:-4]
	elif root[-4:] == 'ло':
		gender = 'N'
		num = 'SG'
		stem = root[:-4]
	elif root[-4:] == 'ли':
		gender = 'M/F/N'
		num = 'PL'
		stem = root[:-4]

	inf = stem+'ть'
	if inf not in Roots.RussianV_inf:
		inf = stem+'ти'

	if inf in Roots.RussianV_impf_inf:
		tense = 'IMPF'
		pinf = Roots.RfindPInfI(inf)
	elif inf in Roots.RussianV_perf_inf:
		tense = 'PERF'
		pinf = inf
		inf = Roots.RfindIInfP(pinf)

	return [inf,pinf,per,num,gender,tense]

# def revIrregular(root):

def reverseConjugate(word):
	if '_' in word:
		return futrFindForm(word)
	elif word[-2:] in ['у','ю','м'] or word[-4:] in ['шь','ет','ит','ёт','те','ут','ат','ют','ят']:
		return nonpastFindForm(word)
	elif word[-2:] == 'л' or word[-4:] in ['ла','ло','ли']:
		return pastFindForm(word)

# -------------------------------------------------------------
# -------------------------------------------------------------
# NOUNS
# -------------------------------------------------------------
# DECLENSION

# takes nomS, case, number
# def decline(nom, case, num, d=None, gender=None):