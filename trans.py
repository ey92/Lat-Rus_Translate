# Elizabeth Yam ey92
# -*- coding: utf-8 -*-
import Roots
import Latin
import Russian

# -------------------------------------------------------------
# TRANSLATE VERBS

# find Russian verb infinitive from Latin verb infinitive
def RLvRoot(rinf):
	return Roots.VMap_lat[Roots.VMap_rus.index(rinf)]

# find Latin verb infinitive from Russian verb infinitive
def LRvRoot(linf):
	return Roots.VMap_rus[Roots.VMap_lat.index(linf)]

# translate Russian verb into Latin verb
def RLVerb(rus_verb):
	# deconstruct Russian form
	(rinf,pinf,per,num,gender,tense) = Russian.reverseConjugate(rus_verb)
	
	# look up Latin root
	linf = RLvRoot(rinf)

	# if Russian verb in past form, default to 3rd person
	if len(per) > 3:
		per = 'TRD'
	
	# construct Latin form
	return Latin.conjugate(linf,per,num,tense)

# translate Latin verb into Russian verb
# default to male gender if none provided
def LRVerb(lat_verb, gender='M'):
	# deconstruct Latin form
	(linf,perf,per,num,tense) = Latin.reverseConjugate(lat_verb)
	
	# look up Russian root
	rinf = LRvRoot(linf)
	
	# pluperfect tense doesn't exist in Russian, so closest tense is perfect tense
	if tense == 'PLUP':
		tense = 'PERF'
	
	# construct Russian form
	return Russian.conjugate(rinf,per,num,gender,tense)

# -------------------------------------------------------------
# TRANSLATE NOUNS

# find Latin genitive singular from Russian nominative singular
def RLnRoot(rnom):
	return Roots.NMap_lat[Roots.NMap_rus.index(rnom)]

# find Russian nominative singular from Latin genitive
def LRnRoot(lgen):
	return Roots.NMap_rus[Roots.NMap_lat.index(lgen)]

# translate Russian noun to Latin noun
def RLNoun(rus_noun, accconstr=False):
	# deconstruct Russian form
	(rnoms,rgenp,case,num) = Russian.reverseDecline(rus_noun)

	# if multiple possible cases, pick one, in order of preference as listed below
	if len(case) > 3:
		if 'NOM' in case:
			case = 'NOM'
		elif 'ACC' in case:
			case = 'ACC'
		elif 'GEN' in case:
			case = 'GEN'
		elif 'PRP' in case:
			case = 'PRP'
		elif 'DAT' in case:
			case = 'DAT'
		# only pick INS if that is the only choice
	
	# the Russian Instrumental is often the "Ablative of means" construction in Latin
	# the Prepositional cases must be found from context, so we require additional input in those cases
	# most of the Prepositional uses in Russian align with Ablative uses in Latin
	if case in ['INS','PRP']:
		case = 'ABL'

	if case == 'ABL' and accconstr:
		case = 'ACC'

	# look up Latin root
	lgen = RLnRoot(rnoms)
	# look up Latin nominative form from genitive form
	lnom = Roots.LfindNomG(lgen)

	# construct Latin form
	return Latin.decline(lnom,lgen,case,num)

# translate Latin noun to Russian noun
def LRNoun(lat_noun, insconstr=False):
	# deconstruct Latin form
	(lnom,lgen,case,num) = Latin.reverseDecline(lat_noun)

	# if multiple possible cases, pick one, in order of preference as listed below
	if len(case) > 3:
		if 'NOM' in case:
			case = 'NOM'
		elif 'ACC' in case:
			case = 'ACC'
		elif 'GEN' in case:
			case = 'GEN'
		elif 'ABL' in case:
			case = 'ABL'
		elif 'DAT' in case:
			case = 'DAT'
		# only pick VOC if that is the only choice
		# VOC is only used in direct speech, and thus the least likely to be used

	# Russians address each other by the nominative form of their names
	if case == 'VOC':
		case = 'NOM'

	# many Ablative uses in Latin align with Prepositional uses in Russian
	# the Russian Instrumental is a subset of the Latin Ablative ("Ablative of means"), 
	#   so this can only be determined from context, requiring additional input to the function
	if case == 'ABL':
		if insconstr:
			case = 'INS'
		else:
			case = 'PRP'

	# look up Russian root
	rnom = LRnRoot(lgen)

	#check for animacy
	animate = Roots.RisAnimateG(rnom)
	if case == 'ACC' and animate:
		case = 'GEN'

	# construct Russian form
	return Russian.decline(rnom,case,num)

# -------------------------------------------------------------
# TRANSLATE ADJECTIVES

# find Latin adjective masculine nominative singular from Russian adjective masculine nominative singular
def RLaRoot(rnomM):
	return (Roots.AMap_lat[Roots.AMap_rus.index(rnomM)])

# find Russian adjective masculine nominative singular from Latin adjective masculine nominative singular
def LRaRoot(lnomM):
	return (Roots.AMap_rus[Roots.AMap_lat.index(lnomM)])

# translate Russian adjective to Latin adjective
def RLAdj(rus_adj, accconstr=False, noun_case=None):
	case = ''

	# deconstruct Russian form
	(rnomM, case, num, gender) = Russian.reverseDeclineA(rus_adj)

	# always copy the noun's case if known
	if noun_case != None:
		case = noun_case

	else:
		# if multiple possible cases, pick one, in order of preference as listed below
		if len(case) > 3:
			if 'NOM' in case:
				case = 'NOM'
			elif 'ACC' in case:
				case = 'ACC'
			elif 'GEN' in case:
				case = 'GEN'
			elif 'PRP' in case:
				case = 'PRP'
			elif 'DAT' in case:
				case = 'DAT'
			# only pick INS if that is the only choice

		# the Russian Instrumental is often the "Ablative of means" construction in Latin
		# the Prepositional cases must be found from context, so we require additional input in those cases
		# most of the Prepositional uses in Russian align with Ablative uses in Latin
		if case in ['INS','PRP']:
			case = 'ABL'

		if case == 'ABL' and accconstr:
			case = 'ACC'

	# look up Latin nomM
	lnomM = RLaRoot(rnomM)

	# look up Latin adj root form
	lroot = Roots.LfindRootNM(lnomM)

	# look up Latin adj decl
	ldecl = Roots.LfindDeclR(lroot)

	# construct Latin form
	return Latin.declineA(lnomM,lroot,ldecl,gender,case,num)

# translate Russian adjective to Latin adjective
# assume not animate
def LRAdj(lat_adj, accconstr=False, noun_gender='M', noun_case=None, animate=False):
	case = ''

	# deconstruct Latin form
	(lnom, lrt, case, num, lgender) = Latin.reverseDeclineA(lat_adj)

	# always copy the noun's case if known
	if noun_case != None:
		case = noun_case

	else:
		# if multiple possible cases, pick one, in order of preference as listed below
		if len(case) > 3:
			if 'NOM' in case:
				case = 'NOM'
			elif 'ACC' in case:
				case = 'ACC'
			elif 'GEN' in case:
				case = 'GEN'
			elif 'ABL' in case:
				case = 'ABL'
			elif 'DAT' in case:
				case = 'DAT'
			# only pick VOC if that is the only choice
			# VOC is only used in direct speech, and thus the least likely to be used

		# Russians address each other by the nominative form of their names
		if case == 'VOC':
			case = 'NOM'

		# check for case change with animacy
		if case == 'ACC' and animate:
			case = 'GEN'

		# many Ablative uses in Latin align with Prepositional uses in Russian
		# the Russian Instrumental is a subset of the Latin Ablative ("Ablative of means"), 
		#   so this can only be determined from context, requiring additional input to the function
		if case == 'ABL':
			if insconstr:
				case = 'INS'
			else:
				case = 'PRP'

	# look up Russian nomM
	rnomM = LRaRoot(lnom)

	# should require noun's gender, otherwise guess from latin noun's gender
	# rgender = lgender if noun_gender == None else noun_gender

	return Russian.declineA(rnomM,rgender,case,num,animate)
