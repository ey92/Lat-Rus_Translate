import sys
import Latin

YCHOICES = ['y','yes']
NCHOICES = ['n','no']
ACHOICES = ['a','again']
YNCHOICES = YCHOICES+NCHOICES+ACHOICES

def processInput(string):
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
		return 2
	else:
		sys.exit(0)

def latinConstructNouns():
	# make nouns
	params = str(raw_input("Please enter the nominativeS form, genitiveS form, declension, gender, number, and case, separated by commas\n")).strip()
	params = processInput(params)
	while len(params) != 6 or not(checkStr(params)):
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the nominativeS form, genitiveS form, declension, gender, number, and case, separated by commas\n")).strip()
		params = processInput(params)

	# pad declension param with spaces
	if len(params[3]) < 3:
		params[3]+='  '
	print Latin.decline(params[0], params[1], params[2], params[3], params[4], params[5])
	
	return cont()

def latinConstructVerbs():
	# make verbs
	params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n")).strip()
	params = processInput(params)
	while len(params) != 6 or not(checkStr(params)):
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n")).strip()
		params = processInput(params)
	print Latin.conjugate(params[0], params[1], params[2], params[3], params[4], params[5])

	return cont()

def latinConstructAdj():
	# make adjectives
	params = str(raw_input("Please enter the nominativeM, genitive/nomF (root), declension, gender, case, number, separated by commas\n")).strip()
	params = processInput(params)
	while len(params) != 6 or not(checkStr(params)):
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n")).strip()
		params = processInput(params)
	print Latin.declineA(params[0], params[1], params[2], params[3], params[4], params[5])

	return cont()

def latinConstruct():
	print("What part of speech do you want to make?\n1) Nouns\n2) Verbs\n3) Adjectives\n4) Return to previous menu")
	choice2 = raw_input().strip()
	while checkInt(choice2) and (int(choice2) < 1 or int(choice2) > 4):
		print("That's not a choice")
		print("What part of speech do you want to make?\n1) Nouns\n2) Verbs\n3) Adjectives\n4) Return to previous menu")
		choice2 = raw_input().strip()
	choice2 = int(choice2)

	# Construct Nouns
	if choice2 == 1:
		val = 2
		while (val in [1,2]):
			val = latinConstructNouns()
			if val == 1:
				return 2
			elif val == 2:
				val = latinConstructNouns()
			elif val == None:
				return val	

	# Construct Verbs
	elif choice2 == 2:
	# if choice2 == 2:
		val = 2
		while (val in [1,2]):
			val = latinConstructVerbs()
			if val == 1:
				return 2
			elif val == 2:
				val = latinConstructVerbs()
			elif val == None:
				return val	

	# Construct Adjectives
	elif choice2 == 3:
		val = 2
		while (val in [1,2]):
			val = latinConstructAdj()
			if val == 1:
				return 2
			elif val == 2:
				val = latinConstructAdj()
			elif val == None:
				return val

	# Return to previous menu
	elif choice2 == 4:
		return 1

def latinDeconstructNouns():
	# deconstruct noun
	params = str(raw_input("Please enter the noun you want to deconstruct\n")).strip()
	params = processInput(params)
	while len(params) != 1 or not(checkStr(params)):
		print(len(params))
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params)
	print Latin.reverseDecline(params[0])

	return cont()

def latinDeconstructVerbs():
	# deconstruct verb
	params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
	params = processInput(params)
	while len(params) != 1 or not(checkStr(params)):
		print(len(params))
		print("Sorry, not the right number of parameters or they aren't all strings.")
		params = str(raw_input("Please enter the form you want to deconstruct\n")).strip()
		params = processInput(params)
	print Latin.reverseConjugate(params[0])

	return cont()

# def latinDeconstructAdj():

def latinDeconstruct():
	print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective\n4) Return to previous menu")
	choice3 = raw_input().strip()

	while checkInt(choice3) and (int(choice3) < 1 or int(choice3) > 4):
		print("That's not a choice")
		print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective\n4) Return to previous menu")
		choice3 = raw_input().strip()
	choice3 = int(choice3)

	# Deconstruct Noun
	if choice3 == 1:
		val = 2
		while (val in [1,2]):
			val = latinDeconstructNouns()
			if val == 1:
				return 2
			elif val == 2:
				val = latinDeconstructNouns()
			elif val == None:
				return val	
	
	# Deconstruct Verb
	elif choice3 == 2:
	# if choice3 == 2:
		val = 2
		while (val in [1,2]):
			val = latinDeconstructVerbs()
			if val == 1:
				return 2
			elif val == 2:
				val = latinDeconstructVerbs()
			elif val == None:
				return val	

	# Deconstruct Adjective
	# elif choice3 == 3:
		# deconstruct adjective

	elif choice3 == 4:
		return 1


def latinMenu():
	print("What do you want to do?\n1) Construct Latin forms\n2) Deconstruct Latin forms\n3) Return to previous menu")
	choice1 = raw_input().strip()
	
	while checkInt(choice1) and (int(choice1) < 1 or int(choice1) > 3):
		print("That's not a choice")
		print("What do you want to do?\n1) Construct Latin forms\n2) Deconstruct Latin forms\n3) Return to previous menu")
		choice1 = raw_input().strip()
	choice1 = int(choice1)
		
	# Construct Latin forms
	if choice1 == 1:
		val = 2
		while (val in [1,2]):
			val = latinConstruct()
			if val == 1:
				return 2
			elif val == 2:
				val = latinConstruct()
			elif val == None:
				return val	

	# Deconstruct Latin forms
	elif choice1 == 2:
		val = 2
		while (val in [1,2]):
			val = latinDeconstruct()
			if val == 1:
				return 2
			elif val == 2:
				val = latinDeconstruct()
			elif val == None:
				return val
		
	elif choice1 == 3:
		return 1

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
		while (val in [1,2]):
			val = latinMenu()
			if val == 1:
				return 'y'
			elif val == 2:
				val = latinMenu()
			elif val == None:
				return val
	
	# Russian
	# elif choice0 == 4:
		#do something
		# return russianMenu()

	# Quit
	elif choice0 == 5:
		return None

if __name__ == '__main__':
	res = main()
	while res == 'y':
		res = main()