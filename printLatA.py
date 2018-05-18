#!/bin/env
# -*- coding: utf-8 -*-
from __future__ import print_function
import Roots
import Latin
import runtest

import sys


table = ''

for nomM in Roots.AMap_lat:
	root = Roots.LfindRootNM(nomM)
	d = Roots.LfindDeclR(root)


	table += nomM + ', ' + root + ' - ' + Roots.AMap_eng[Roots.AMap_lat.index(nomM)]
	table += '\n\n'
	table += '|   | F |   | M |   | N |   |\n'
	table += '| - | - | - | - | - | - | - |\n'
	table += '|   | S | P | S | P | S | P |\n'

	for case in ['NOM','GEN','DAT','ACC','ABL','VOC']:
		table += '| ' + case + ' | '

		for gender in ['F','M','N']:
			table += Latin.declineA(nomM,root,d,gender,case,"SG") + ' | '
			table += Latin.declineA(nomM,root,d,gender,case,"PL") + ' | '

		table += '\n'

	table += '\n'

print(table)

# f1=open('./Latin_Verbs_all.md', 'w+')
# f1.write(table)
# f1.close()
