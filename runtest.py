# Elizabeth Yam ey92
# -*- coding: utf-8 -*-
import sys
import Roots
import Latin
import Russian
import trans

YCHOICES = ['y','yes']
NCHOICES = ['n','no']
ACHOICES = ['a','again']
YNCHOICES = YCHOICES+NCHOICES+ACHOICES

def transliterateRussian(rus):
	rus = rus.replace('a','а').replace('б','b').replace('в','v').replace('г','g').replace('д','d')
	rus = rus.replace('е','ye').replace('ё','yo').replace('ж','zh').replace('з','z').replace('й','y')
	rus = rus.replace('и','yi').replace('к','k').replace('л','l').replace('м','m').replace('н','n')
	rus = rus.replace('о','o').replace('п','p').replace('р','r').replace('с','s').replace('т','t')
	rus = rus.replace('у','u').replace('ф','f').replace('х','x').replace('ц','ts').replace('ч','ch')
	rus = rus.replace('ш','sh').replace('щ','sh\'').replace('ъ','').replace('ы','i').replace('ь','\'')
	rus = rus.replace('э','e').replace('ю','yu').replace('я','ya')

	return rus

def printList(lst):
	if lst == None:
		print lst

	if len(lst) == 0:
		print lst
	elif len(lst) == 1:
		print('['+lst[0]+']')
	else:
		s = '['+lst[0]
		for i in range(1,len(lst)):
			s += ', '+lst[i]
		s += ']'
		print(s)

def processInput(string, latin=False, verb=False):
	if latin:
		lst = []
		inds = []
		string = string.split(',')
		if verb:
			inds = [0,5]
		else:
			inds = [0,1]
		for i in range(len(string)):
			if i in inds:
				lst.append(Latin.toMacron(string[i].strip()))
			else:
				lst.append(string[i].strip())
		return lst
	else:
		return [p.strip() for p in string.split(',')]

def checkStr(lst):
	for e in lst:
		if type(e) != str:
			return False
	return True

def checkInt(num):
	try:
	    int(num)
	    return True
	except:
	    return False

def cont():
	choice4 = raw_input("Would you like to do more? (y/n/a)\n").lower()
	while choice4 not in YNCHOICES:
		choice4 = raw_input("Would you like to do more? (y/n/a)\n").lower()
	if choice4 in YCHOICES:
		# choice0 = 0
		return 'y'
	elif choice4 in ACHOICES:
		return 'a'
	else:
		sys.exit(0)

def latinConstructNouns():
	# make nouns
	params = []
	while not (len(params) in [4,6]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the nominativeS form, genitiveS form, case, number, [declension, gender], separated by commas\n")).strip()
		params = processInput(params,True, False)

	if len(params) == 4:
		result =  Latin.decline(params[0], params[1], params[2], params[3])

	else:
		# pad declension param with spaces
		if len(params[4]) < 3:
			params[4]+='  '
		result = Latin.decline(params[0], params[1], params[2], params[3], params[4], params[5])
	
	print("\nThe Latin form is:")
	print(result)
	return cont()

def latinConstructVerbs():
	# make verbs
	params = []
	while not (len(params) in [4,6]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, person, number, and tense, [conjugation, perfective form], separated by commas\n")).strip()
		params = processInput(params,True,True)

	if len(params) == 4:
		result = Latin.conjugate(params[0], params[1], params[2], params[3])

	else:
		result = Latin.conjugate(params[0], params[1], params[2], params[3], params[4], params[5])

	print("\nThe Latin form is:")
	print(result)
	return cont()

def latinConstructAdj():
	# make adjectives
	params = []
	while len(params) != 6 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the nominativeMS, root form, declension, gender, case, and number, separated by commas\n")).strip()
		params = processInput(params,True,False)

	print("\nThe Latin form is:")
	print Latin.declineA(params[0], params[1], params[2], params[3], params[4], params[5])

	return cont()

def latinConstruct():
	choice2 = 0
	while checkInt(choice2) and (int(choice2) < 1 or int(choice2) > 4):
		if choice2 != 0:
			print("That's not a choice")
		print("What part of speech do you want to make?\n1) Nouns\n2) Verbs\n3) Adjectives\n4) Return to previous menu")
		choice2 = raw_input().strip()
	choice2 = int(choice2)

	# Construct Nouns
	if choice2 == 1:
		val = 2
		while (True):
			val = latinConstructNouns()
			if val == 'y':
				return 2
			if val == 'a':
				val = 2
			elif val == None:
				return val	

	# Construct Verbs
	elif choice2 == 2:
	# if choice2 == 2:
		val = 2
		while (True):
			val = latinConstructVerbs()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinConstructVerbs()
			elif val == None:
				return val	

	# Construct Adjectives
	elif choice2 == 3:
		val = 2
		while (True):
			val = latinConstructAdj()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinConstructAdj()
			elif val == None:
				return val

	# Return to previous menu
	elif choice2 == 4:
		return 'y'

def latinDeconstructNouns():
	# deconstruct noun
	params = []
	while len(params) != 1 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params,True)

	print("\nThe Latin components are:")
	printList(Latin.reverseDecline(params[0]))

	return cont()

def latinDeconstructVerbs():
	# deconstruct verb
	params = []
	while len(params) != 1 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params,True)

	print("\nThe Latin components are:")
	printList(Latin.reverseConjugate(params[0]))

	return cont()

def latinDeconstructAdj():
	# deconstruct adjective
	params = []
	while not (len(params) in [1,2]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params,True)
		params += ['']

	print("\nThe Latin components are:")
	printList(Latin.reverseDeclineA(params[0], params[1]))

	return cont()

def latinDeconstruct():
	print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective\n4) Return to previous menu")
	choice3 = raw_input().strip()

	while checkInt(choice3) and (int(choice3) < 1 or int(choice3) > 4):
		if choice3 != 0:
			print("That's not a choice")
		print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective\n4) Return to previous menu")
		choice3 = raw_input().strip()
	choice3 = int(choice3)

	# Deconstruct Noun
	if choice3 == 1:
		val = 2
		while (True):
			val = latinDeconstructNouns()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinDeconstructNouns()
			elif val == None:
				return val	
	
	# Deconstruct Verb
	elif choice3 == 2:
	# if choice3 == 2:
		val = 2
		while (True):
			val = latinDeconstructVerbs()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinDeconstructVerbs()
			elif val == None:
				return val	

	# Deconstruct Adjective
	elif choice3 == 3:
		val = 2
		while (True):
			val = latinDeconstructAdj()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinDeconstructAdj()
			elif val == None:
				return val	

	elif choice3 == 4:
		return 'y'

def latinMenu():
	choice1 = 0
	while checkInt(choice1) and (int(choice1) < 1 or int(choice1) > 3):
		if choice1 != 0:
			print("That's not a choice")
		print("What do you want to do?\n1) Construct Latin forms\n2) Deconstruct Latin forms\n3) Return to previous menu")
		choice1 = raw_input().strip()
	choice1 = int(choice1)
		
	# Construct Latin forms
	if choice1 == 1:
		val = 2
		while (True):
			val = latinConstruct()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinConstruct()
			elif val == None:
				return val	

	# Deconstruct Latin forms
	elif choice1 == 2:
		val = 2
		while (True):
			val = latinDeconstruct()
			if val == 'y':
				return 2
			elif val == 'a':
				val = latinDeconstruct()
			elif val == None:
				return val
		
	elif choice1 == 3:
		return 'a'

def russianConstructNouns():
	# make nouns
	params = []
	while not (len(params) in [3,5]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the nominativeS form, case, number, [declension, gender], separated by commas\n")).strip()
		params = processInput(params,False, False)

	if len(params) == 3:
		result =  Russian.decline(params[0], params[1], params[2])

	else:
		# pad declension param with spaces
		if len(params[3]) < 3:
			params[3]+='  '
		result = Russian.decline(params[0], params[1], params[2], params[3], params[4])
	
	print("\nThe Russian form is:")
	print result
	print transliterateRussian(result)

	return cont()

def russianConstructVerbs():
	# make verbs
	params = []
	while not (len(params) in [5]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, person, number, gender, and tense, separated by commas\n")).strip()
		params = processInput(params)

		form = Russian.conjugate(params[0], params[1], params[2], params[3], params[4])
		print("\nThe Russian form is:")
		print form
		print transliterateRussian(form)

	return cont()

def russianConstructAdj():
	# make adjectives
	params = []
	while len(params) != 5 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the nominativeMS, gender, case, number, and animacy, separated by commas\n")).strip()
		params = processInput(params,True,False)
	
	form = Russian.declineA(params[0], params[1], params[2], params[3], params[4])
	print("\nThe Russian form is:")
	print form
	print transliterateRussian(form)

	return cont()

def russianConstruct():
	choice2 = 0
	while checkInt(choice2) and (int(choice2) < 1 or int(choice2) > 4):
		if choice2 != 0:
			print("That's not a choice")
		print("What part of speech do you want to make?\n1) Nouns\n2) Verbs\n3) Adjectives\n4) Return to previous menu")
		choice2 = raw_input().strip()
	choice2 = int(choice2)

	# Construct Nouns
	if choice2 == 1:
		val = 2
		while (True):
			val = russianConstructNouns()
			if val == 'y':
				return 2
			if val == 'a':
				val = 2
			elif val == None:
				return val	

	# Construct Verbs
	elif choice2 == 2:
	# if choice2 == 2:
		val = 2
		while (True):
			val = russianConstructVerbs()
			if val == 'y':
				return 2
			elif val == 'a':
				val = 2
			elif val == None:
				return val	

	# Construct Adjectives
	elif choice2 == 3:
		val = 2
		while (True):
			val = russianConstructAdj()
			if val == 'y':
				return 2
			elif val == 'a':
				val = 2
			elif val == None:
				return val

	# Return to previous menu
	elif choice2 == 4:
		return 'y'

def russianDeconstructNouns():
	# deconstruct noun
	params = []
	while len(params) != 1 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params,True)

	print("\nThe Russian components are:")
	printList(Russian.reverseDecline(params[0]))

	return cont()

def russianDeconstructVerbs():
	# deconstruct verb
	params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
	params = processInput(params)
	while len(params) != 1 or not(checkStr(params)):
		print(len(params))
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params)

	print("\nThe Russian components are:")
	printList(Russian.reverseConjugate(params[0]))

	return cont()

def russianDeconstructAdj():
	# deconstruct adjective
	params = []
	while not (len(params) in [1,2]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params,True)
		params += ['']
	# printList(Russian.reverseDeclineA(params[0], params[1]))

	print("\nThe Russian components are:")
	printList(Russian.reverseDeclineA(params[0]))

	return cont()

def russianDeconstruct():
	print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective\n4) Return to previous menu")
	choice3 = raw_input().strip()

	while checkInt(choice3) and (int(choice3) < 1 or int(choice3) > 4):
		if choice3 != 0:
			print("That's not a choice")
		print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective\n4) Return to previous menu")
		choice3 = raw_input().strip()
	choice3 = int(choice3)

	# Deconstruct Noun
	if choice3 == 1:
		val = 2
		while (True):
			val = russianDeconstructNouns()
			if val == 'y':
				return 2
			elif val == 'a':
				val = russianDeconstructNouns()
			elif val == None:
				return val	
	
	# Deconstruct Verb
	elif choice3 == 2:
	# if choice3 == 2:
		val = 2
		while (True):
			val = russianDeconstructVerbs()
			if val == 'y':
				return 2
			elif val == 'a':
				val = russianDeconstructVerbs()
			elif val == None:
				return val	

	# Deconstruct Adjective
	elif choice3 == 3:
		val = 2
		while (True):
			val = russianDeconstructAdj()
			if val == 'y':
				return 2
			elif val == 'a':
				val = russianDeconstructAdj()
			elif val == None:
				return val	

	elif choice3 == 4:
		return 'y'

def russianMenu():
	choice1 = 0
	while checkInt(choice1) and (int(choice1) < 1 or int(choice1) > 3):
		if choice1 != 0:
			print("That's not a choice")
		print("What do you want to do?\n1) Construct Russian forms\n2) Deconstruct Russian forms\n3) Return to previous menu")
		choice1 = raw_input().strip()
	choice1 = int(choice1)
		
	# Construct Russian forms
	if choice1 == 1:
		val = 2
		while (True):
			val = russianConstruct()
			if val == 'y':
				return 2
			elif val == 'a':
				val = russianConstruct()
			elif val == None:
				return val	

	# Deconstruct Russian forms
	elif choice1 == 2:
		val = 2
		while (True):
			val = russianDeconstruct()
			if val == 'y':
				return 2
			elif val == 'a':
				val = russianDeconstruct()
			elif val == None:
				return val
		
	elif choice1 == 3:
		return 'a'

def transLRverb():
	# translate verb Latin to Russian
	params = []
	while not (len(params) in [1,2]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the Latin verb you want to translate\n")).strip()
		params = processInput(params, True, True)
		params += ['']
	
	form = trans.LRVerb(params[0])
	print("\nThe Russian equivalent is:")
	print form
	print transliterateRussian(form)

	return cont()

def transLRnoun():
	# translate verb Latin to Russian
	params = []
	while not (len(params) in [1,2]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the Latin noun you want to translate\n")).strip()
		params = processInput(params, True, False)
		params += ['']
	
	form =  trans.LRNoun(params[0])
	print("\nThe Russian equivalent is:")
	print form
	print transliterateRussian(form)

	return cont()

def transLRadjective():
	# translate adjective Latin to Russian
	params = []
	while not (len(params) in [1,2,3]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the Latin adjective you want to translate\nOptional: provide noun case")).strip()
		params = processInput(params, True, False)
		params += ['']
	
	if len(params) == 1:
		form =  trans.LRAdj(params[0])
	elif len(params) == 2:
		form =  trans.LRAdj(params[0],noun_case=params[1])
	elif len(params) == 3:
		form =  trans.LRAdj(params[0],accconstr=params[2],noun_case=params[1])

	print("\nThe Russian equivalent is:")
	print form
	print transliterateRussian(form)

	return cont()

def translateLRmenu():
	choice1 = 0
	while checkInt(choice1) and (int(choice1) < 1 or int(choice1) > 4):
		if choice1 != 0:
			print("That's not a choice")
		print("What do you want to do? (LR)\n1) Translate Verbs\n2) Translate Nouns\n3) Translate Adjectives\n4) Return to previous menu")
		choice1 = raw_input().strip()
	choice1 = int(choice1)
		
	# Translate Verbs
	if choice1 == 1:
		val = 2
		while (True):
			val = transLRverb()
			if val == 'y':
				return 2
			elif val == 'a':
				val = transLRverb()
			elif val == None:
				return val	

	# Translate Nouns
	elif choice1 == 2:
		val = 2
		while (True):
			val = transLRnoun()
			if val == 'y':
				return 2
			elif val == 'a':
				val = transLRnoun()
			elif val == None:
				return val

	# Translate Adjectives
	elif choice1 == 3:
		val = 2
		while (True):
			val = transLRadjective()
			if val == 'y':
				return 2
			elif val == 'a':
				val = transLRadjective()
			elif val == None:
				return val
		
	elif choice1 == 4:
		return 'a'

def transRLverb():
	# translate verb Latin to Russian
	params = []
	while not (len(params) in [1,2]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the Russian verb you want to translate\n")).strip()
		params = processInput(params, False, True)
		params += ['']
	
	print("\nThe Latin equivalent is:")
	print trans.RLVerb(params[0])

	return cont()

def transRLnoun():
	# translate verb Latin to Russian
	params = []
	while not (len(params) in [1,2]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the Russian noun you want to translate\n")).strip()
		params = processInput(params)
		params += ['']
	
	print("\nThe Latin equivalent is:")
	print trans.RLNoun(params[0])

	return cont()

def transRLadjective():
	# translate adjective Latin to Russian
	params = []
	while not (len(params) in [1,2,3,4,5]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the Russian adjective you want to translate\nOptional: provide noun case, noun gender, animacy\n")).strip()
		params = processInput(params, True, False)
		params += ['']
	
	if len(params) == 1:
		form =  trans.LRAdj(params[0])
	elif len(params) == 2:
		form =  trans.LRAdj(params[0],noun_case=params[1])
	elif len(params) == 3:
		form =  trans.LRAdj(params[0],noun_case=params[1],noun_gender=params[2])
	elif len(params) == 4:
		form =  trans.LRAdj(params[0],noun_case=params[1],noun_gender=params[2],animacy=params[3])
	elif len(params) == 5:
		form =  trans.LRAdj(params[0],noun_case=params[1],noun_gender=params[2],animacy=params[3],accconstr=params[4])

	return cont()

def translateRLmenu():
	choice1 = 0
	while checkInt(choice1) and (int(choice1) < 1 or int(choice1) > 4):
		if choice1 != 0:
			print("That's not a choice")
		print("What do you want to do? (RL)\n1) Translate Verbs\n2) Translate Nouns\n3) Translate Adjectives\n4) Return to previous menu")
		choice1 = raw_input().strip()
	choice1 = int(choice1)
		
	# Translate Verbs
	if choice1 == 1:
		val = 2
		while (True):
			val = transRLverb()
			if val == 'y':
				return 2
			elif val == 'a':
				val = transRLverb()
			elif val == None:
				return val	

	# Translate Nouns
	elif choice1 == 2:
		val = 2
		while (True):
			val = transRLnoun()
			if val == 'y':
				return 2
			elif val == 'a':
				val = transRLnoun()
			elif val == None:
				return val

	# Translate Adjectives
	elif choice1 == 3:
		val = 2
		while (True):
			val = transRLadjective()
			if val == 'y':
				return 2
			elif val == 'a':
				val = transRLadjective()
			elif val == None:
				return val
		
	elif choice1 == 4:
		return 'a'

def main():
	print("Latin/Russian Translator\n")
	choice0 = 0
	while checkInt(choice0) and (int(choice0) < 1 or int(choice0) > 5):
		print("Please enter the number corresponding with your choice")
		print("What do you want to do?\n1) Latin to Russian\n2) Russian to Latin\n3) Latin\n4) Russian\n5) Exit")
		choice0 = raw_input("").strip()
	choice0 = int(choice0)

	# Latin to Russian
	if choice0 == 1:
		val = 2
		while (True):
			val = translateLRmenu()
			if val == 'y' or val == 'a':
				return 'y'
			elif val == None:
				return val
	
	# Russian to Latin
	elif choice0 == 2:
		val = 2
		while (True):
			val = translateRLmenu()
			if val == 'y' or val == 'a':
				return 'y'
			elif val == None:
				return val
	
	# Latin
	elif choice0 == 3:
	# if choice0 == 3:
		val = 2
		while (True):
			val = latinMenu()
			if val == 'y' or val == 'a':
				return 'y'
			elif val == None:
				return val
	
	# Russian
	elif choice0 == 4:
		val = 2
		while (True):
			val = russianMenu()
			if val == 'y' or val == 'a':
				return 'y'
			elif val == None:
				return val

	# Quit
	elif choice0 == 5:
		return None

if __name__ == '__main__':
	res = main()
	while res == 'y':
		res = main()