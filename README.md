<!---Elizabeth Yam ey92-->
# Lat-Rus_Translate (Latin/Russian Literal Translator)
## CS 4744/Ling 4244 Computational Linguistics Final Project (1mo)
## Elizabeth Yam (ey92)
As my final project for this class, I am creating a program to translate between Latin and Russian via their morphology and phonology. I chose these two languages because I have studied Latin for 5 years and Russian for about 2 years, and they have relatively similar grammatical structures (parallels in conjugating and declining).<br>

This translator was created to do a direct, word-for-word literal translation between Latin and Russian. <br>

It doesn't into account context or identify special phrasal constructions. It is only concerned with the indicative mood and active voice for verbs. Nouns are not declined into the locative case. Adjectives used substantively will not be detected as being used in such a way. Additionally, there are no adverbs, auxiliary verbs, modals, comparatives, or superlatives.<br>

[Roots.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Roots.py) has all of the words included in the translator's dictionary. It can attempt to conjugate verbs and decline nouns/adjectives when given the parameters needed, but cannot deconstruct (and therefore translate) words not already in the dictionary.<br>

[See what's included for Latin](https://github.com/ey92/Lat-Rus_Translate/blob/master/Latin.md)

[See what's included for Russian](https://github.com/ey92/Lat-Rus_Translate/blob/master/Russian.md)

## Latin

### Verbs
#### CONJUGATION
`Latin.conjugate()`
- takes infinitive, number, person, tense
- if verb not in dictionary, add perfective and conjugation as last 2 parameters

input:    `amare, FST, SG, PRES`<br>
output:   `amo`<br>

input:    `amare, FST, SG, PRES, 1, amāvī`<br>
output:   `amo`<br>

#### REVERSE CONJUGATION
`Latin.reverseConjugate()`
- takes Latin verb form

input:    `amant`<br>
output:   `['amare', 'am\xc4\x81v\xc4\xab', 'TRD', 'PL', 'PRES']`<br>
output:  `['amare', 'amāvi', 'TRD', 'PL', 'PRES']` (unicode translated)<br>

#### Verb Parameters

| Parameter | Meaning |
| --------- | ------- |
| FST   | first-person          |
| SND   | second-person         |
| TRD   | third-person          |
| SG    | singular              |
| PL    | plural                |
| PRES  | present tense         |
| IMPF  | imperfect tense       |
| FUTR  | future tense          |
| PERF  | perfect tense         |
| PLUP  | pluperfect tense      |
| FUTP  | future perfect tense  |

### Nouns
#### DECLENSION
`Latin.decline()`
- takes nominativeS, genitiveS, case, number
- if noun not in dictionary, add declension and gender as last 2 parameters

input:    `puella, puellae, ACC, SG`<br>
output:   `puellam`<br>

input:    `puella, puellae, ACC, SG, 1, F`<br>
output:   `puellam`<br>

#### REVERSE DECLENSION
`Latin.reverseDecline()`
- takes Latin noun form

input:    `puellīs`<br>
output:   `['puella', 'puellae', 'DAT/ABL', 'PL']`<br>

#### Noun Parameters

| Parameter | Meaning |
| --------- | ------- |
| SG  | singular        |
| PL  | plural          |
| NOM | nominative case |
| GEN | genitive case   |
| DAT | dative case     |
| ACC | accusative case |
| ABL | ablative case   |
| VOC | vocative case   |

### Adjectives
#### DECLENSION
`Latin.declineA()`
- takes nomM, genitive/nomF (root), declension d, gender, case, number

input:  `ācer, ācris, 3a, N, GEN, PL`<br>
output: `acrium`<br>

#### REVERSE DECLENSION
`Latin.reverseDeclineA()`
- takes Latin adjective form
- optional gender parameter (if known)

input:  `fortibus`<br>
output: `['fortis', 'fortis', 'DAT/ABL', 'PL', 'F/M/N']`<br>

input:  `pulchrum`<br>
output: `['pulcher', 'pulchra', 'NOM/ACC', 'SG', 'M/N']`<br>

input:  `pulchrum, M`<br>
outputb: `['pulcher', 'pulchra', 'ACC', 'SG', 'M']`<br>  

input:  `bona`<br>
output: `['bonus', 'bona', 'NOM', 'SG', 'F']`<br>

input:  `bona, N`<br>
output: `['bonus', 'bona', 'NOM/ACC', 'PL', 'N']`<br>


#### Adjective Parameters
| Parameter | Meaning |
| --------- | ------- |
| F   | feminine gender |
| M   | masculine gender|
| N   | neuter gender   |
| SG  | singular        |
| PL  | plural          |
| NOM | nominative case |
| GEN | genitive case   |
| DAT | dative case     |
| ACC | accusative case |
| ABL | ablative case   |
| VOC | vocative case   |

[see Latin.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Latin.py)

---

## Russian

### Verbs
#### CONJUGATION
`Russian.conjugate()`
- takes (either) infinitive, person, number, gender(matters sometimes), tense

input: 	  `читать, SND, PL, , PRES`<br>
output:   `читаете`<br>

input: 	  `прочитать, SND, PL, , PRES`<br>
output:   `читаете`<br>

input: 	  `сказать, , PL, F, PERF `<br>
output:   `сказали`<br>

input: 	  `говорить, , PL, F, PERF`<br>
output:   `сказали`<br>

input: 	  `жить, FST, SG, , FUTR`<br>
output:   `буду_жить`<br>

input: 	  `прожить, FST, SG,  , FUTR`<br>
output:   `буду_жить`<br>


#### REVERSE CONJUGATION
`Russian.reverseConjugate()`
- takes Latin verb form

input:    <br>
output:   <br>
output2:  <br>

#### Verb Parameters

| Parameter | Meaning |
| --------- | ------- |
| M     | masculine	gender		|
| F 	| feminine gender		|
| N 	| neuter gender 		|
| FST   | first-person          |
| SND   | second-person         |
| TRD   | third-person          |
| SG    | singular              |
| PL    | plural                |
| PRES  | present tense         |
| IMPF  | imperfect tense       |
| FUTR  | future tense          |
| PERF  | perfect tense         |
| PLUP  | pluperfect tense      |
| FUTP  | future perfect tense  |

[see Russian.py](https://github.com/ey92/Lat-Rus_Translate/blob/master/Russian.py)