#!/bin/env
# -*- coding: utf-8 -*-
from __future__ import print_function
import Roots
import Russian
import runtest

import sys


table = ''
pinf = ''
eng = ''

for inf in Roots.VMap_rus:
	if inf in Roots.RussianV_perf_inf:
		pinf = inf
		inf = '-'
		eng = Roots.VMap_eng[Roots.VMap_rus.index(pinf)]
	else:
		pinf = Roots.RussianV_perf_inf[Roots.RussianV_impf_inf.index(inf)]
		eng = Roots.VMap_eng[Roots.VMap_rus.index(inf)]

	if pinf == '':
		pinf = '_'

	table += inf + ', '+ pinf + ' - ' + eng
	table += '\n\n'
	table += '| tense |   | S |   |   | P |   |   |\n'
	table += '| ----- | - | - | - | - | - | - | - |\n'

	if inf in Roots.RussianV_impf_inf:
		table += '|   | Person | 1st | 2nd | 3rd | 1st | 2nd | 3rd |\n'

		for tense in ['PRES','FUTR','FUTP']:
			table += '| ' + tense + ' |   | '
			table += Russian.conjugate(inf,"FST","SG","",tense) + ' |'
			table += Russian.conjugate(inf,"SND","SG","",tense) + ' | '
			table += Russian.conjugate(inf,"TRD","SG","",tense) + ' | '
			table += Russian.conjugate(inf,"FST","PL","",tense) + ' | '
			table += Russian.conjugate(inf,"SND","PL","",tense) + ' | '
			table += Russian.conjugate(inf,"TRD","PL","",tense) + ' |\n'

	if pinf in Roots.RussianV_perf_inf:
		table += '|   | Gender | M | F | N | Any |   |   |\n'

		for tense in ['IMPF','PERF']:
			table += '| ' + tense + ' |   | '
			table += Russian.conjugate(inf,"","SG","M",tense) + ' |'
			table += Russian.conjugate(inf,"","SG","F",tense) + ' | '
			table += Russian.conjugate(inf,"","SG","N",tense) + ' | '
			table += Russian.conjugate(inf,"","PL","",tense) + ' |   |   |\n'

	table += '\n'

print(table)

# f1=open('./Latin_Verbs_all.md', 'w+')
# f1.write(table)
# f1.close()
