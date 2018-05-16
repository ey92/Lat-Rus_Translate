#!/bin/env
import Latin
import Russian
import sys

inf = sys.argv[1].strip()
tense = sys.argv[2].strip()

print Latin.conjugate(inf,"FST","SG",tense)
print Latin.conjugate(inf,"SND","SG",tense)
print Latin.conjugate(inf,"TRD","SG",tense)
print Latin.conjugate(inf,"FST","PL",tense)
print Latin.conjugate(inf,"SND","PL",tense)
print Latin.conjugate(inf,"TRD","PL",tense)