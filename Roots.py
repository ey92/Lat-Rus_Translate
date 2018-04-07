# Elizabeth Yam ey92
# -*- coding: utf-8 -*-

# 55 Noun stems
NMap = [
    ("puellae",      "девочка",      "girl"                      ), \
    ("terrae",       "земля",        "land"                      ), \
    ("feminae",      "женщина",      "woman"                     ), \
    ("agricolae",    "земледелец",   "farmer"                    ), \
    ("puerī",        "мальчик",      "boy"                       ), \
    ("virī",         "мужчина",      "man"                       ), \
    ("filiī",        "сын",          "son"                       ), \
    ("modī",         "способ",       "measure, manner"           ), \
    ("annī",         "год",          "year"                      ), \
    ("mūrī",         "стена",        "wall"                      ), \
    ("servī",        "раб",          "slave, servant"            ), \
    ("librī",        "книга",        "book"                      ), \
    ("bellī",        "война",        "war"                       ), \
    ("dōnī",         "подарок",      "gift"                      ), \
    ("hominis",      "человек",      "human, person"             ), \
    ("regis",        "царь",         "king"                      ), \
    ("consulis",     "консул",       "consul"                    ), \
    ("pānis",        "хлеб",         "bread"                     ), \
    ("laudis",       "похвала",      "praise"                    ), \
    ("jūris",        "право",        "law"                       ), \
    ("flūminis",     "река",         "river"                     ), \
    ("temporis",     "время",        "time"                      ), \
    ("nōminis",      "имя",          "name"                      ), \
    ("pōntis",       "мост",         "bridge"                    ), \
    ("mēnsis",       "месяц",        "month"                     ), \
    ("noctis",       "ночь",         "night"                     ), \
    ("mortis",       "смерть",       "death"                     ), \
    ("urbis",        "город",        "city"                      ), \
    ("turris",       "башня",        "tower"                     ), \
    ("cīvis",        "гражданин",    "citizen"                   ), \
    ("nāvis",        "корабль",      "ship"                      ), \
    ("pārtis",       "доля",         "part"                      ), \
    ("clāvis",       "ключ",         "key"                       ), \
    ("animālis",     "животное",     "animal"                    ), \
    ("maris",        "море",         "sea"                       ), \
    ("manūs",        "рука",         "hand"                      ), \
    ("portūs",       "порт",         "harbor, port"              ), \
    ("cornūs",       "рог",          "horn"                      ), \
    ("reī",          "дело",         "thing, matter"             ), \
    ("bonī",         "вещь",         "possession"                ), \
    ("iterātiōnis",  "раз",          "iteration"                 ), \
    ("oculī",        "глаз",         "eye"                       ), \
    ("vītae",        "жизнь",        "life,existence"            ), \
    ("capitis",      "голова",       "head"                      ), \
    ("amicī",        "друг",         "friend"                    ), \
    ("domī",         "дом",          "house,home,household"      ), \
    ("verbī",        "слово",        "word,speech"               ), \
    ("locī",         "место",        "place,site,region,area"    ), \
    ("faciēī",       "лицо",         "face,person"               ), \
    ("patriae",      "сторона",      "side,party,land,place,part"), \
    ("pedis",        "нога",         "foot,leg"                  ), \
    ("laboris",      "работа",       "work,job"                  ), \
    ("fīnis",        "конец",        "end,ending"                ), \
    ("jānuae",       "дверь",        "door"                      ), \
    ("diēī",         "день",         "day"                       ) \
]

NMap_lat = [x[0] for x in NMap]
NMap_rus = [x[1] for x in NMap]
NMap_eng = [x[2] for x in NMap]


# 26 Verb stems
VMap = [
    ('ire',              'пойти',       'to go'             ), \
    ('esse',             'есть',        'to be'             ), \
    ('posse',            'мочь',        'to be able'        ), \
    ('velle',            'хотеть',      'to want'           ), \
    ('nōlle',            'нехотеть',    'to not want'       ), \
    ('ferre',            'нести',       'to bring, carry'   ), \
    ('amare',            'любить',      'to love'           ), \
    ('cōgitare',         'думать',      'to think'          ), \
    ('parare',           'готовить',    'to prepare'        ), \
    ('rogare',           'спрашивать',  'to ask'            ), \
    ('spectare',         'смотреть',    'to watch'          ), \
    ('stare',            'стоять',      'to stand'          ), \
    ('dēlēre',           'уничтожать',  'to destroy'        ), \
    ('habēre',           'иметь',       'to have'           ), \
    ('vidēre',           'видеть',      'to see'            ), \
    ('comprehendere',    'понимать',    'to understand'     ), \
    ('dīcere',           'говорить',    'to say'            ), \
    ('edere',            'есть',        'to eat'            ), \
    ('petere',           'искать',      'to seek'           ), \
    ('sīdere',           'сидеть',      'to sit'            ), \
    ('vīvere',           'жить',        'to live'           ), \
    ('audire',           'слышать',     'to hear'           ), \
    ('scire',            'знать',       'to know'           ), \
    ('venire',           'приходить',   'to come'           ), \
    ('capere',           'брать',       'to take'           ), \
    ('incipere',         'начать',      'to begin'          ) \
]

VMap_lat = [x[0] for x in VMap]
VMap_rus = [x[1] for x in VMap]
VMap_eng = [x[2] for x in VMap]

# Pronoun mapping
LatinPN = ['ego','meī','mihi','mē','mē','tu','tuī','tibi','tē','tē','nōs','nostrum','nōbis','nōs','nōbis','vōs','vestrum','vōbis','vōs','vōbis','is','ea','id','ēius','ēius','ēius','eī','eī','eī','eum','eam','id','eō','eā','eō','eī','eae','ea','eōrum','earum','eōrum','eīs','eīs','eīs','eōs','eās','ea','eīs','eīs','eīs']
RussianPN = [['я'],['меня'],['мне'],['меня'],['мне','мной'],['ты'],['тебя'],['тебе'],['тебя'],['тебе','тобой'],['мы'],['нас'],['нам'],['нас'],['нас','нами'],['вы'],['вас'],['вам'],['вас'],['вас','вами'],['он'],['его'],['ему'],['его'],['нём','им'],['она'],['её'],['ей'],['её'],['ней','ей'],['оно'],['его'],['ему'],['его'],['нём','им'],['они'],['их'],['им'],['их'],['них','ими'],['они'],['их'],['им'],['их'],['них','ими'],['они'],['их'],['им'],['их'],['них','ими'],]
PNMap = zip(LatinPN, RussianPN)
def PNL2R(word):
    return RussianPN[LatinPN.index(word)]

def PNR2L(word):
    ind = -1
    for e in RussianPN:
        if word in e:
            ind = RussianPN.index(e)
    if ind == -1:
        return None
    else:
        return LatinPN[ind]


# PNDict = {}
# for e in PNMap:
#     if e[0] in PNDict.keys():
#         PNDict[e[0]].append(e[1])
#     else:
#         PNDict[e[0]] = [e[1]]
# form = irePres.keys()[irePres.values().index(root)]

PrepMap = {}

# -------------------------------------------------------------
# LATIN
# 30 Verb stems
LatinV = [
    ('eo',          'ire',              'īvī',          '0', 'to go',             'пойти',     'идти'), \
    ('sum',         'esse',             'fuī',          '0', 'to be',             'есть',      'быть'), \
    ('possum',      'posse',            'potuī',        '0', 'to be able',        'мочь',      'смочь'), \
    ('volo',        'velle',            'voluī',        '0', 'to want',           'хотеть',    'захотеть'), \
    ('nōlo',        'nōlle',            'nōluī',        '0', 'to not want',       'нехотеть',  'незахотеть'), \
    ('fero',        'ferre',            'tulī',         '0', 'to bring, carry',   'нести',     'понести'), \
    ('amo',         'amare',            'amāvī',        '1', 'to love',           'любить',    'полюбить'), \
    ('ambulo',      'ambulare',         'ambulāvī',     '1', 'to walk',           'гулять',    'погулять'), \
    ('cōgito',      'cōgitare',         'cōgitāvī',   '1', 'to think',          'думать',    'подумать'), \
    ('paro',        'parare',           'parāvī',       '1', 'to prepare',        'готовить',  'подготовить'), \
    ('rogo',        'rogare',           'rogāvī',       '1', 'to ask',            'спрашивать','спросить'), \
    ('specto',      'spectare',         'spectāvī',   '1', 'to watch',          'смотреть',  'посмотреть'), \
    ('sto',         'stare',            'stetī',      '1', 'to stand',          'стоять',    'постоя́ть'), \
    ('dēleo',       'dēlēre',           'dēlēvī',       '2', 'to destroy',        'уничтожать','уничтожить'), \
    ('doceo',       'docēre',           'docuī',        '2', 'to teach',          'учить',     'обучить'), \
    ('habeo',       'habēre',           'habuī',        '2', 'to have',           'иметь',     '(no perf)'), \
    ('video',       'vidēre',           'vidī',         '2', 'to see',            'видеть',    'увидеть'), \
    ('comprehendo', 'comprehendere',    'comprehendī',  '3', 'to understand',     'понимать',  'понять'), \
    ('dīco',        'dīcere',           'dīxī',         '3', 'to say',            'говорить',  'сказать'), \
    ('edo',         'edere',            'ēdī',          '3', 'to eat',            'есть',      'съесть'), \
    ('lego',        'legere',           'lēgī',         '3', 'to read',           'читать',    'прочитать'), \
    ('peto',        'petere',           'petīvī',     '3', 'to seek',           'искать',    'поискать'), \
    ('scrībō',      'scrībere',         'scrīpsī',      '3', 'to write',          'писать',    'написать'), \
    ('sīdo',        'sīdere',           'sīdī',         '3', 'to sit',            'сидеть',    'сесть'), \
    ('vīvo',        'vīvere',           'vīxī',         '3', 'to live',           'жить',      'прожить'), \
    ('audio',       'audire',           'audīvī',       '4', 'to hear',           'слышать',   'услышать'), \
    ('scio',        'scire',            'scīvī',        '4', 'to know',           'знать',     'узнать'), \
    ('venio',       'venire',           'vēnī',         '4', 'to come',           'приходить', 'прийти'), \
    ('capio',       'capere',           'cēpī',         '5', 'to take',           'брать',     'взять'), \
    ('incipio',     'incipere',         'incēpī',       '5', 'to begin',          'начать',    'начинать') \
]

LatinV_fs = [x[0] for x in LatinV]
LatinV_inf = [x[1] for x in LatinV]
LatinV_perf = [x[2] for x in LatinV]
LatinV_conj = [x[3] for x in LatinV]
LatinV_eng = [x[4] for x in LatinV]
LatinV_rus_impf = [x[5] for x in LatinV]
LatinV_rus_perf = [x[6] for x in LatinV]

def LfindConjI(word):
    return LatinV_conj[LatinV_inf.index(word)]

def LfindConjP(word):
    return LatinV_conj[LatinV_perf.index(word)]

def LfindInfFS(word):
    return LatinV_inf[LatinV_fs.index(word)]

def LfindInfP(word):
    return LatinV_inf[LatinV_perf.index(word)]

def LfindPerfI(word):
    return LatinV_perf[LatinV_inf.index(word)]

# 55 Noun stems
LatinN = [
    ("agricola",    "agricolae",    "1",    "M",    "земледелец",   "farmer"                    ), \
    ("femina",      "feminae",      "1",    "F",    "женщина",      "woman"                     ), \
    ("jānua",       "jānuae",       "1",    "F",    "дверь",        "door"                      ), \
    ("patria",      "patriae",      "1",    "F",    "сторона",      "side,party,land,place,part"), \
    ("puella",      "puellae",      "1",    "F",    "девочка",      "girl"                      ), \
    ("terra",       "terrae",       "1",    "F",    "земля",        "land"                      ), \
    ("vīta",        "vītae",        "1",    "F",    "жизнь",        "life,existence"            ), \
    ("puer",        "puerī",        "2",    "M",    "мальчик",      "boy"                       ), \
    ("vir",         "virī",         "2",    "M",    "мужчина",      "man"                       ), \
    ("filius",      "filiī",        "2",    "M",    "сын",          "son"                       ), \
    ("modus",       "modī",         "2",    "M",    "способ",       "measure, manner"           ), \
    ("annus",       "annī",         "2",    "M",    "год",          "year"                      ), \
    ("mūrus",       "mūrī",         "2",    "M",    "стена",        "wall"                      ), \
    ("servus",      "servī",        "2",    "M",    "раб",          "slave, servant"            ), \
    ("liber",       "librī",        "2",    "M",    "книга",        "book"                      ), \
    ("amicus",      "amicī",        "2",    "M",    "друг",         "friend"                    ), \
    ("domus",       "domī",         "2",    "M",    "дом",          "house,home,household"      ), \
    ("locus",       "locī",         "2",    "M",    "место",        "place,site,region,area"    ), \
    ("oculus",      "oculī",        "2",    "M",    "глаз",         "eye"                       ), \
    ("bellum",      "bellī",        "2",    "N",    "война",        "war"                       ), \
    ("dōnum",       "dōnī",         "2",    "N",    "подарок",      "gift"                      ), \
    ("bonum",       "bonī",         "2",    "N",    "вещь",         "possession"                ), \
    ("verbum",      "verbī",        "2",    "N",    "слово",        "word,speech"               ), \
    ("homō",        "hominis",      "3  ",  "M",    "человек",      "human, person"             ), \
    ("rex",         "regis",        "3  ",  "M",    "царь",         "king"                      ), \
    ("consul",      "consulis",     "3  ",  "M",    "консул",       "consul"                    ), \
    ("labor",       "laboris",      "3  ",  "M",    "работа",       "work,job"                  ), \
    ("pānis",       "pānis",        "3  ",  "M",    "хлеб",         "bread"                     ), \
    ("pēs",         "pedis",        "3  ",  "M",    "нога",         "foot,leg"                  ), \
    ("iterātiō",    "iterātiōnis",  "3  ",  "F",    "раз",          "iteration"                 ), \
    ("laus",        "laudis",       "3  ",  "F",    "похвала",      "praise"                    ), \
    ("caput",       "capitis",      "3  ",  "N",    "голова",       "head"                      ), \
    ("jūs",         "jūris",        "3  ",  "N",    "право",        "law"                       ), \
    ("flūmen",      "flūminis",     "3  ",  "N",    "река",         "river"                     ), \
    ("nōmen",       "nōminis",      "3  ",  "N",    "имя",          "name"                      ), \
    ("tempus",      "temporis",     "3  ",  "N",    "время",        "time"                      ), \
    ("pōns",        "pōntis",       "3i ",  "M",    "мост",         "bridge"                    ), \
    ("mēnsis",      "mēnsis",       "3i ",  "M",    "месяц",        "month"                     ), \
    ("nox",         "noctis",       "3i ",  "F",    "ночь",         "night"                     ), \
    ("mors",        "mortis",       "3i ",  "F",    "смерть",       "death"                     ), \
    ("urbs",        "urbis",        "3i ",  "F",    "город",        "city"                      ), \
    ("turris",      "turris",       "3i ",  "F",    "башня",        "tower"                     ), \
    ("cīvis",       "cīvis",        "3ii",  "M",    "гражданин",    "citizen"                   ), \
    ("fīnis",       "fīnis",        "3ii",  "F",    "конец",        "end,ending"                ), \
    ("nāvis",       "nāvis",        "3ii",  "F",    "корабль",      "ship"                      ), \
    ("pārs",        "pārtis",       "3ii",  "F",    "доля",         "part"                      ), \
    ("clāvis",      "clāvis",       "3ii",  "F",    "ключ",         "key"                       ), \
    ("animal",      "animālis",     "3ii",  "N",    "животное",     "animal"                    ), \
    ("mare",        "maris",        "3ii",  "N",    "море",         "sea"                       ), \
    ("manus",       "manūs",        "4",    "F",    "рука",         "hand"                      ), \
    ("portus",      "portūs",       "4",    "F",    "порт",         "harbor, port"              ), \
    ("cornū",       "cornūs",       "4",    "N",    "рог",          "horn"                      ), \
    ("diēs",        "diēī",         "5",    "M",    "день",         "day"                       ), \
    ("faciēs",      "faciēī",       "5",    "F",    "лицо",         "face,person"               ), \
    ("rēs",         "rēī",          "5",    "F",    "дело",         "thing, matter"             ) \
]

LatinN_ns = [x[0] for x in LatinN]          # list of all Latin nomS
LatinN_gs = [x[1] for x in LatinN]          # list of all Latin genS
LatinN_decl = [x[2] for x in LatinN]        # list of all Latin decl
LatinN_gender = [x[3] for x in LatinN]      # list of all Latin gender
LatinN_rus = [x[4] for x in LatinN]         # list of all Russian equiv of Latin
LatinN_eng = [x[5] for x in LatinN]         # list of all English equiv of Latin

# returns nomS of genS provided
def LfindNomG(word):
    return LatinN_ns[LatinN_gs.index(word)]

# returns genS of nomS provided
def LfindGenN(word):
    return LatinN_gs[LatinN_ns.index(word)]

# returns decl of genS provided
def LfindDeclG(word):
    return LatinN_decl[LatinN_gs.index(word)]

# returns True if decl of genS provided is 3ii
def Lis3iistemG(word):
    return LfindDeclG == "3ii"

# returns True if gender of genS provided is N
def LisNG(word):
    return LatinN_gender[LatinN_gs.index(word)] == "N"

# 8 Adjectives
LatinA = [
    ('bonus',   'bona',     '12',   'хороший',          'good'          ), \
    ('miser',   'misera',   '12',   'жалкий',           'miserable'     ), \
    ('pulcher', 'pulchra',  '12',   'красивы',          'beautiful'     ), \
    ('ācer',    'ācris',    '3a',   'острый',           'sharp'         ), \
    ('fortis',  'fortis',   '3a',   'крепкий',          'strong, brave' ), \
    ('amāns',   'amantis',  '3b',   'любящий',          'loving'        ), \
    ('fēlīx',   'fēlicis',  '3b',   'счастливый',       'lucky, happy'  ), \
    ('prūdens', 'prūdentis','3b',   'благоразумный',    'wise'          ), \
]

LatinA_nm = [x[0] for x in LatinA]          # list of all Latin nomS
LatinA_fr = [x[1] for x in LatinA]          # list of all Latin genS
LatinA_decl = [x[2] for x in LatinA]        # list of all Latin decl
LatinA_rus = [x[3] for x in LatinA]         # list of all Latin gender
LatinA_eng = [x[4] for x in LatinA]         # list of all Russian equiv of Latin

def LfindMascR(word):
    return LatinA_nm[LatinA_fr.index(word)]    

def LfindRootNM(word):
    return LatinA_fr[LatinA_nm.index(word)]

def LfindDeclR(word):
    return LatinA_decl[LatinA_fr.index(word)]

def LfindDeclNM(word):
    return LatinA_decl[LatinA_nm.index(word)]

# -------------------------------------------------------------
# RUSSIAN
# 7 Verb stems
RussianV = [
    ('читать',     'читают',     '1v',  'прочитать',    'прочитают',    '1v'), \
    ('гулять',     'гуляют',     '1v',  'погулять',     'погуляют',     '1v'), \
    ('жить',       'живут',      '1c',  'прожить',      'проживут',     '1c'), \
    ('писать',     'пишут',      '1c',  'написать',     'напишут',      '1c'), \
    ('говорить',   'говорят',    '2v',  'сказать',      'скажут',       '1c'), \
    ('смотреть',   'смотрят',    '2v',  'посмотреть',   'посмотрят',    '2v'), \
    ('учить',      'учат',       '2c',  'обучить',      'обучат',       '2c'), \
]

RussianV_impf_inf = [x[0] for x in RussianV]
RussianV_impf_3p = [x[1] for x in RussianV]
RussianV_impf_conj = [x[2] for x in RussianV]
RussianV_perf_inf = [x[3] for x in RussianV]
RussianV_perf_3p = [x[4] for x in RussianV]
RussianV_perf_conj = [x[5] for x in RussianV]

def RfindPInfI(word):
    return RussianV_perf_inf[RussianV_impf_inf.index(word)]

def RfindIInfP(word):
    return RussianV_impf_inf[RussianV_perf_inf.index(word)]

def RfindI3PIInf(word):
    return RussianV_impf_3p[RussianV_impf_inf.index(word)]

def RfindP3PPInf(word):
    return RussianV_perf_3p[RussianV_perf_inf.index(word)]

def RfindIConjIInf(word):
    return RussianV_impf_conj[RussianV_impf_inf.index(word)]

def RfindPConjPInf(word):
    return RussianV_perf_conj[RussianV_perf_inf.index(word)]
