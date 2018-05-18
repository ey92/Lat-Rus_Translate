#!/bin/env
# -*- coding: utf-8 -*-
from __future__ import print_function
import Roots
import Latin
import runtest

import sys


table = ''

for inf in Roots.VMap_lat:
	table += inf
	table += '\n\n'
	table += '|   | S |   |   | P |   |   |\n'
	table += '| - | - | - |- | - | - | - |\n'
	table += '|   | 1st person | 2nd person | 3rd person | 1st person | 2nd person | 3rd person |\n'

	for tense in ['PRES','IMPF','FUTR','PERF','PLUP','FUTP']:
		table += '| ' + tense + ' | '
		table += Latin.conjugate(inf,"FST","SG",tense) + ' |'
		table += Latin.conjugate(inf,"SND","SG",tense) + ' | '
		table += Latin.conjugate(inf,"TRD","SG",tense) + ' | '
		table += Latin.conjugate(inf,"FST","PL",tense) + ' | '
		table += Latin.conjugate(inf,"SND","PL",tense) + ' | '
		table += Latin.conjugate(inf,"TRD","PL",tense) + ' |\n'

	table += '\n'

print(table)

# f1=open('./Latin_Verbs_all.md', 'w+')
# f1.write(table)
# f1.close()
