# Elizabeth Yam ey92
import sys
import Latin
import Russian

YCHOICES = ['y','yes']
NCHOICES = ['n','no']
ACHOICES = ['a','again']
YNCHOICES = YCHOICES+NCHOICES+ACHOICES

def processInput(string, latin=True):
	if latin:
		return [Latin.toMacron(p.strip()) for p in string.split(',')]
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
		params = processInput(params,True)

	if len(params) == 4:
		result =  Latin.decline(params[0], params[1], params[2], params[3])

	else:
		# pad declension param with spaces
		if len(params[2]) < 3:
			params[2]+='  '
		result = Latin.decline(params[0], params[1], params[2], params[3], params[4], params[5])
	
	print(result)
	return cont()

def latinConstructVerbs():
	# make verbs
	params = []
	while not (len(params) in [4,6]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, person, number, and tense, [conjugation, perfective form], separated by commas\n")).strip()
		params = processInput(params,True)

	if len(params) == 4:
		result = Latin.conjugate(params[0], params[1], params[2], params[3])

	else:
		result = Latin.conjugate(params[0], params[1], params[2], params[3], params[4], params[5])

	print(result)
	return cont()

def latinConstructAdj():
	# make adjectives
	params = []
	while len(params) != 6 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n")).strip()
		params = processInput(params,True)
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
	print Latin.reverseDecline(params[0])

	return cont()

def latinDeconstructVerbs():
	# deconstruct verb
	params = []
	while len(params) != 1 or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params,True)
	print Latin.reverseConjugate(params[0])

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
	print Latin.reverseDeclineA(params[0], params[1])

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

def russianConstructVerbs():
	# make verbs
	params = []
	while not (len(params) in [5]) or not(checkStr(params)):
		if params != []:
			print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, person, number, gender, and tense, separated by commas\n")).strip()
		params = processInput(params)

		print Russian.conjugate(params[0], params[1], params[2], params[3], params[4])

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
	# if choice2 == 1:
	# 	val = 2
	# 	while (True):
	# 		val = russianConstructNouns()
	# 		if val == 'y':
	# 			return 2
	# 		if val == 'a':
	# 			val = 2
	# 		elif val == None:
	# 			return val	

	# Construct Verbs
	# elif choice2 == 2:
	if choice2 == 2:
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
	# elif choice2 == 3:
	# 	val = 2
	# 	while (True):
	# 		val = russianConstructAdj()
	# 		if val == 'y':
	# 			return 2
	# 		elif val == 'a':
	# 			val = 2
	# 		elif val == None:
	# 			return val

	# Return to previous menu
	elif choice2 == 4:
		return 'y'

def russianDeconstructVerbs():
	# deconstruct verb
	params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
	params = processInput(params)
	while len(params) != 1 or not(checkStr(params)):
		print(len(params))
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params)
	print Russian.reverseConjugate(params[0])

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
	# if choice3 == 1:
	# 	val = 2
	# 	while (True):
	# 		val = russianDeconstructNouns()
	# 		if val == 'y':
	# 			return 2
	# 		elif val == 'a':
	# 			val = russianDeconstructNouns()
	# 		elif val == None:
	# 			return val	
	
	# Deconstruct Verb
	# elif choice3 == 2:
	if choice3 == 2:
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
	# elif choice3 == 3:
	# 	val = 2
	# 	while (True):
	# 		val = russianDeconstructAdj()
	# 		if val == 'y':
	# 			return 2
	# 		elif val == 'a':
	# 			val = russianDeconstructAdj()
	# 		elif val == None:
	# 			return val	

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

def main():
	print("Latin/Russian Translator\n")
	choice0 = 0
	while checkInt(choice0) and (int(choice0) < 1 or int(choice0) > 5):
		print("Please enter the number corresponding with your choice")
		print("What do you want to do?\n1) Latin to Russian\n2) Russian to Latin\n3) Latin\n4) Russian\n5) Exit")
		choice0 = raw_input("").strip()
	choice0 = int(choice0)

	# Latin to Russian
	# if choice0 == 1:
		#do something
	
	# Russian to Latin
	# elif choice0 == 2:
		#do something
	
	# Latin
	# elif choice0 == 3:
	if choice0 == 3:
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