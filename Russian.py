# Elizabeth Yam ey92
# -*- coding: utf-8 -*-
import Roots

vowLow = ['а','е','ё','и','о','у','ы','э','ю','я']
vowCap = ['А','Е','Ё','И','О','У','Ы','Э','Ю','Я']
vowStr = ['а́','е́','ё','и́','о́','у́','ы́','э́','ю́','я́']
vow = vowLow+vowCap
allVow = vow+vowStr
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
DECL_FORM_KEYS = ['NOM','GEN','DAT','ACC','PRP','INS']
DECL_ENDG_KEYSSG = ['NOMSG','GENSG','DATSG','ACCSG','PRPSG','INSSG']
DECL_ENDG_KEYSPL = ['NOMPL','GENPL','DATPL','ACCPL','PRPPL','INSPL']

# irregular verb conjugations
irreg = ['мочь','давать','есть','брать','класть','ждать','жить','ехать','идти','хотеть']
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

# decl endings, default inanimate
endingsN00sglst = ['0','а','у','0','е','ом']
endingsN00pllst = ['ы','ов','ам','ы','ах','ами']
endingsNaasglst = ['а','ы','е','у','е','ой']
endingsNaapllst = ['ы','0','ам','ы','ах','ами']
endingsNoosglst = ['о','а','у','о','е','ом']
endingsNoopllst = ['а','0','ам','а','ах','ами']
endingsNmzsglst = ['ь','и','и','ь','и','ью']
endingsNmzpllst = ['и','ей','ям','и','ях','ями']
endingsNiisglst = ['я','и','и','я','и','ем']
endingsNiipllst = ['а','0','ам','а','ах','ами']
endingsN00sg = dict(zip(DECL_ENDG_KEYSSG,endingsN00sglst))
endingsN00pl = dict(zip(DECL_ENDG_KEYSPL,endingsN00pllst))
endingsNaasg = dict(zip(DECL_ENDG_KEYSSG,endingsNaasglst))
endingsNaapl = dict(zip(DECL_ENDG_KEYSPL,endingsNaapllst))
endingsNoosg = dict(zip(DECL_ENDG_KEYSSG,endingsNoosglst))
endingsNoopl = dict(zip(DECL_ENDG_KEYSPL,endingsNoopllst))
endingsNmzsg = dict(zip(DECL_ENDG_KEYSSG,endingsNmzsglst))
endingsNmzpl = dict(zip(DECL_ENDG_KEYSPL,endingsNmzpllst))
endingsNiisg = dict(zip(DECL_ENDG_KEYSSG,endingsNiisglst))
endingsNiipl = dict(zip(DECL_ENDG_KEYSPL,endingsNiipllst))
endingsN00 = endingsN00sg.copy()
endingsN00.update(endingsN00pl)
endingsNaa = endingsNaasg.copy()
endingsNaa.update(endingsNaapl)
endingsNoo = endingsNoosg.copy()
endingsNoo.update(endingsNoopl)
endingsNmz = endingsNmzsg.copy()
endingsNmz.update(endingsNmzpl)
endingsNii = endingsNiisg.copy()
endingsNii.update(endingsNiipl)

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
	elif inf == 'давать':
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

def revIrregular(root):
	form = ''
	tense = ''
	gender = ''
	per = ''
	num = ''
	if root in mochAll:
		inf = 'мочь'
		if root in mochPreslst:
			tense = 'PRES'
			form = mochPres.keys()[mochPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in mochFutplst:
			tense = 'FUTP'
			form = mochFutp.keys()[mochFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in mochImpflst:
			tense = 'IMPF'
			form = mochImpf.keys()[mochImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in mochPerflst:
			tense = 'PERF'
			form = mochPerf.keys()[mochPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in datAll:
		inf = 'давать'
		if root in datPreslst:
			tense = 'PRES'
			form = datPres.keys()[datPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in datFutplst:
			tense = 'FUTP'
			form = datFutp.keys()[datFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in datImpflst:
			tense = 'IMPF'
			form = datImpf.keys()[datImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in datPerflst:
			tense = 'PERF'
			form = datPerf.keys()[datPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in estAll:
		inf = 'есть'
		if root in estPreslst:
			tense = 'PRES'
			form = estPres.keys()[estPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in estFutplst:
			tense = 'FUTP'
			form = estFutp.keys()[estFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in estImpflst:
			tense = 'IMPF'
			form = estImpf.keys()[estImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in estPerflst:
			tense = 'PERF'
			form = estPerf.keys()[estPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in bratAll:
		inf = 'брать'
		if root in bratPreslst:
			tense = 'PRES'
			form = bratPres.keys()[bratPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in bratFutplst:
			tense = 'FUTP'
			form = bratFutp.keys()[bratFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in bratImpflst:
			tense = 'IMPF'
			form = bratImpf.keys()[bratImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in bratPerflst:
			tense = 'PERF'
			form = bratPerf.keys()[bratPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in klastAll:
		inf = 'класть'
		if root in klastPreslst:
			tense = 'PRES'
			form = klastPres.keys()[klastPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in klastFutplst:
			tense = 'FUTP'
			form = klastFutp.keys()[klastFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in klastImpflst:
			tense = 'IMPF'
			form = klastImpf.keys()[klastImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in klastPerflst:
			tense = 'PERF'
			form = klastPerf.keys()[klastPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in zhdatAll:
		inf = 'ждать'
		if root in zhdatPreslst:
			tense = 'PRES'
			form = zhdatPres.keys()[zhdatPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in zhdatFutplst:
			tense = 'FUTP'
			form = zhdatFutp.keys()[zhdatFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in zhdatImpflst:
			tense = 'IMPF'
			form = zhdatImpf.keys()[zhdatImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in zhdatPerflst:
			tense = 'PERF'
			form = zhdatPerf.keys()[zhdatPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in zhitAll:
		inf = 'жить'
		if root in zhitPreslst:
			tense = 'PRES'
			form = zhitPres.keys()[zhitPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in zhitFutplst:
			tense = 'FUTP'
			form = zhitFutp.keys()[zhitFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in zhitImpflst:
			tense = 'IMPF'
			form = zhitImpf.keys()[zhitImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in zhitPerflst:
			tense = 'PERF'
			form = zhitPerf.keys()[zhitPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in exatAll:
		inf = 'ехать'
		if root in exatPreslst:
			tense = 'PRES'
			form = exatPres.keys()[exatPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in exatFutplst:
			tense = 'FUTP'
			form = exatFutp.keys()[exatFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in exatImpflst:
			tense = 'IMPF'
			form = exatImpf.keys()[exatImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in exatPerflst:
			tense = 'PERF'
			form = exatPerf.keys()[exatPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in idtiAll:
		inf = 'идти'
		if root in idtiPreslst:
			tense = 'PRES'
			form = idtiPres.keys()[idtiPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in idtiFutplst:
			tense = 'FUTP'
			form = idtiFutp.keys()[idtiFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in idtiImpflst:
			tense = 'IMPF'
			form = idtiImpf.keys()[idtiImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in idtiPerflst:
			tense = 'PERF'
			form = idtiPerf.keys()[idtiPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
	elif root in xotetAll:
		inf = 'хотеть'
		if root in xotetPreslst:
			tense = 'PRES'
			form = xotetPres.keys()[xotetPres.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in xotetFutplst:
			tense = 'FUTP'
			form = xotetFutp.keys()[xotetFutp.values().index(root)]
			num = form[-2:]
			per = form[:-2]
		elif root in xotetImpflst:
			tense = 'IMPF'
			form = xotetImpf.keys()[xotetImpf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form
		elif root in xotetPerflst:
			tense = 'PERF'
			form = xotetPerf.keys()[xotetPerf.values().index(root)]
			if form == 'PL':
				num = form
			else:
				num = 'SG'
				gender = form

	perfinf = Roots.RfindPInfI(inf)
	return [inf, perfinf, per, num, gender, tense]

def reverseConjugate(word):
	if '_' in word:
		return futrFindForm(word)
	elif word in irregAll:
		return revIrregular(word)
	elif word[-2:] in ['у','ю','м'] or word[-4:] in ['шь','ет','ит','ёт','те','ут','ат','ют','ят']:
		return nonpastFindForm(word)
	elif word[-2:] == 'л' or word[-4:] in ['ла','ло','ли']:
		return pastFindForm(word)

# -------------------------------------------------------------
# -------------------------------------------------------------
# NOUNS
# -------------------------------------------------------------
# DECLENSION

def contains(string, lst):
	for e in lst:
		if e in string:
			return True
	return False

def ztoe(word):
	return word.replace('0','')

# more phonological changes, independent of gender or declension
def generalPhon(word):
	if word[-2:] == 'ы' and word[-4:-2] in ['г','к','х','ж','ч','ш','щ']:
		word = word[:-2]+'и'
	elif word[-2:] == 'о' and word[-4:-2] in ['ж','ч','ш','щ','ц']:
		word = word[:-2]+'е'
	elif word[-2:] == 'я' and word[-4:-2] in ['г','к','х','ж','ч','ш','щ','ц']:
		word = word[:-2]+'а'
	elif word[-2:] == 'ю' and word[-4:-2] in ['г','к','х','ж','ч','ш','щ','ц']:
		word = word[:-2]+'у'
	# vowels include palatal indicators when appended to stem
	word = word.replace('ьа','я').replace('ьу','ю').replace('ье','е').replace('ьо','ё').replace('ьы','и')
	word = word.replace('йа','я').replace('йу','ю').replace('йе','е').replace('йы','и')

	return word

# includes noun and adj, having stressed syllables important
def findGenP(nom, d, gender):
	root = ''
	gen = ''

	# find stem, depending on the declension
	if d[:2] == 'aa':
		root = nom[:-2]
		if gender == None:
			gender = 'F'
	elif d[:2] == '00':
		root = nom
		if gender == None:
			gender = 'M'
	elif d[:2] == 'oo':
		root = nom[:-2]
		if gender == None:
			gender = 'N'
	elif d[:2] == 'mz':
		root = nom[:-2]
		gen = root+'ей'
		if gender == None:
			gender = 'F'

	# find the appropriate ending, depending on the gender
	if gender == 'F':
		if nom[-2:] == 'а':
			gen = root
		elif nom[-4:-2] in vow and nom[-2:] == 'я':
			gen = root+'й'
		elif nom[-4:-2] in cons and nom[-2:] == 'я':
			gen = root+'ь'
		if d[:2] != 'mz' and root[-4:-2] in cons and root[-2:] in cons:
			gen = root[:-2]+'е'+root[-2:]
	elif gender == 'M':
		# stress is also a 2-char 'letter'
		if nom[-2:] in ['й','ь'] and nom[-6:-2] in vowStr:
			gen = root+'ев'
		elif nom[-2:] in ['ж','ч','ш','щ','ь']:
			gen = root+'ей'
		else:
			gen = root+'ов'
	elif gender == 'N':
		if nom[-4:] == 'ие':
			gen = nom[:-4]+'ий'
		elif nom[-2:] == 'е':
			gen = nom+'й'
		elif nom[-2:] == 'о':
			gen = nom[:-2]

	return generalPhon(gen)

# phonological changes to nominative plural case endings
def nomPlPhon(noms, gender):
	root = noms[:-2]
	nomp = ''

	# normal nomP endings
	if gender == 'M':
		if noms[-2:] == 'й':
			nomp = root+'и'
		elif noms[-2:] == 'ь':
			nomp = root+'и'
		else:
			root = noms
			nomp = root+'ы'
	elif gender == 'F':
		if noms[-2:] == 'а':
			nomp = root+'ы'
		elif noms[-2:] in 'я':
			nomp = root+'и'
	elif gender == 'N':
		if noms[-2:] == 'о':
			nomp = root+'а'
		elif noms[-2:] == 'е':
			nomp = root+'я'

	return generalPhon(nomp)

# phonological changes to instrumental singular case endings for M/F
def insSgPhon(noms, gender):
	root = ''
	inss = ''

	if gender == 'F':
		root = noms[:-2]
		if root[-2:] in ['ж','ч','ц','ш','щ'] and not (root[-6:-2] in vowStr):
			inss = root+'ей'
		elif noms[-2:] == 'я' and noms[-4:-2] in [e for e in Russian.vowLow if e!='ё']:
			inss = root+'ей'
		elif noms[-2:] == 'я' and (noms[-6:-2] in vowStr or noms[-4:-2] == 'ё'):
			inss = root+'ёй'
		else:
			inss = root+'ой'
	elif gender == 'M':
		root = noms
		if root[-2:] in ['ж','ч','ц','ш','щ'] and not (root[-6:-2] in vowStr):
			inss = root+'ем'
		# elif noms[-2:] in ['й','ь'] and (noms[-6:-2] in vowStr or noms[-4:-2] == 'ё'):
		elif noms[-2:] in ['ь'] and (noms[-6:-2] in vowStr or noms[-4:-2] == 'ё' or not contains(noms,allVow)):
			inss = root[:-2]+'ём'
		elif noms[-2:] in ['й','ь']:
			inss = root+'ем'
		else:
			inss = root+'ом'
	return inss

def aDecl(nom, gen, gender, case, num, animate):
	form = case+num
	root = nom[:-2]

	if form == 'ACCPL':
		form = 'GENPL' if animate == 'a' else 'NOMPL'

	if form == 'NOMPL':
		return nomPlPhon(nom, gender)
	elif form == 'NOMSG':
		return nom
	elif form == 'GENPL':
		return gen
	elif form == 'INSSG':
		return insSgPhon(nom, gender)
	else:
		return generalPhon(ztoe(root+endingsNaa[form]))

def zDecl(nom, gen, gender, case, num, animate):
	form = case+num
	root = nom

	if (num == 'PL' and Roots.RfindDeclG(gen)[3] == 'p') or (Roots.RfindDeclG(gen)[3] == 'r'):
		root = Roots.RfindRootG(gen)

	if case == 'ACC':
		case = 'GEN' if animate == 'a' else 'NOM'
		form = case+num

	if form == 'NOMPL':
		# for irregular nom/acc plurals ending in 'а'
		if Roots.RfindDeclG(gen)[3] in ['n','p']:
			return nomPlPhon(root+'о','N')
		else:
			return nomPlPhon(root, gender)
	elif form == 'NOMSG':
		return nom
	elif form == 'GENPL':
		return gen
	elif form == 'INSSG':
		return insSgPhon(root, gender)
	else:
		# print(ztoe(endingsN00[form]))
		return generalPhon(ztoe(root+endingsN00[form]))

def oDecl(nom, gen, gender, case, num, animate):
	form = case+num
	root = nom[:-2]
	if case == 'ACC':
		case = 'GEN' if animate == 'a' else 'NOM'
		form = case+num

	if form == 'NOMPL':
		return nomPlPhon(nom, gender)
	elif form == 'NOMSG':
		return nom
	elif form == 'GENPL':
		return gen
	else:
		return generalPhon(ztoe(root+endingsN00[form]))

def mzDecl(nom, gen, gender, case, num, animate):
	form = case+num
	root = nom[:-2]
	if form == 'ACCPL':
		form = 'GENPL' if animate == 'a' else 'NOMPL'

	# if form == 'NOMPL':
	# 	return nomPlPhon(nom, gender)
	# elif form == 'NOMSG':
	if form == 'NOMSG':
		return nom
	elif form == 'GENPL':
		return gen
	else:
		# minor phonology changes
		return ztoe(root+endingsNmz[form]).replace('щя','ща').replace('ця','ца')

def iDecl(nom, gen, gender, case, num, animate):
	form = case+num
	root = Roots.RfindRootG(gen)

	if case == 'ACC':
		case = 'GEN' if animate == 'a' else 'NOM'
		form = case+num

	if form == 'NOMSG':
		return nom
	elif form == 'GENPL':
		return gen
	else:
		return generalPhon(ztoe(root+endingsNii[form]))

# takes nomS, case, number
def decline(nom, case, num, d=None, gender=None):
	try:
		gen = Roots.RfindGenN(nom)
		nom = Roots.RfindNomN(nom)
	except:
		gen = findGenP(nom,d,gender)
		# continue

	try:
		d = Roots.RfindDeclG(gen) if d == None else d+'  '
		gender = Roots.RfindGenderG(gen) if gender == None else gender
	except:
		return 'Declension or gender doesn\'t exist'

	if d[:2] == 'aa':
		return aDecl(nom,gen,gender,case,num,d[2])
	elif d[:2] == '00':
		return zDecl(nom,gen,gender,case,num,d[2])
	elif d[:2] == 'oo':
		return oDecl(nom,gen,gender,case,num,d[2])
	elif d[:2] == 'mz':
		return mzDecl(nom,gen,gender,case,num,d[2])
	elif d[:2] == 'ii':
		return iDecl(nom,gen,gender,case,num,d[2])

# -------------------------------------------------------------
# REVERSE DECLENSION

# def findRoot(word,end):

def findDeclNomPGenS(root):
	# could be zero declension M/N NomPlural, or ь declension NomPlural or a declension NomPlural/GenSingular
	if root[-2:] in ['и','ы']:
		# if zero declension M
		noms = root[:-2]
		case = "NOM"
		num = "PL"
		
		# i declension -> find word by root
		if noms in Roots.RussianN2_root:
			case = "GEN"
			num = "SG"
			noms = Roots.RfindNomR(noms)
		# if zero declension N 
		if not (noms in Roots.RussianN2_ns):
			noms = root[:-2]+'о'
			# if ь declension F NomPlural
			if not (noms in Roots.RussianN2_ns):
				noms = root[:-2]+'ь'
				if noms in Roots.RussianN_root:
					noms = Roots.RfindNomR(noms)
				# nominative plural is more likely than genitive singular for a declension
				elif not (noms in Roots.RussianN2_ns):
					noms = root[:-2]+'а'
		gen = Roots.RfindGenN(noms)
		if not (Roots.RisAnimateG(gen)) and case == "NOM":
			case = "NOM/ACC"
	# nominative singular for a declension should have been taken care of already
	# should only be zero declension M/N GenSingular
	elif root[-2:] == 'а':
		case = "GEN"
		num = "SG"
		noms = root[:-2]
		
		if noms in Roots.RussianN2_root:
			case = "NOM"
			num = "PL"
			noms = Roots.RfindNomR(noms)
		# if zero declension N, more common as nom/accPl
		if not (noms in Roots.RussianN2_ns):
			case = "NOM"
			num = "PL"
			noms = noms+'о'
	
		gen = Roots.RfindGenN(noms)
		if not (Roots.RisAnimateG(gen)):
			case = "NOM/ACC"
	
		else:
			case = "GEN/ACC"

	# i declension -> find word by root
	elif root[-2:] == 'я':
		noms = root[:-2]+'ь'
		case = "NOM"
		num = "PL"
		if not (noms in Roots.RussianN2_ns) and (noms in Roots.RussianN_root):
			noms = Roots.RfindNomR(noms)
			gen = Roots.RfindGenN(noms)
			# print(Roots.RfindDeclG)
			if Roots.RfindDeclG(gen)[3] == 'r':
				case = "GEN"
				num = "SG"

	return [noms,gen,case,num]

def findDeclDatS(root):
	case = "DAT"
	num = "SG"
	nom = ''
	gen = ''
	# if zero declension, nom drop ending
	nom = root[:-2]
	if not (nom in Roots.RussianN2_ns):
		if nom+'ь' in Roots.RussianN_root:
			nom = Roots.RfindNomR(nom+'ь')
		else:
			# if N, append 'о'
			nom = nom+'о'
			# only other case for ending in 'у' is inanimate F a-declension accusative
			if not (nom in Roots.RussianN2_ns):
				nom = nom[:-2]+'ь'
				if nom in Roots.RussianN_root:
					nom = Roots.RfindNomR(nom)
				else:
					nom = nom[:-2]+'а'
					case = "ACC" 	# set dative to be default case for a declension
	# ь declension has ending 'и', but more common as nom/acc pl

	gen = Roots.RfindGenN(nom)
	return [nom,gen,case,num]

def findDeclPrpS(root):
	case = "PRP"
	num = "SG"
	nom = ''
	gen = ''

	# if zero declension, nom drop ending
	nom = root[:-2]
	# if a declension, is actually dative
	if not (nom in Roots.RussianN2_ns):
		if nom+'ь' in Roots.RussianN_root:
			nom = Roots.RfindNomR(nom+'ь')
		else:
			nom = nom+'о'
			if not (nom in Roots.RussianN2_ns):
				nom = nom[:-2]+'а'
				case = "DAT/PRP" 	# set dative to be default case for a declension
	# ь declension has ending 'и', but more common as nom/acc pl

	gen = Roots.RfindGenN(nom)
	return [nom,gen,case,num]

def findDeclInsS(root):
	case = "INS"
	num = "SG"
	nom = ''
	gen = ''

	# zero declension M or NOM
	if root[-4:] == 'ом':
		# if M, no ending
		nom  = root[:-4]
		# if N, add ending 'о'
		if not (nom in Roots.RussianN2_ns):
			nom = nom+'о'
	# a declension
	elif root[-4:] == 'ой':
		nom = root[:-4]+'а'
	# a decl (rare) or usuall ь declension
	elif root[-4:] == 'ью':
		nom = root[:-4]+'а'
		if not (nom in Roots.RussianN2_ns):
			nom = root[:-4]+'ь'
	# ём as a result of phonology
	elif root[-4:] == 'ём':
		nom = root[:-4]+'ь'
		if nom in Roots.RussianN_root:
			nom = Roots.RfindNomR(nom)
		elif not (nom in Roots.RussianN2_ns):
			nom = root[-4:]+'й'
	# should only be in i decl, which requires diff root
	elif root[-4:] == 'ем':
		nom = root[:-4]
		if root[:-4] in Roots.RussianN_root:
			nom = Roots.RfindNomR(nom)

	gen = Roots.RfindGenN(nom)
	return [nom,gen,case,num]

def findDeclDatP(root):
	case = "DAT"
	num = "PL"
	nom = ''
	gen = ''

	if root[-4:] == 'ам':
		# i declension -> find word by root
		if root[:-4] in Roots.RussianN2_root:
			nom = Roots.RfindNomR(root[:-4])
		# zero declension M -> find noms by dropping ending
		elif root[:-4] in Roots.RussianN2_ns:
			nom = root[:-4]
		# a declension -> keep the a in the ending
		elif root[:-2] in Roots.RussianN2_ns:
			nom = root[:-2]
		# zero declension N -> find noms by dropping ending and adding 'о'
		elif (root[:-4]+'о') in Roots.RussianN2_ns:
			nom = root[:-4]+'о'
		# ь declension F -> drop ending and add 'ь'
		elif (root[:-4]+'ь') in Roots.RussianN2_ns:
				nom = root[:-4]+'ь'
	# this would only happen as a result of phonology - ending in 'й' or 'ь'
	elif root[-4:] == 'ям':
		# if # decl M, ends in 'й'
		if (root[:-4]+'й') in Roots.RussianN2_ns:
			nom = root[:-4]+'й'
		elif (root[:-4]+'ь') in Roots.RussianN2_root:
			nom = Roots.RfindNomR(root[:-4]+'ь')
		# if ь declension, ends in 'ь'
		elif (root[:-4]+'ь') in Roots.RussianN2_ns:
			nom = root[:-4]+'ь'

	gen = Roots.RfindGenN(nom)
	return [nom,gen,case,num]

def findDeclPrpP(root):
	case = "PRP"
	num = "PL"
	nom = ''
	gen = ''
	
	if root[-4:] == 'ах':
		# i declension -> find word by root
		if root[:-4] in Roots.RussianN2_root:
			nom = Roots.RfindNomR(root[:-4])
		# zero declension M -> find noms by dropping ending
		elif root[:-4] in Roots.RussianN2_ns:
			nom = root[:-4]
		# a declension -> keep the a in the ending; could be dative
		elif root[:-4]+'а' in Roots.RussianN2_ns:
			nom = root[:-2]
		# zero declension N -> find noms by dropping ending and adding 'о'
		elif (root[:-4]+'о') in Roots.RussianN2_ns:
			nom = root[:-4]+'о'
		# ь declension F -> find noms by dropping ending and adding 'ь'
		elif (root[:-4]+'ь') in Roots.RussianN2_ns:
			nom = root[:-4]+'ь'
	# this would only happen as a result of phonology - ending in 'й' or 'ь'
	elif root[-4:] == 'ях':
		# if zero decl M, ends in 'й'
		if (root[:-4]+'й') in Roots.RussianN2_ns:
			nom = root[:-4]+'й'
		elif (root[:-4]+'ь') in Roots.RussianN_root:
			nom = Roots.RfindNomR(root[:-4]+'ь')
		# if ь declension, ends in 'ь'
		elif (root[:-4]+'ь') in Roots.RussianN2_ns:
			nom = root[:-4]+'ь'

	gen = Roots.RfindGenN(nom)
	return [nom,gen,case,num]

def findDeclInsP(root):
	case = "INS"
	num = "PL"
	nom = ''
	gen = ''

	if root[-6:] == 'ами':
		# i declension -> find word by root
		if root[:-6] in Roots.RussianN2_root:
			nom = Roots.RfindNomR(root[:-6])
		# zero declension M -> find noms by dropping ending
		elif root[:-6] in Roots.RussianN2_ns:
			nom = root[:-6]
		# a declension -> keep the a in the ending
		elif root[:-4] in Roots.RussianN2_ns:
			nom = root[:-4]
		# zero declension N -> find noms by dropping ending and adding 'о'
		elif (root[:-6]+'о') in Roots.RussianN2_ns:
			nom = root[:-6]+'о'
		# ь declension N -> find noms by dropping ending and adding 'ь'
		elif (root[:-6]+'ь') in Roots.RussianN2_ns:
			nom = root[:-6]+'ь'
	# this would only happen as a result of phonology - ending in 'й' or 'ь'
	elif root[-6:] == 'ями':
		# if # decl M, ends in 'й'
		if (root[:-6]+'й') in Roots.RussianN2_ns:
			nom = root[:-6]+'й'
		elif (root[:-6]+'ь') in Roots.RussianN_root:
			nom = Roots.RfindNomR(root[:-6]+'ь')
		# if ь declension, ends in 'ь'
		elif (root[:-6]+'ь') in Roots.RussianN2_ns:
			nom = root[:-6]+'ь'

	gen = Roots.RfindGenN(nom)
	return [nom,gen,case,num]

def findDeclGenP(root):
	case = "GEN"
	num = "PL"
	gen = root
	nom = Roots.RfindNomG(gen)
	if Roots.RisAnimateG(gen):
		case = "GEN/ACC"

	return [nom,gen,case,num]

def findDeclNomS(root):
	case = "NOM"
	num = "SG"
	nom = root
	gen = Roots.RfindGenN(nom)
	if not (Roots.RisAnimateG(gen)) and Roots.RfindDeclG(gen)[0]!='a':
		case = "NOM/ACC"

	return [nom,gen,case,num]

def reverseDecline(word):
	if word in Roots.RussianN2_ns:
		# print('finddecl1')
		return findDeclNomS(word)	
	elif word in Roots.RussianN2_gp:
		# print('finddecl2')
		return findDeclGenP(word)	
	elif word[-6:] in ['ами','ями']:
		# print('finddecl3')
		return findDeclInsP(word)	
	elif word[-4:] in ['ах','ях']:
		# print('finddecl4')
		return findDeclPrpP(word)	
	elif word[-4:] in ['ам','ям']:
		# print('finddecl5')
		return findDeclDatP(word)	
	elif word[-4:] in ['ом','ой','ью','ём', 'ем']:
		# print('finddecl6')
		return findDeclInsS(word)	
	elif word[-2:] == 'е':
		# print('finddecl7')
		return findDeclPrpS(word)	
	elif word[-2:] in ['у','ю']:
		# print('finddecl8')
		return findDeclDatS(word)	
	elif word[-2:] in ['ы','и','а','я']:
		# print('finddecl9')
		return findDeclNomPGenS(word)

# -------------------------------------------------------------
# -------------------------------------------------------------
# ADJECTIVES
# -------------------------------------------------------------
# DECLENSION

# takes nomM, genitive/nomF (root), declension d, gender, case, number
# def declineA(nomM, root, d, gender, case, num):
