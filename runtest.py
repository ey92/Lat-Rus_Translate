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

def main():
	print("Latin/Russian Translator\n")
	choice0 = 0
	while choice0 < 1 or choice0 > 4:
		print("Please enter the number corresponding with your choice")
		print("What do you want to do?\n1) Latin to Russian\n2) Russian to Latin\n3) Latin\n4) Russian")
		choice0 = int(raw_input("").strip())

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
		while choice1 < 1 or choice1 > 2:
			choice1 = int(raw_input().strip())
			
		# Construct Latin forms
		if choice1 == 1:
			print("What part of speech do you want to make?\n1) Nouns\n2) Verbs\n3) Adjectives")
			choice2 = 0
			while choice2 < 1 or choice2 > 3:
				choice2 = int(raw_input().strip())

			# Construct Nouns
			# if choice2 == 1:
				# make nouns

			# Construct Verbs
			# elif choice2 == 2:
			if choice2 == 2:
				# make verbs
				params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n").strip())
				params = processInput(params)
				while len(params) != 6 or not(checkStr(params)):
					print("Sorry, not the right number of parameters or they aren't all strings.")
					params = str(raw_input("Please enter the infinitive form, perfective form, conjugation, person, number, and tense, separated by commas\n").strip())
					params = processInput(params)
				print Latin.conjugate(params[0], params[1], params[2], params[3], params[4], params[5])

				choice4 = raw_input("Would you like to do more? (y/n)\n").lower()
				print(choice4 in YCHOICES)
				while choice4 not in YNCHOICES:
					choice4 = raw_input("Would you like to do more? (y/n)\n").lower()
				if choice4 in YCHOICES:
					choice0 = 0
					return 'y'
				else:
					sys.exit(0)

			# Construct Adjectives
			# elif choice2 == 3:
				# make adjectives

		# Deconstruct Latin forms
		# elif choice1 == 2:
			# print("What part of speech is the form you want to deconstruct?\n1)Noun\n2)Verb\n3)Adjective")
			# choice3 = 0
			# while choice3 < 1 or choice >3:
				# choice3 = raw_input().strip()

			# Deconstruct Noun
			# if choice3 == 1:
				# deconstruct noun
			
			# Deconstruct Verb
			# if choice3 == 2:
				# deconstruct verb

			# Deconstruct Adjective
			# if choice3 == 3:
				# deconstruct adjective
	
	# Russian
	# elif choice0 == 4:
		#do something
if __name__ == '__main__':
	res = main()
	while res == 'y':
		res = main()