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
		case = Roots.RfindDeclG(Roots.RfindGenN(nom))

		print Russian.decline(nom,gen,"NOM","SG")
		print Russian.decline(nom,gen,"GEN","SG")
		print Russian.decline(nom,gen,"DAT","SG")
		print Russian.decline(nom,gen,"ACC","SG")
		print Russian.decline(nom,gen,"PRP","SG")
		print Russian.decline(nom,gen,"INS","SG")
		print Russian.decline(nom,gen,"NOM","PL")
		print Russian.decline(nom,gen,"GEN","PL")
		print Russian.decline(nom,gen,"DAT","PL")
		print Russian.decline(nom,gen,"ACC","PL")
		print Russian.decline(nom,gen,"PRP","PL")
		print Russian.decline(nom,gen,"INS","PL")

if pos == 'A':
	nomM = sys.argv[3].strip()
	if lang == "Latin":
		nomM = Latin.toMacron(nomM)
		root = Roots.LfindRootNM(nomM)
		d = Roots.LfindDeclR(root)
		gender = sys.argv[4].strip()

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
