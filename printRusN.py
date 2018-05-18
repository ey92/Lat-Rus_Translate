#!/bin/env
# -*- coding: utf-8 -*-
from __future__ import print_function
import Roots
import Russian
import runtest

import sys


table = ''

for nom in Roots.NMap_rus:
	gen = Roots.RfindGenN(nom)

	table += nom + ', ' + gen + ' - ' + Roots.RfindGenderG(gen) + ' - ' + Roots.NMap_eng[Roots.NMap_rus.index(nom)]
	table += '\n\n'
	table += '|   | S | P |\n'
	table += '| - | - | - |\n'

	for case in ['NOM','GEN','DAT','ACC','PRP','INS']:
		table += '| ' + case + ' | '
		table += Russian.decline(nom,case,"SG") + ' | '
		table += Russian.decline(nom,case,"PL") + ' |\n'

	table += '\n'

print(table)

# f1=open('./Latin_Verbs_all.md', 'w+')
# f1.write(table)
# f1.close()
