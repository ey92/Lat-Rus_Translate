# Lat-Rus_Translate
## CS 4744/Ling 4244 Computational Linguistics Final Project
## Elizabeth Yam (ey92)
translate between Latin and Russian via morphology and phonology

[See what's included for Latin](https://github.com/ey92/Lat-Rus_Translate/blob/master/Latin.md)

[See what's included for Russian](https://github.com/ey92/Lat-Rus_Translate/blob/master/Russian.md)

## Latin

### CONJUGATION
`Latin.conjugate()`
- takes infinitive, perfective, type, number, person, tense

input:    `amare, amāvi, 1, FST, SG, PRES`<br>
output:   `amo`<br>

### REVERSE CONJUGATION
`Latin.reverseConjugate()`
- takes Latin verb form

input:    `amant`<br>
output:   `['amare', 'am\xc4\x81v\xc4\xab', 'TRD', 'PL', 'PRES']`<br>
output2:  `['amare', 'amāvi', 'TRD', 'PL', 'PRES']`<br>

### DECLENSION
`Latin.decline()`
- takes nominativeS, genitiveS, declension d, number, person, tense

input:    `puella, puellae, 1, F, ACC, SG`<br>
output:   `puellam`<br>

### REVERSE DECLENSION
`Latin.reverseDecline()`
- takes Latin noun form

input:    `puellīs`<br>
output:   `['puella', 'puellae', 'DAT/ABL', 'PL']`<br>

[see Latin.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Latin.py)

---

## Russian