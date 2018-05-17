#!/bin/env
import Roots
import Latin
import runtest

import sys

table = ''

for inf in Roots.VMap_lat:
	table += inf
	table += '\n'
	table += '| S |   |   | P |   |   |\n'
	table += '| - | - |- | - | - | - |\n'
	table += '| 1st person | 2nd person | 3rd person | 1st person | 2nd person | 3rd person |\n'

	for tense in ['PRES','IMPF','FUTR','PERF','PLUP','FUTP']:
		table += '| '
		table += Latin.conjugate(inf,"FST","SG",tense) + ' | '
		table += Latin.conjugate(inf,"SND","SG",tense) + ' | '
		table += Latin.conjugate(inf,"TRD","SG",tense) + ' | '
		table += Latin.conjugate(inf,"FST","PL",tense) + ' | '
		table += Latin.conjugate(inf,"SND","PL",tense) + ' | '
		table += Latin.conjugate(inf,"TRD","PL",tense) + ' |\n\n'

	table += '\n'

print table
