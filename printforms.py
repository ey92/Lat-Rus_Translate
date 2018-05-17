#!/bin/env
import Roots
import Latin
import Russian
import runtest

import sys

lang = sys.argv[1].strip()
language = eval(lang)
pos = sys.argv[2].strip()

if pos == 'V': 	
	inf = sys.argv[3].strip()
	tense = sys.argv[4].strip()
	
	if lang == "Latin":
		inf = Latin.toMacron(inf)

		print Latin.conjugate(inf,"FST","SG",tense)
		print Latin.conjugate(inf,"SND","SG",tense)
		print Latin.conjugate(inf,"TRD","SG",tense)
		print Latin.conjugate(inf,"FST","PL",tense)
		print Latin.conjugate(inf,"SND","PL",tense)
		print Latin.conjugate(inf,"TRD","PL",tense)

	else:
		if tense in ["IMPF", "PERF"]:
			print Russian.conjugate(inf,"","SG","M",tense)
			print Russian.conjugate(inf,"","SG","F",tense)
			print Russian.conjugate(inf,"","SG","N",tense)
			print Russian.conjugate(inf,"","PL","",tense)

		else:
			print Russian.conjugate(inf,"FST","SG","",tense)
			print Russian.conjugate(inf,"SND","SG","",tense)
			print Russian.conjugate(inf,"TRD","SG","",tense)
			print Russian.conjugate(inf,"FST","PL","",tense)
			print Russian.conjugate(inf,"SND","PL","",tense)
			print Russian.conjugate(inf,"TRD","PL","",tense)

if pos == 'N':
	nom = sys.argv[3].strip()
	if lang == "Latin":
		nom = Latin.toMacron(nom)
		gen = Roots.LfindGenN(nom)

		print Latin.decline(nom,gen,"NOM","SG")
		print Latin.decline(nom,gen,"GEN","SG")
		print Latin.decline(nom,gen,"DAT","SG")
		print Latin.decline(nom,gen,"ACC","SG")
		print Latin.decline(nom,gen,"ABL","SG")
		print Latin.decline(nom,gen,"VOC","SG")
		print Latin.decline(nom,gen,"NOM","PL")
		print Latin.decline(nom,gen,"GEN","PL")
		print Latin.decline(nom,gen,"DAT","PL")
		print Latin.decline(nom,gen,"ACC","PL")
		print Latin.decline(nom,gen,"ABL","PL")
		print Latin.decline(nom,gen,"VOC","PL")

	else:
		# d = Roots.RfindDeclG(Roots.RfindGenN(nom))
		transliterate = sys.argv[3].strip()
		if transliterateRussian in [None,'']:
			transliterate = False

		if transliterate:
			print runtest.transliterateRussian(Russian.decline(nom,"NOM","SG"))
			print runtest.transliterateRussian(Russian.decline(nom,"GEN","SG"))
			print runtest.transliterateRussian(Russian.decline(nom,"DAT","SG"))
			print runtest.transliterateRussian(Russian.decline(nom,"ACC","SG"))
			print runtest.transliterateRussian(Russian.decline(nom,"PRP","SG"))
			print runtest.transliterateRussian(Russian.decline(nom,"INS","SG"))
			print runtest.transliterateRussian(Russian.decline(nom,"NOM","PL"))
			print runtest.transliterateRussian(Russian.decline(nom,"GEN","PL"))
			print runtest.transliterateRussian(Russian.decline(nom,"DAT","PL"))
			print runtest.transliterateRussian(Russian.decline(nom,"ACC","PL"))
			print runtest.transliterateRussian(Russian.decline(nom,"PRP","PL"))
			print runtest.transliterateRussian(Russian.decline(nom,"INS","PL"))

		else:
			print Russian.decline(nom,"NOM","SG")
			print Russian.decline(nom,"GEN","SG")
			print Russian.decline(nom,"DAT","SG")
			print Russian.decline(nom,"ACC","SG")
			print Russian.decline(nom,"PRP","SG")
			print Russian.decline(nom,"INS","SG")
			print Russian.decline(nom,"NOM","PL")
			print Russian.decline(nom,"GEN","PL")
			print Russian.decline(nom,"DAT","PL")
			print Russian.decline(nom,"ACC","PL")
			print Russian.decline(nom,"PRP","PL")
			print Russian.decline(nom,"INS","PL")

if pos == 'A':
	nomM = sys.argv[3].strip()
	gender = sys.argv[4].strip()

	if lang == "Latin":
		nomM = Latin.toMacron(nomM)
		root = Roots.LfindRootNM(nomM)
		d = Roots.LfindDeclR(root)

		if gender in [None,'']:
			for gender in ["M","F","N"]:
				print Latin.declineA(nomM,root,d,gender,"NOM","SG")
				print Latin.declineA(nomM,root,d,gender,"GEN","SG")
				print Latin.declineA(nomM,root,d,gender,"DAT","SG")
				print Latin.declineA(nomM,root,d,gender,"ACC","SG")
				print Latin.declineA(nomM,root,d,gender,"ABL","SG")
				print Latin.declineA(nomM,root,d,gender,"VOC","SG")

		else:
			print Latin.declineA(nomM,root,d,gender,"NOM","SG")
			print Latin.declineA(nomM,root,d,gender,"GEN","SG")
			print Latin.declineA(nomM,root,d,gender,"DAT","SG")
			print Latin.declineA(nomM,root,d,gender,"ACC","SG")
			print Latin.declineA(nomM,root,d,gender,"ABL","SG")
			print Latin.declineA(nomM,root,d,gender,"VOC","SG")

		print Latin.declineA(nomM,root,d,gender,"NOM","PL")
		print Latin.declineA(nomM,root,d,gender,"GEN","PL")
		print Latin.declineA(nomM,root,d,gender,"DAT","PL")
		print Latin.declineA(nomM,root,d,gender,"ACC","PL")
		print Latin.declineA(nomM,root,d,gender,"ABL","PL")
		print Latin.declineA(nomM,root,d,gender,"VOC","PL")

	else:
		transliterate = False
		if gender in [None,'','True','False']:
			transliterate = eval(sys.argv[4])
			for gender in ["M","F","N"]:
				if transliterate: 
					print runtest.transliterateRussian(Russian.declineA(nomM,gender,"NOM","SG",False))
					print runtest.transliterateRussian(Russian.declineA(nomM,gender,"GEN","SG",False))
					print runtest.transliterateRussian(Russian.declineA(nomM,gender,"DAT","SG",False))
					print runtest.transliterateRussian(Russian.declineA(nomM,gender,"ACC","SG",False))
					print runtest.transliterateRussian(Russian.declineA(nomM,gender,"PRP","SG",False))
					print runtest.transliterateRussian(Russian.declineA(nomM,gender,"INS","SG",False))
				else:
					print Russian.declineA(nomM,gender,"NOM","SG",False)
					print Russian.declineA(nomM,gender,"GEN","SG",False)
					print Russian.declineA(nomM,gender,"DAT","SG",False)
					print Russian.declineA(nomM,gender,"ACC","SG",False)
					print Russian.declineA(nomM,gender,"PRP","SG",False)
					print Russian.declineA(nomM,gender,"INS","SG",False)

		else:
			transliterate = eval(sys.argv[5])
			if transliterate: 
				print runtest.transliterateRussian(Russian.declineA(nomM,gender,"NOM","SG",False))
				print runtest.transliterateRussian(Russian.declineA(nomM,gender,"GEN","SG",False))
				print runtest.transliterateRussian(Russian.declineA(nomM,gender,"DAT","SG",False))
				print runtest.transliterateRussian(Russian.declineA(nomM,gender,"ACC","SG",False))
				print runtest.transliterateRussian(Russian.declineA(nomM,gender,"PRP","SG",False))
				print runtest.transliterateRussian(Russian.declineA(nomM,gender,"INS","SG",False))
			else:
				print Russian.declineA(nomM,gender,"NOM","SG",False)
				print Russian.declineA(nomM,gender,"GEN","SG",False)
				print Russian.declineA(nomM,gender,"DAT","SG",False)
				print Russian.declineA(nomM,gender,"ACC","SG",False)
				print Russian.declineA(nomM,gender,"PRP","SG",False)
				print Russian.declineA(nomM,gender,"INS","SG",False)

		if transliterate:
			print runtest.transliterateRussian(Russian.declineA(nomM,gender,"NOM","PL",False))
			print runtest.transliterateRussian(Russian.declineA(nomM,gender,"GEN","PL",False))
			print runtest.transliterateRussian(Russian.declineA(nomM,gender,"DAT","PL",False))
			print runtest.transliterateRussian(Russian.declineA(nomM,gender,"ACC","PL",False))
			print runtest.transliterateRussian(Russian.declineA(nomM,gender,"PRP","PL",False))
			print runtest.transliterateRussian(Russian.declineA(nomM,gender,"INS","PL",False))

		else:
			print Russian.declineA(nomM,gender,"NOM","PL",False)
			print Russian.declineA(nomM,gender,"GEN","PL",False)
			print Russian.declineA(nomM,gender,"DAT","PL",False)
			print Russian.declineA(nomM,gender,"ACC","PL",False)
			print Russian.declineA(nomM,gender,"PRP","PL",False)
			print Russian.declineA(nomM,gender,"INS","PL",False)