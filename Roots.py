# Elizabeth Yam ey92
# -*- coding: utf-8 -*-

# 61 Noun stems: Latin genS to Russian nomS, english
NMap = [
    ("agricolae",    "земледелец",   "farmer"                    ), \
    ("feminae",      "женщина",      "woman"                     ), \
    ("jānuae",       "дверь",        "door"                      ), \
    ("patriae",      "сторона",      "side,party,land,place,part"), \
    ("pennae",       "ручка",        "pen"                       ), \
    ("puellae",      "девочка",      "girl"                      ), \
    ("terrae",       "земля",        "land"                      ), \
    ("vītae",        "жизнь",        "life,existence"            ), \
    ("ānulī",        "кольцо",       "ring"                      ), \
    ("puerī",        "мальчик",      "boy"                       ), \
    ("virī",         "мужчина",      "man"                       ), \
    ("filiī",        "сын",          "son"                       ), \
    ("modī",         "способ",       "measure, manner"           ), \
    ("annī",         "год",          "year"                      ), \
    ("mūrī",         "стена",        "wall"                      ), \
    ("servī",        "раб",          "slave, servant"            ), \
    ("librī",        "книга",        "book"                      ), \
    ("amicī",        "друг",         "friend"                    ), \
    ("domī",         "дом",          "house,home,household"      ), \
    ("locī",         "место",        "place,site,region,area"    ), \
    ("oculī",        "глаз",         "eye"                       ), \
    ("bellī",        "война",        "war"                       ), \
    ("dōnī",         "подарок",      "gift"                      ), \
    ("bonī",         "вещь",         "possession"                ), \
    ("verbī",        "слово",        "word,speech"               ), \
    ("vīnī",         "вино",         "wine"                      ), \
    ("calicis",      "стакан",       "cup, glass"                ), \
    ("hominis",      "человек",      "human, person"             ), \
    ("consulis",     "консул",       "consul"                    ), \
    ("laboris",      "работа",       "work,job"                  ), \
    ("pānis",        "хлеб",         "bread"                     ), \
    ("pedis",        "нога",         "foot,leg"                  ), \
    ("regis",        "король",       "king"                      ), \
    ("graphidis",    "карандаш",     "pencil"                    ), \
    ("iterātiōnis",  "раз",          "iteration"                 ), \
    ("laudis",       "похвала",      "praise"                    ), \
    ("capitis",      "голова",       "head"                      ), \
    ("jūris",        "право",        "law"                       ), \
    ("flūminis",     "река",         "river"                     ), \
    ("nōminis",      "имя",          "name"                      ), \
    ("temporis",     "время",        "time"                      ), \
    ("pōntis",       "мост",         "bridge"                    ), \
    ("mēnsis",       "месяц",        "month"                     ), \
    ("noctis",       "ночь",         "night"                     ), \
    ("mortis",       "смерть",       "death"                     ), \
    ("urbis",        "город",        "city"                      ), \
    ("turris",       "башня",        "tower"                     ), \
    ("cīvis",        "гражданин",    "citizen"                   ), \
    ("fīnis",        "конец",        "end,ending"                ), \
    ("nāvis",        "корабль",      "ship"                      ), \
    ("pārtis",       "доля",         "part"                      ), \
    ("clāvis",       "ключ",         "key"                       ), \
    ("animālis",     "животное",     "animal"                    ), \
    ("maris",        "море",         "sea"                       ), \
    ("manūs",        "рука",         "hand"                      ), \
    ("portūs",       "порт",         "harbor, port"              ), \
    ("cornūs",       "рог",          "horn"                      ), \
    ("diēī",         "день",         "day"                       ), \
    ("faciēī",       "лицо",         "face,person"               ), \
    ("rēī",          "дело",         "thing, matter"             ), \
    ("spēī",         "наде́жда",      "hope"                      ) \
]

NMap_lat = [x[0] for x in NMap]
NMap_rus = [x[1] for x in NMap]
NMap_eng = [x[2] for x in NMap]


# 35 Verb stems
VMap = [
    ('ire',              'ехать',      'to go'              ), \
    ('esse',             'быть',       'to be'              ), #no imperf\
    ('posse',            'мочь',       'to be able'         ), \
    ('velle',            'хотеть',     'to want'            ), \
    ('nōlle',            'нехотеть',   'to not want'        ), \
    ('ferre',            'нести',      'to bring, carry'    ), \
    ('amare',            'любить',     'to love'            ), \
    ('ambulare',         'гулять',     'to walk'            ), \
    ('clāmare',          'кричать',    'to shout'           ), \
    ('cōgitare',         'думать',     'to think'           ), \
    ('dare',             'давать',     'to give'            ), \
    ('expectare',        'ждать',      'to wait'            ), \
    ('parare',           'готовить',   'to prepare'         ), \
    ('rogare',           'спрашивать', 'to ask'             ), \
    ('spectare',         'смотреть',   'to watch'           ), \
    ('stare',            'стоять',     'to stand'           ), \
    ('dēlēre',           'уничтожать', 'to destroy'         ), \
    ('docēre',           'учить',      'to teach'           ), \
    ('habēre',           'иметь',      'to have'            ), \
    ('vidēre',           'видеть',     'to see'             ), \
    ('claudere',         'закрывать',  'to close'           ), \
    ('comprehendere',    'понимать',   'to understand'      ), \
    ('dīcere',           'говорить',   'to say'             ), \
    ('edere',            'есть',       'to eat'             ), \
    ('legere',           'читать',     'to read'            ), \
    ('lūdere',           'игра́ть',     'to play'            ), \
    ('petere',           'искать',     'to seek'            ), \
    ('pōnere',           'класть',     'to put, place'      ), \
    ('scrībere',         'писать',     'to write'           ), \
    ('sīdere',           'сидеть',     'to sit'             ), \
    ('vīvere',           'жить',       'to live'            ), \
    ('audire',           'слышать',    'to hear'            ), \
    ('scire',            'знать',      'to know'            ), \
    ('venire',           'приходить',  'to come'            ), \
    ('capere',           'брать',      'to take'            ), \
    ('incipere',         'начинать',   'to begin'           ) \
]

VMap_lat = [x[0] for x in VMap]
VMap_rus = [x[1] for x in VMap]
VMap_eng = [x[2] for x in VMap]

# 10 Adjectives
AMap = [
    ('bonus',   'хороший',          'good'          ), \
    ('caeruleus','синий',           'blue'          ), \
    ('miser',   'жалкий',           'miserable'     ), \
    ('novus',   'новый',            'new'           ), \
    ('pulcher', 'красивы',          'beautiful'     ), \
    ('ācer',    'острый',           'sharp'         ), \
    ('fortis',  'крепкий',          'strong, brave' ), \
    ('amāns',   'любящий',          'loving'        ), \
    ('fēlīx',   'счастливый',       'lucky, happy'  ), \
    ('prūdens', 'благоразумный',    'wise'          ) \
]

AMap_lat = [x[0] for x in AMap]
AMap_rus = [x[1] for x in AMap]
AMap_eng = [x[2] for x in AMap]


# Pronoun mapping
LatinPN = [
    'ego','meī','mihi','mē','mē',\
    'tu','tuī','tibi','tē','tē',\
    'nōs','nostrum','nōbis','nōs','nōbis',\
    'vōs','vestrum','vōbis','vōs','vōbis',\
    'is','ēius','eī','eum','eō',\
    'ea','ēius','eī','eam','eā',\
    'id','ēius','eī','id','eō',\
    'eī','eōrum','eīs','eōs','eīs',\
    'eae','earum','eīs','eās','eīs',\
    'ea','eōrum','eīs','ea','eīs',\
]

RussianPN = [
    ['я'],['меня'],['мне'],['меня'],['мне','мной'],\
    ['ты'],['тебя'],['тебе'],['тебя'],['тебе','тобой'],\
    ['мы'],['нас'],['нам'],['нас'],['нас','нами'],\
    ['вы'],['вас'],['вам'],['вас'],['вас','вами'],\
    ['он'],['его'],['ему'],['его'],['нём','им'],\
    ['она'],['её'],['ей'],['её'],['ней','ей'],\
    ['оно'],['его'],['ему'],['его'],['нём','им'],\
    ['они'],['их'],['им'],['их'],['них','ими'],\
    ['они'],['их'],['им'],['их'],['них','ими'],\
    ['они'],['их'],['им'],['их'],['них','ими'],\
]

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
# 35 Verb stems
LatinV = [
    ('eo',          'ire',              'īvī',          '0', 'to go',             ), \
    ('sum',         'esse',             'fuī',          '0', 'to be',             ), \
    ('possum',      'posse',            'potuī',        '0', 'to be able',        ), \
    ('volo',        'velle',            'voluī',        '0', 'to want',           ), \
    ('nōlo',        'nōlle',            'nōluī',        '0', 'to not want',       ), \
    ('fero',        'ferre',            'tulī',         '0', 'to bring, carry',   ), \
    ('amo',         'amare',            'amāvī',        '1', 'to love',           ), \
    ('ambulo',      'ambulare',         'ambulāvī',     '1', 'to walk',           ), \
    ('clāmō',       'clāmare',          'clāmāvī',      '1', 'to shout',          ), \
    ('cōgito',      'cōgitare',         'cōgitāvī',     '1', 'to think',          ), \
    ('do',          'dare',             'dedī',         '1', 'to give',           ), \
    ('expecto',     'expectare',        'exspectāvī',   '1', 'to wait',           ), \
    ('paro',        'parare',           'parāvī',       '1', 'to prepare',        ), \
    ('rogo',        'rogare',           'rogāvī',       '1', 'to ask',            ), \
    ('specto',      'spectare',         'spectāvī',     '1', 'to watch',          ), \
    ('sto',         'stare',            'stetī',        '1', 'to stand',          ), \
    ('dēleo',       'dēlēre',           'dēlēvī',       '2', 'to destroy',        ), \
    ('doceo',       'docēre',           'docuī',        '2', 'to teach',          ), \
    ('habeo',       'habēre',           'habuī',        '2', 'to have',           ), \
    ('video',       'vidēre',           'vidī',         '2', 'to see',            ), \
    ('claudo',      'claudere',         'clausī',       '3', 'to close',          ), \
    ('comprehendo', 'comprehendere',    'comprehendī',  '3', 'to understand',     ), \
    ('dīco',        'dīcere',           'dīxī',         '3', 'to say',            ), \
    ('edo',         'edere',            'ēdī',          '3', 'to eat',            ), \
    ('lego',        'legere',           'lēgī',         '3', 'to read',           ), \
    ('lūdo',        'lūdere',           'lūsī',         '3', 'to play',           ), \
    ('peto',        'petere',           'petīvī',       '3', 'to seek',           ), \
    ('pōno',        'pōnere',           'pōsuī',        '3', 'to put, place',     ), \
    ('scrībō',      'scrībere',         'scrīpsī',      '3', 'to write',          ), \
    ('sīdo',        'sīdere',           'sīdī',         '3', 'to sit',            ), \
    ('vīvo',        'vīvere',           'vīxī',         '3', 'to live',           ), \
    ('audio',       'audire',           'audīvī',       '4', 'to hear',           ), \
    ('scio',        'scire',            'scīvī',        '4', 'to know',           ), \
    ('venio',       'venire',           'vēnī',         '4', 'to come',           ), \
    ('capio',       'capere',           'cēpī',         '5', 'to take',           ), \
    ('incipio',     'incipere',         'incēpī',       '5', 'to begin',          ) \
]

LatinV_fs = [x[0] for x in LatinV]
LatinV_inf = [x[1] for x in LatinV]
LatinV_perf = [x[2] for x in LatinV]
LatinV_conj = [x[3] for x in LatinV]
LatinV_eng = [x[4] for x in LatinV]

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

# 61 Noun stems
LatinN = [
    ("agricola",    "agricolae",    "1  ",  "M",    "farmer"                    ), \
    ("femina",      "feminae",      "1  ",  "F",    "woman"                     ), \
    ("jānua",       "jānuae",       "1  ",  "F",    "door"                      ), \
    ("patria",      "patriae",      "1  ",  "F",    "side,party,land,place,part"), \
    ("penna",       "pennae",       "1  ",  "F",    "pen"                       ), \
    ("puella",      "puellae",      "1  ",  "F",    "girl"                      ), \
    ("terra",       "terrae",       "1  ",  "F",    "land"                      ), \
    ("vīta",        "vītae",        "1  ",  "F",    "life,existence"            ), \
    ("ānulus ",     "ānulī",        "2  ",  "M",    "ring"                      ), \
    ("puer",        "puerī",        "2  ",  "M",    "boy"                       ), \
    ("vir",         "virī",         "2  ",  "M",    "man"                       ), \
    ("filius",      "filiī",        "2  ",  "M",    "son"                       ), \
    ("modus",       "modī",         "2  ",  "M",    "measure, manner"           ), \
    ("annus",       "annī",         "2  ",  "M",    "year"                      ), \
    ("mūrus",       "mūrī",         "2  ",  "M",    "wall"                      ), \
    ("servus",      "servī",        "2  ",  "M",    "slave, servant"            ), \
    ("liber",       "librī",        "2P ",  "M",    "book"                      ), \
    ("amicus",      "amicī",        "2  ",  "M",    "friend"                    ), \
    ("domus",       "domī",         "2  ",  "M",    "house,home,household"      ), \
    ("locus",       "locī",         "2  ",  "M",    "place,site,region,area"    ), \
    ("oculus",      "oculī",        "2  ",  "M",    "eye"                       ), \
    ("bellum",      "bellī",        "2  ",  "N",    "war"                       ), \
    ("dōnum",       "dōnī",         "2  ",  "N",    "gift"                      ), \
    ("bonum",       "bonī",         "2  ",  "N",    "possession"                ), \
    ("verbum",      "verbī",        "2  ",  "N",    "word,speech"               ), \
    ("vīnum",       "vīnī",         "2  ",  "N",    "wine"                      ), \
    ("calix",       "calicis",      "3  ",  "M",    "cup, glass"                ), \
    ("homō",        "hominis",      "3  ",  "M",    "human, person"             ), \
    ("consul",      "consulis",     "3  ",  "M",    "consul"                    ), \
    ("labor",       "laboris",      "3  ",  "M",    "work,job"                  ), \
    ("pānis",       "pānis",        "3  ",  "M",    "bread"                     ), \
    ("pēs",         "pedis",        "3  ",  "M",    "foot,leg"                  ), \
    ("rex",         "regis",        "3  ",  "M",    "king"                      ), \
    ("graphis",     "graphidis",    "3  ",  "F",    "pencil"                    ), \
    ("iterātiō",    "iterātiōnis",  "3  ",  "F",    "iteration"                 ), \
    ("laus",        "laudis",       "3  ",  "F",    "praise"                    ), \
    ("caput",       "capitis",      "3  ",  "N",    "head"                      ), \
    ("jūs",         "jūris",        "3  ",  "N",    "law"                       ), \
    ("flūmen",      "flūminis",     "3  ",  "N",    "river"                     ), \
    ("nōmen",       "nōminis",      "3  ",  "N",    "name"                      ), \
    ("tempus",      "temporis",     "3  ",  "N",    "time"                      ), \
    ("pōns",        "pōntis",       "3i ",  "M",    "bridge"                    ), \
    ("mēnsis",      "mēnsis",       "3i ",  "M",    "month"                     ), \
    ("nox",         "noctis",       "3i ",  "F",    "night"                     ), \
    ("mors",        "mortis",       "3i ",  "F",    "death"                     ), \
    ("urbs",        "urbis",        "3i ",  "F",    "city"                      ), \
    ("turris",      "turris",       "3i ",  "F",    "tower"                     ), \
    ("cīvis",       "cīvis",        "3ii",  "M",    "citizen"                   ), \
    ("fīnis",       "fīnis",        "3ii",  "F",    "end,ending"                ), \
    ("nāvis",       "nāvis",        "3ii",  "F",    "ship"                      ), \
    ("pārs",        "pārtis",       "3ii",  "F",    "part"                      ), \
    ("clāvis",      "clāvis",       "3ii",  "F",    "key"                       ), \
    ("animal",      "animālis",     "3ii",  "N",    "animal"                    ), \
    ("mare",        "maris",        "3ii",  "N",    "sea"                       ), \
    ("manus",       "manūs",        "4  ",  "F",    "hand"                      ), \
    ("portus",      "portūs",       "4  ",  "F",    "harbor, port"              ), \
    ("cornū",       "cornūs",       "4  ",  "N",    "horn"                      ), \
    ("diēs",        "diēī",         "5  ",  "M",    "day"                       ), \
    ("faciēs",      "faciēī",       "5  ",  "F",    "face,person"               ), \
    ("rēs",         "rēī",          "5  ",  "F",    "thing, matter"             ), \
    ("spēs",        "spēī",         "5  ",  "F",    "hope"                      ) \
]

LatinN_ns = [x[0] for x in LatinN]          # list of all Latin nomS
LatinN_gs = [x[1] for x in LatinN]          # list of all Latin genS
LatinN_decl = [x[2] for x in LatinN]        # list of all Latin decl
LatinN_gender = [x[3] for x in LatinN]      # list of all Latin gender
LatinN_eng = [x[4] for x in LatinN]         # list of all English equiv of Latin

# returns nomS of genS provided
def LfindNomG(word):
    return LatinN_ns[LatinN_gs.index(word)]

# returns genS of nomS provided
def LfindGenN(word):
    return LatinN_gs[LatinN_ns.index(word)]

# returns declension of genS provided
def LfindDeclG(word):
    return LatinN_decl[LatinN_gs.index(word)]

# returns decl of genS provided
def LfindDeclG(word):
    return LatinN_decl[LatinN_gs.index(word)]

# returns gender of genS provided
def LfindGenderG(word):
    return LatinN_gender[LatinN_gs.index(word)]

# returns True if decl of genS provided is 3ii
def Lis3iistemG(word):
    return LfindDeclG == "3ii"

# returns True if gender of genS provided is N
def LisNG(word):
    return LatinN_gender[LatinN_gs.index(word)] == "N"

# 10 Adjectives
LatinA = [
    ('bonus',   'bona',     '12',   'хороший',          'good'          ), \
    ('caeruleus','caerulea','12',   'синий',          'blue'          ), \
    ('miser',   'misera',   '12',   'жалкий',           'miserable'     ), \
    ('novus',   'nova',     '12',   'новый',            'new'           ), \
    ('pulcher', 'pulchra',  '12',   'красивы',          'beautiful'     ), \
    ('ācer',    'ācris',    '3a',   'острый',           'sharp'         ), \
    ('fortis',  'fortis',   '3a',   'крепкий',          'strong, brave' ), \
    ('amāns',   'amantis',  '3b',   'любящий',          'loving'        ), \
    ('fēlīx',   'fēlicis',  '3b',   'счастливый',       'lucky, happy'  ), \
    ('prūdens', 'prūdentis','3b',   'благоразумный',    'wise'          ) \
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
# 35 Verb stems
RussianV = [
    ('',           '',           '',    'быть',         'будут',        'ir', 'to be'           ), \
    ('мочь',       'могут',      'ir',  'смочь',        'смогут',       'ir', 'to be able'      ), \
    ('давать',     'дают',       'ir',  'дать',         'дадут',        'ir', 'to give'         ), \
    ('есть',       'едят',       'ir',  'съесть',       'съедят',       'ir', 'to eat'          ), \
    ('брать',      'берут',      'ir',  'взять',        'возьмут',      'ir', 'to take'         ), \
    ('класть',     'кладут',     'ir',  'положить',     'положат',      '2c', 'to put, place'   ), \
    ('ждать',      'ждут',       'ir',  'подождать',    'подождут',     'ir', 'to wait'         ), \
    ('жить',       'живут',      'ir',  'прожить',      'проживут',     'ir', 'to live'         ), \
    ('закрывать',  'закрывают',  '1v',  'закрыть',      'закроют',      'ir', 'to close'        ), \
    ('ехать',      'едут',       'ir',  'поехать',      'поедут',       'ir', 'to go'           ), \
    # ('идти',       'идут',       'ir',  'пойти',        'пойдут',       'ir', 'to walk'         ), \
    ('хотеть',     'хотят',      'ir',  'захотеть',     'захотят',      'ir', 'to want'         ), \
    ('нехотеть',   'нехотят',    'ir',  'незахотеть',   'незахотят',    'ir', 'to not want'     ), \
    ('нести',      'несут',      '1c',  'понести',      'понесут',      '1c', 'to bring, carry' ), #find conj\
    ('писать',     'пишут',      '1c',  'написать',     'напишут',      '1c', 'to write'        ), \
    ('читать',     'читают',     '1v',  'прочитать',    'прочитают',    '1v', 'to read'         ), \
    ('гулять',     'гуляют',     '1v',  'погулять',     'погуляют',     '1v', 'to walk'         ), \
    ('искать',     'ищут',       '1c',  'поискать',     'поищут',       '1c', 'to seek'         ), \
    ('говорить',   'говорят',    '2v',  'сказать',      'скажут',       '1c', 'to say'          ), \
    ('смотреть',   'смотрят',    '2v',  'посмотреть',   'посмотрят',    '2v', 'to watch'        ), \
    ('учить',      'учат',       '2c',  'обучить',      'обучат',       '2c', 'to teach'        ), \
    #test below
    ('кричать',    'кричат',     '1v',  'закричать',    'закричат',     '2v', 'to shout'        ), \
    ('любить',     'любят',      '2v',  'полюбить',     'полюбят',      '2v', 'to love'         ), \
    ('думать',     'ду́мают',     '2v',  'подумать',     'подумают',     '2v', 'to think'        ), \
    ('готовить',   'готовят',    '2v',  'приготовить',  'приготовят',   '2v', 'to prepare',     ), \
    ('спрашивать', 'спрашивают', '1v',  'спросить',     'спросят',      '2c', 'to ask',         ), \
    ('стоять',     'стоят',      '2v',  'постоять',     'постоят',      '2v', 'to stand',       ), \
    ('уничтожать', 'уничтожают', '1v',  'уничтожить',   'уничтожат',    '2c', 'to destroy',     ), \
    ('иметь',      'имеют',      '1v',  '',             '',             '',   'to have',        ), \
    ('видеть',     'видят',      '2v',  'увидеть',      'увидят',       '2v', 'to see',         ), #irreg 1ps\
    ('понимать',   'понимают',   '1v',  'понять',       'поймут',       '1c', 'to understand',  ), \
    ('сидеть',     'сидят',      '2v',  'сесть',        'сядут',        '1c', 'to sit',         ), \
    ('слышать',    'слышат',     '2c',  'услышать',     'услышат',      '2c', 'to hear',        ), \
    ('знать',      'знают',      '1v',  'узнать',       'узнают',       '1v', 'to know',        ), \
    ('игра́ть',     'игра́ют',     '1v',  'поигра́ть',     'поигра́ют',     '1v', 'to play',        ), \
    ('приходить',  'приходят',   '2v',  'прийти',       'придут',       '1c', 'to come',        ), \
    ('начина́ть',   'начинают',   '1v',  'начать',       'начнут',       '1c', 'to begin',       ), \
]

RussianV_impf_inf = [x[0] for x in RussianV]
RussianV_impf_3p = [x[1] for x in RussianV]
RussianV_impf_conj = [x[2] for x in RussianV]
RussianV_perf_inf = [x[3] for x in RussianV]
RussianV_perf_3p = [x[4] for x in RussianV]
RussianV_perf_conj = [x[5] for x in RussianV]
RussianV_inf = RussianV_impf_inf+RussianV_perf_inf
RussianV_3p = RussianV_impf_3p+RussianV_perf_3p

def rmStress(word):
    return word.replace('а́','а').replace('е́','е').replace('и́','и').replace('о́','о').replace('у́','у').replace('ы́','ы').replace('э́','э').replace('ю́','ю').replace('я́','я')

RussianV2 = []

for e in RussianV:
    RussianV2.append(map(rmStress, e))

RussianV_impf_inf2 = [x[0] for x in RussianV2]
RussianV_impf_3p2 = [x[1] for x in RussianV2]
RussianV_impf_conj2 = [x[2] for x in RussianV2]
RussianV_perf_inf2 = [x[3] for x in RussianV2]
RussianV_perf_3p2 = [x[4] for x in RussianV2]
RussianV_perf_conj2 = [x[5] for x in RussianV2]
RussianV_inf2 = RussianV_impf_inf2+RussianV_perf_inf2
RussianV_3p2 = RussianV_impf_3p2+RussianV_perf_3p2

def RfindPInfI(word):
    return RussianV_perf_inf[RussianV_impf_inf.index(word)]

def RfindIInfP(word):
    return RussianV_impf_inf[RussianV_perf_inf.index(word)]

def RfindIInf3PI(word):
    try:
        return RussianV_impf_inf[RussianV_impf_3p.index(word)]
    except:
        try:
            return RussianV_impf_inf[RussianV_impf_3p2.index(word)]
        except:
            return None

def RfindPInf3PP(word):
    try:
        return RussianV_perf_inf[RussianV_perf_3p.index(word)]
    except:
        try:
            return RussianV_perf_inf[RussianV_perf_3p2.index(word)]
        except:
            return None

def RfindI3PIInf(word):
    return RussianV_impf_3p[RussianV_impf_inf.index(word)]

def RfindP3PPInf(word):
    return RussianV_perf_3p[RussianV_perf_inf.index(word)]

def RfindIConjIInf(word):
    return RussianV_impf_conj[RussianV_impf_inf.index(word)]

def RfindPConjPInf(word):
    return RussianV_perf_conj[RussianV_perf_inf.index(word)]


# 61 Noun Stems
# aa_ = a-declension
# 00_ = 0-declension
# oo_ = o-declension
# mz_ = ь-declension
# jj_ = declines like adj
# __i = inanimate
# __a = animate
# __p = irregular plural stem
# __n = nom/acc plural ends in a
# __r = irregular root
RussianN = [
    ('земледелец',   'земледельцев', '00a ', '',       'M', 'farmer'                    ), \
    ('женщина',      'женщин',       'aaa ', '',       'F', 'woman'                     ), \
    ('дверь',        'дверей',       'mzi ', '',       'F', 'door'                      ), \
    ('сторона',      'сторон',       'aai ', '',       'F', 'side,party,land,place,part'), \
    ('ручка',        'ручек',        'aai ', '',       'F', 'pen'                       ), \
    ('девочка',      'девочек',      'aaa ', '',       'F', 'girl'                      ), \
    ('земля',        'земель',       'aai ', '',       'F', 'land'                      ), \
    ('жизнь',        'жизней',       'mzi ', '',       'F', 'life,existence'            ), \
    ('кольцо',       'колец',        'ooi ', '',       'N', 'ring'                      ), \
    ('мальчик',      'мальчиков',    '00a ', '',       'M', 'boy'                       ), \
    ('мужчина',      'мужчин',       'aaa ', '',       'M', 'man'                       ), \
    ('сын',          'сынове́й',      '00ap', 'сыновьь', 'M', 'son'                      ), \
    ('способ',       'способов',     '00i ', '',       'M', 'measure, manner'           ), \
    ('год',          'годов',        '00i ', '',       'M', 'year'                      ), \
    ('стена',        'стен',         'aai ', '',       'F', 'wall'                      ), \
    ('раб',          'рабов',        '00a ', '',       'M', 'slave, servant'            ), \
    ('книга',        'книг',         'aai ', '',       'F', 'book'                      ), \
    ('друг',         'друзей',       '00ap', 'друзьь', 'M', 'friend'                    ), \
    ('дом',          'домов',        '00i ', '',       'M', 'house,home,household'      ), \
    ('место',        'мест',         'ooi ', '',       'N', 'place,site,region,area'    ), \
    ('глаз',         'глаз',         '00i ', '',       'M', 'eye'                       ), \
    ('война',        'войн',         'aai ', '',       'F', 'war'                       ), \
    ('подарок',      'подарков',     '00i ', '',       'M', 'gift'                      ), \
    ('вещь',         'вещей',        'mzi ', '',       'F', 'possession'                ), \
    ('слово',        'слов',         'ooi ', '',       'N', 'word,speech'               ), \
    ('вино',         'вин',          'ooi ', '',       'N', 'wine'                      ), \
    ('стакан',       'стаканов',     '00i ', '',       'M', 'cup'                       ), \
    ('человек',      'человеков',    '00a ', '',       'M', 'human, person'             ), \
    ('консул',       'консулов',     '00a ', '',       'M', 'consul'                    ), \
    ('работа',       'работ',        'aai ', '',       'F', 'work,job'                  ), \
    ('хлеб',         'хлебов',       '00i ', '',       'M', 'bread'                     ), \
    ('нога',         'ног',          'aai ', '',       'F', 'foot,leg'                  ), \
    ('коро́ль',       'короле́й',      '00a ', '',       'M', 'king'                      ), \
    ('каранда́ш',     'карандашей',   '00i ', '',       'M', 'pencil'                    ), \
    ('раз',          'раз',          '00i ', '',       'M', 'iteration'                 ), \
    ('похвала',      'похвал',       'aai ', '',       'F', 'praise'                    ), \
    ('голова',       'голов',        'aai ', '',       'F', 'head'                      ), \
    ('право',        'прав',         'ooi ', '',       'N', 'law'                       ), \
    ('река',         'рек',          'aai ', '',       'F', 'river'                     ), \
    ('имя',          'имён',         'iii ', 'имен',   'N', 'name'                      ), \
    ('время',        'времён',       'iii ', 'времен', 'N', 'time'                      ), \
    ('мост',         'мостов',       '00i ', '',       'M', 'bridge'                    ), \
    ('месяц',        'месяцев',      '00i ', '',       'M', 'month'                     ), \
    ('ночь',         'ночей',        'mzi ', '',       'F', 'night'                     ), \
    ('смерть',       'смертей',      'mzi ', '',       'F', 'death'                     ), \
    ('город',        'городо́в',      '00in', '',       'M', 'city'                      ), \
    ('башня',        'башен',        'aai ', '',       'F', 'tower'                     ), \
    ('гражданин',    'граждан',      '00a ', '',       'M', 'citizen'                   ), \
    ('конец',        'концов',       '00i ', '',       'M', 'end'                       ), \
    ('корабль',      'кораблей',     '00i ', '',       'M', 'ship'                      ), \
    ('доля',         'долей',        'aai ', '',       'F', 'part'                      ), \
    ('ключ',         'ключей',       '00i ', '',       'M', 'key'                       ), \
    ('животное',     'животных',     'jja ', 'животн', 'N', 'animal'                    ), \
    ('море',         'морей',        'ooi ', '',       'N', 'sea'                       ), #different root\
    ('рука',         'рук',          'aai ', '',       'F', 'hand'                      ), \
    ('порт',         'портов',       '00i ', '',       'M', 'harbor, port'              ), \
    ('рог',          'рогов',        '00in', '',       'M', 'horn'                      ), \
    ('де́нь',         'дней',         '00ir', 'днь',    'M', 'day'                       ), \
    ('лицо',         'лиц',          'ooi ', '',       'N', 'face,person'               ), \
    ('дело',         'дел',          'ooi ', '',       'N', 'thing, matter'             ), \
    ('наде́жда',      'наде́жд',       'aai ', '',       'F', 'hope'                      ) \
]

RussianN_ns = [x[0] for x in RussianN]          # list of all Russian nomS
RussianN_gp = [x[1] for x in RussianN]          # list of all Russian genS
RussianN_decl = [x[2] for x in RussianN]        # list of all Russian decl
RussianN_root = [x[3] for x in RussianN]        # list of all Russian Roots
RussianN_gender = [x[4] for x in RussianN]      # list of all Russian gender
RussianN_eng = [x[5] for x in RussianN]         # list of all English equiv of Russian

RussianN2 = []

for e in RussianN:
    RussianN2.append(map(rmStress, e))

RussianN2_ns = [x[0] for x in RussianN2]        # list of all Russian nomS
RussianN2_gp = [x[1] for x in RussianN2]        # list of all Russian genS
RussianN2_decl = [x[2] for x in RussianN2]      # list of all Russian decl
RussianN2_root = [x[3] for x in RussianN2]      # list of all Russian Roots
RussianN2_gender = [x[4] for x in RussianN2]    # list of all Russian gender
RussianN2_eng = [x[5] for x in RussianN2]       # list of all English equiv of Russian

# return nomS with stresses (if included)
def RfindNomN(word):
    return RussianN_ns[RussianN2_ns.index(word)]

# returns nomS of genP provided
def RfindNomG(word):
    return RussianN_ns[RussianN2_gp.index(word)]

def RfindNomR(word):
    return RussianN_ns[RussianN2_root.index(word)]

# returns genP of nomS provided
def RfindGenN(word):
    try:
        return RussianN_gp[RussianN2_ns.index(word)]
    except:
        return RussianN_gp[RussianN_ns.index(word)]

# returns declension of genP provided
def RfindDeclG(word):
    try:
        return RussianN_decl[RussianN2_gp.index(word)]
    except:
        try:
            return RussianN_decl[RussianN_gp.index(word)]
        except:
            return '    '

# returns gender of genP provided
def RfindGenderG(word):
    try:
        return RussianN_gender[RussianN2_gp.index(word)]
    except:
        try:
            return RussianN_gender[RussianN_gp.index(word)]
        except:
            return ' '

# returns True if noun is animate
def RisAnimateG(word):
    return RfindDeclG(word)[2] == 'a'

# returns noun root if noun has irregular root
def RfindRootG(word):
    try:
        return RussianN_root[RussianN2_gp.index(word)]
    except:
        return RussianN_root[RussianN_gp.index(word)]

# 10 Adjectives
RussianA = [
    ('хороший',          'good'          ), \
    ('синий',            'dark blue'     ), \
    ('жалкий',           'miserable'     ), \
    ('новый',            'new'           ), \
    ('красивы',          'beautiful'     ), \
    ('острый',           'sharp'         ), \
    ('крепкий',          'strong, brave' ), \
    ('любящий',          'loving'        ), \
    ('счастливый',       'lucky, happy'  ), \
    ('благоразумный',    'wise'          ) \
]