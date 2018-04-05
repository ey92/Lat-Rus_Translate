# -*- coding: utf-8 -*-
# 20 Noun stems
NMap = {
    "man,person":"человек", \
    "time":"время", \
    "hand,arm,handwriting":"рука", \
    "affair,business,thing,matter":"дело", \
    "time":"раз", \
    "eye":"глаз", \
    "day,afternoon":"день", \
    "life,existence":"жизнь", \
    "here":"тут", \
    "head":"голова", \
    "friend":"друг", \
    "house,home,household":"дом", \
    "word,speech":"слово", \
    "place,site,region,area":"место", \
    "face,right side,person":"лицо", \
    "side,party,land,place,part":"сторона", \
    "foot,leg":"нога", \
    "work,job":"работа", \
    "end,ending":"конец", \
    "door":"дверь" \
}

# 20 Verb stems
VMap = {
    "be":"быть", \
    "say,speak,talk,indicate":"сказать", \
    "be able, can":"мочь", \
    "know":"знать", \
    "speak,say,tell":"говорить", \
    "begin,come,become":"стать", \
    "eat,exists":"есть", \
    "want":"хотеть", \
    "see":"видеть", \
    "start,leave,go":"идти", \
    "stand,be,lie,stop":"стоять", \
    "think,consider,believe":"думать", \
    "ask,inquire,demand":"спросить", \
    "live":"жить", \
    "look,see,watch,inspect":"смотреть", \
    "have":"иметь", \
    "understand,comprehend,realize":"понять", \
    "sit,be":"сидеть", \
    "make,do":"делать", \
    "make,do(perf)":"сделать" \
}
# -------------------------------------------------------------
# LATIN
LatinV = [
    ("eo",      "ire",      "īvī",      0), \
    ("sum",     "esse",     "fuī",      0), \
    ("possum",  "posse",    "potuī",    0), \
    ("volo",    "velle",    "voluī",    0), \
    ("nōlo",    "nōlle",    "nōluī",    0), \
    ("fero",    "ferre",    "tulī",     0), \
    ("amo",     "amare",    "amāvī",    1), \
    ("paro",    "parare",   "parāvī",   1), \
    ("dēleo",   "dēlēre",   "dēlēvī",   2), \
    ("habeo",   "habēre",   "habuī",    2), \
    ("peto",    "petere",   "petīvī",   3), \
    ("dīco",    "dīcere",   "dīxī",     3), \
    ("venio",   "venire",   "vēnī",     4), \
    ("audio",   "audire",   "audīvī",   4), \
    ("capio",   "capere",   "cēpī",     5) \
]
LatinV_fs = [x[0] for x in LatinV]
LatinV_inf = [x[1] for x in LatinV]
LatinV_perf = [x[2] for x in LatinV]
LatinV_conj = [x[3] for x in LatinV]

def findConjI(word):
    return LatinV_conj[LatinV_inf.index(word)]

def findConjP(word):
    return LatinV_conj[LatinV_perf.index(word)]

def findInfFS(word):
    return LatinV_inf[LatinV_fs.index(word)]

def findInfP(word):
    return LatinV_inf[LatinV_perf.index(word)]

def findPerfI(word):
    return LatinV_perf[LatinV_inf.index(word)]

LatinN = [
    ("puella",  "puellae",  "1",    "F"), \
    ("terra",   "terrae",   "1",    "F"), \
    ("femina",  "feminae",  "1",    "F"), \
    ("agricola","agricolae","1",    "M"), \
    ("puer",    "puerī",    "2",    "M"), \
    ("vir",     "virī",     "2",    "M"), \
    ("filius",  "filiī",    "2",    "M"), \
    ("modus",   "modī",     "2",    "M"), \
    ("annus",   "annī",     "2",    "M"), \
    ("mūrus",   "mūrī",     "2",    "M"), \
    ("servus",  "servī",    "2",    "M"), \
    ("liber",   "librī",    "2",    "M"), \
    ("bellum",  "bellī",    "2",    "N"), \
    ("dōnus",   "dōnī",     "2",    "N"), \
    ("homō",    "hominis",  "3  ",  "M"), \
    ("rex",     "regis",    "3  ",  "M"), \
    ("consul",  "consulis", "3  ",  "M"), \
    ("pānis",   "pānis",    "3  ",  "M"), \
    ("laus",    "laudis",   "3  ",  "F"), \
    ("jūs",     "jūris",    "3  ",  "N"), \
    ("flūmen",  "flūminis", "3  ",  "N"), \
    ("tempus",  "temporis", "3  ",  "N"), \
    ("nōmen",   "nōminis",  "3  ",  "N"), \
    ("pōns",    "pōntis",   "3i ",  "M"), \
    ("mēnsis",  "mēnsis",   "3i ",  "M"), \
    ("nox",     "noctis",   "3i ",  "F"), \
    ("mors",    "mortis",   "3i ",  "F"), \
    ("urbs",    "urbis",    "3i ",  "F"), \
    ("turris",  "turris",   "3i ",  "F"), \
    ("cīvis",   "cīvis",    "3ii",  "MF"), \
    ("nāvis",   "nāvis",    "3ii",  "F"), \
    ("pārs",    "pārtis",   "3ii",  "F"), \
    ("clāvis",  "clāvis",   "3ii",  "F"), \
    ("animal",  "animālis", "3ii",  "N"), \
    ("mare",    "maris",    "3ii",  "N"), \
    ("manus",   "manūs",    "4",    "F"), \
    ("portus",  "portūs",   "4",    "F"), \
    ("cornū",   "cornūs",   "4",    "N"), \
    ("rēs",     "reī",      "5",    "F"), \
    ("diēs",    "diēī",     "5",    "M")
]