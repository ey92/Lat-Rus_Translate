#!/bin/env
# -*- coding: utf-8 -*-
from __future__ import print_function
import Roots
import Latin
import runtest

import sys


table = ''

for gen in Roots.NMap_lat:
	nom = Roots.LfindNomG(gen)

	table += nom + ', ' + gen
	table += '\n\n'
	table += '|   | S | P |\n'
	table += '| - | - | - |\n'

	for case in ['NOM','GEN','DAT','ACC','ABL','VOC']:
		table += '| ' + case + ' | '
		table += Latin.decline(nom,gen,case,"SG") + ' | '
		table += Latin.decline(nom,gen,case,"PL") + ' |\n'

	table += '\n'

print(table)

# f1=open('./Latin_Verbs_all.md', 'w+')
# f1.write(table)
# f1.close()
