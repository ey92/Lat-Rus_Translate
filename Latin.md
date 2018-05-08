<!---Elizabeth Yam ey92-->
# Latin
## Capabilities
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
- returns infinitive, 1st person singular perfective, person, number, tense

input:    `amant`<br>
output:  `['amare', 'amāvī', 'TRD', 'PL', 'PRES']`<br>

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
- returns nominative singular, genitive singular, case, number

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
- returns nominative singular masculine, root form, case, number, gender

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

## Grammatical Reference

Latin, for the most part, seems to be chiefly based on morphology and changing suffixes to change meanings. Some literature suggests that the morphology of each declension and conjugation also represents phonology, especially with respect to associating specific sound and morphemes with gendered nouns and tenses of conjugated verbs.

### Verbs:

Conjugations:

| Conjugation | FST SG PRES | Infinitive | FST SG PERF | Supine |
| ----------- | ----------- | ---------- | ----------- | ------ |
| 1         | -o  | -are | -āvī | -atus 	|
| 2         | -eo | -ēre | -ī   | -(i)tus 	|
| 3         | -o  | -ere | -ī   | -(i)tus 	|
| 4         | -io | -ire | -(v)ī| -tus 		|
| 5 (3 IO)  | -io | -ere | -ī   | -tus      |

Indicative mood Active voice:
- (PRES) present
- (IMPF) imperfect
- (FUTR) future
- (PERF) perfect
- (PLUP) pluperfect
- (FUTP) future perfect

Does not include:
- Passive voice
- Subjunctive mood
- Imperative mood
- Gerunds/Gerundives
- Participles

---
### Nouns:

Declensions:

| Declension | NOM SG | GEN SG |
| ---------- | ------ | ------ |
| 1 | -a        | -ae |
| 2 | -um/us/r  | -ī  |
| 3 | ?         | -is |
| 4 | -us       | -ūs |
| 5 | -ēs       | -ēī |

Does not include:
- locative

---
### Adjectives:

Declensions:

| Declension | M | F | N | Root from |
| ---------- | - | - | - | --------- |
| 1/2   | -us/r | -a  | -um | F   |
| 3a    | -is   | -is | -e  | M/F |
| 3b    | ?     | ?   | ?   | -is |

1/2 decline like normal 1/2 nouns<br>
3a and 3b decline like 3ii nouns<br>

Does not include:
- comparatives
- superlatives
- adverbs

---
### Words in dictionary:

#### Latin Verbs

| FST SG PRES | Infinitive | FST SG PERF | Conj<br>(0 = irreg) | English   |
| ----------- | ---------- | ----------- | ------------------- | --------- |
| eo          |  ire              |  īvī          |  0 |  to go            |
| sum         |  esse             |  fuī          |  0 |  to be            |
| possum      |  posse            |  potuī        |  0 |  to be able       |
| volo        |  velle            |  voluī        |  0 |  to want          |
| nōlo        |  nōlle            |  nōluī        |  0 |  to not want      |
| fero        |  ferre            |  tulī         |  0 |  to bring, carry  |
| amo         |  amare            |  amāvī        |  1 |  to love          |
| ambulo      |  ambulare         |  ambulāvī     |  1 |  to walk          |
| cōgito      |  cōgitare         |  cōgitāvī     |  1 |  to think         |
| do          |  dare             |  dedī         |  1 |  to give          |
| expecto     |  expectare        |  exspectāvī   |  1 |  to wait          |
| paro        |  parare           |  parāvī       |  1 |  to prepare       |
| rogo        |  rogare           |  rogāvī       |  1 |  to ask           |
| specto      |  spectare         |  spectāvī     |  1 |  to watch         |
| sto         |  stare            |  stetī        |  1 |  to stand         |
| dēleo       |  dēlēre           |  dēlēvī       |  2 |  to destroy       |
| doceo       |  docēre           |  docuī        |  2 |  to teach         |
| habeo       |  habēre           |  habuī        |  2 |  to have          |
| video       |  vidēre           |  vidī         |  2 |  to see           |
| claudo      |  claudere         |  clausī       |  3 |  to close         |
| comprehendo |  comprehendere    |  comprehendī  |  3 |  to understand    |
| dīco        |  dīcere           |  dīxī         |  3 |  to say           |
| edo         |  edere            |  ēdī          |  3 |  to eat           |
| lego        |  legere           |  lēgī         |  3 |  to read          |
| peto        |  petere           |  petīvī       |  3 |  to seek          |
| pōno        |  pōnere           |  pōsuī        |  3 |  to put, place    |
| scrībō      |  scrībere         |  scrīpsī      |  3 |  to write         |
| sīdo        |  sīdere           |  sīdī         |  3 |  to sit           |
| vīvo        |  vīvere           |  vīxī         |  3 |  to live          |
| audio       |  audire           |  audīvī       |  4 |  to hear          |
| scio        |  scire            |  scīvī        |  4 |  to know          |
| venio       |  venire           |  vēnī         |  4 |  to come          |
| capio       |  capere           |  cēpī         |  5 |  to take          |
| incipio     |  incipere         |  incēpī       |  5 |  to begin         |

#### Latin Nouns

| NOM SG | GEN SG | Decl | Gender | English |
| ------ | ------ | ---- | ------ | ------- |
| agricola   | agricolae   | 1   | M   | farmer                     |
| femina     | feminae     | 1   | F   | woman                      |
| jānua      | jānuae      | 1   | F   | door                       |
| patria     | patriae     | 1   | F   | side,party,land,place,part |
| penna      | pennae      | 1   | F   | pen                        |
| puella     | puellae     | 1   | F   | girl                       |
| terra      | terrae      | 1   | F   | land                       |
| vīta       | vītae       | 1   | F   | life,existence             |
| ānulus     | ānulī       | 2   | M   | ring                       |
| puer       | puerī       | 2   | M   | boy                        |
| vir        | virī        | 2   | M   | man                        |
| filius     | filiī       | 2   | M   | son                        |
| modus      | modī        | 2   | M   | measure, manner            |
| annus      | annī        | 2   | M   | year                       |
| mūrus      | mūrī        | 2   | M   | wall                       |
| servus     | servī       | 2   | M   | slave, servant             |
| liber      | librī       | 2P  | M   | book                       |
| amicus     | amicī       | 2   | M   | friend                     |
| domus      | domī        | 2   | M   | house,home,household       |
| locus      | locī        | 2   | M   | place,site,region,area     |
| oculus     | oculī       | 2   | M   | eye                        |
| bellum     | bellī       | 2   | N   | war                        |
| dōnum      | dōnī        | 2   | N   | gift                       |
| bonum      | bonī        | 2   | N   | possession                 |
| verbum     | verbī       | 2   | N   | word,speech                |
| vīnum      | vīnī        | 2   | N   | wine                       |
| calix      | calicis     | 3   | M   | cup, glass                 |
| homō       | hominis     | 3   | M   | human, person              |
| consul     | consulis    | 3   | M   | consul                     |
| labor      | laboris     | 3   | M   | work,job                   |
| pānis      | pānis       | 3   | M   | bread                      |
| pēs        | pedis       | 3   | M   | foot,leg                   |
| rex        | regis       | 3   | M   | king                       |
| graphis    | graphidis   | 3   | F   | pencil                     |
| iterātiō   | iterātiōnis | 3   | F   | iteration                  |
| laus       | laudis      | 3   | F   | praise                     |
| caput      | capitis     | 3   | N   | head                       |
| jūs        | jūris       | 3   | N   | law                        |
| flūmen     | flūminis    | 3   | N   | river                      |
| nōmen      | nōminis     | 3   | N   | name                       |
| tempus     | temporis    | 3   | N   | time                       |
| pōns       | pōntis      | 3i  | M   | bridge                     |
| mēnsis     | mēnsis      | 3i  | M   | month                      |
| nox        | noctis      | 3i  | F   | night                      |
| mors       | mortis      | 3i  | F   | death                      |
| urbs       | urbis       | 3i  | F   | city                       |
| turris     | turris      | 3i  | F   | tower                      |
| cīvis      | cīvis       | 3ii | M   | citizen                    |
| fīnis      | fīnis       | 3ii | F   | end,ending                 |
| nāvis      | nāvis       | 3ii | F   | ship                       |
| pārs       | pārtis      | 3ii | F   | part                       |
| clāvis     | clāvis      | 3ii | F   | key                        |
| animal     | animālis    | 3ii | N   | animal                     |
| mare       | maris       | 3ii | N   | sea                        |
| manus      | manūs       | 4   | F   | hand                       |
| portus     | portūs      | 4   | F   | harbor, port               |
| cornū      | cornūs      | 4   | N   | horn                       |
| diēs       | diēī        | 5   | M   | day                        |
| faciēs     | faciēī      | 5   | F   | face,person                |
| rēs        | rēī         | 5   | F   | thing, matter              |

#### Latin Adjectives

| NOM SG M | NOM SG F/GEN SG | Decl | Russian | English |
| -------- | --------------- | ---- | ------- | ------- |
|'bonus'|	 'bona'|	 '12'| 'хороший'		| 'good'          |
|'miser'|	 'misera'|	 '12'| 'жалкий'			| 'miserable'     |
|'pulcher'|	 'pulchra'|	 '12'| 'красивы'		| 'beautiful'     |
|'ācer'|	 'ācris'|	 '3a'| 'острый'			| 'sharp'         |
|'fortis'|	 'fortis'|	 '3a'| 'крепкий'		| 'strong, brave' |
|'amāns'|	 'amantis'|	 '3b'| 'любящий'		| 'loving'        |
|'fēlīx'|	 'fēlicis'|	 '3b'| 'счастливый'		| 'lucky, happy'  |
|'prūdens'|	 'prūdentis'|'3b'| 'благоразумный'	| 'wise'          |
