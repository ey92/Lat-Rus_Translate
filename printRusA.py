#!/bin/env
# -*- coding: utf-8 -*-
from __future__ import print_function
import Roots
import Russian
import runtest

import sys


table = ''
gender = ''

for nomM in Roots.AMap_rus:

	table += nomM + ' - ' + Roots.AMap_eng[Roots.AMap_rus.index(nomM)]
	table += '\n\n'
	table += '|   | S |   |   | P |\n'
	table += '| - | - | - | - | - |\n'
	table += '|   | F | M | N | Any |\n'

	for case in ['NOM','GEN','DAT','ACC','PRP','INS']:
		table += '| ' + case + ' | '

		for gender in ['F','M','N']:
			table += Russian.declineA(nomM,gender,case,"SG",False) + ' | '

		table += Russian.declineA(nomM,gender,case,"PL",False) + ' | '
		table += '\n'

	table += '\n'

print(table)

# f1=open('./Latin_Verbs_all.md', 'w+')
# f1.write(table)
# f1.close()
