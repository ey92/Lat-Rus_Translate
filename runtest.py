import sys
import Latin

YCHOICES = ['y','yes']
NCHOICES = ['n','no']
YNCHOICES = YCHOICES+NCHOICES

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
	choice4 = raw_input("Would you like to do more? (y/n)\n").lower()
	while choice4 not in YNCHOICES:
		choice4 = raw_input("Would you like to do more? (y/n)\n").lower()
	if choice4 in YCHOICES:
		choice0 = 0
		return 'y'
	else:
		sys.exit(0)

def main():
	print("Latin/Russian Translator\n")
	choice0 = 0
	while checkInt(choice0) and (int(choice0) < 1 or int(choice0) > 4):
		print("Please enter the number corresponding with your choice")
		print("What do you want to do?\n1) Latin to Russian\n2) Russian to Latin\n3) Latin\n4) Russian")
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
		print("What do you want to do?\n1) Construct Latin forms\n2) Deconstruct Latin forms")
		choice1 = 0
		while checkInt(choice1) and (int(choice1) < 1 or int(choice1) > 2):
			choice1 = raw_input().strip()
		choice1 = int(choice1)
			
		# Construct Latin forms
		if choice1 == 1:
			print("What part of speech do you want to make?\n1) Nouns\n2) Verbs\n3) Adjectives")
			choice2 = 0
			while checkInt(choice2) and (int(choice2) < 1 or int(choice2) > 3):
				choice2 = raw_input().strip()
			choice2 = int(choice2)

			# Construct Nouns
			if choice2 == 1:
				# make nouns
				params = str(raw_input("Please enter the nominativeS form, genitiveS form, declension, gender, number, and case, separated by commas\n").strip())
				params = processInput(params)
				while len(params) != 6 or not(checkStr(params)):
					print("Sorry, not the right number of parameters or they aren't all strings.")
					params = str(raw_input("Please enter the nominativeS form, genitiveS form, declension, gender, number, and case, separated by commas\n").strip())
					params = processInput(params)
				print Latin.decline(params[0], params[1], params[2], params[3], params[4], params[5])
				
				return cont()

			# Construct Verbs
			elif choice2 == 2:
			# if choice2 == 2:
				# make verbs
				params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n").strip())
				params = processInput(params)
				while len(params) != 6 or not(checkStr(params)):
					print("Sorry, not the right number of parameters or they aren't all strings.")
					params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n").strip())
					params = processInput(params)
				print Latin.conjugate(params[0], params[1], params[2], params[3], params[4], params[5])

				return cont()

			# Construct Adjectives
			# elif choice2 == 3:
				# make adjectives

		# Deconstruct Latin forms
		elif choice1 == 2:
			print("What part of speech is the form you want to deconstruct?\n1) Noun\n2) Verb\n3) Adjective")
			choice3 = 0
			while checkInt(choice3) and (int(choice3) < 1 or int(choice3) > 3):
				choice3 = raw_input().strip()
			choice3 = int(choice3)

			# Deconstruct Noun
			# if choice3 == 1:
				# deconstruct noun
			
			# Deconstruct Verb
			# elif choice3 == 2:
			if choice3 == 2:
				# deconstruct verb
				params = str(raw_input("Please enter the form you want to deconstruct\n").strip())
				params = processInput(params)
				while len(params) != 1 or not(checkStr(params)):
					print(len(params))
					print("Sorry, not the right number of parameters or they aren't all strings.")
					params = str(raw_input("Please enter the form you want to deconstruct\n").strip())
					params = processInput(params)
				print Latin.reverseConjugate(params[0])

				return cont()

			# Deconstruct Adjective
			# elif choice3 == 3:
				# deconstruct adjective
	
	# Russian
	# elif choice0 == 4:
		#do something
if __name__ == '__main__':
	res = main()
	while res == 'y':
		res = main()