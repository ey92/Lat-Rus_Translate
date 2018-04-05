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
    ("eo",          "ire",              "īvī",          0, "пойти",     "идти"), \
    ("sum",         "esse",             "fuī",          0, "есть",      "быть"), \
    ("possum",      "posse",            "potuī",        0, "мочь",      "смочь"), \
    ("volo",        "velle",            "voluī",        0, "хотеть",    "захотеть"), \
    ("nōlo",        "nōlle",            "nōluī",        0, "нехотеть",  "незахотеть"), \
    ("fero",        "ferre",            "tulī",         0, "нести",     "понести"), \
    ("amo",         "amare",            "amāvī",        1, "любить",    "полюбить"), \
    ("cōgito",      "cōgitare",         "cōgitāvī",     1, "думать",    "подумать"), \
    ("paro",        "parare",           "parāvī",       1, "готовить",  "подготовить"), \
    ("rogo",        "rogare",           "rogāvī",       1, "спрашивать","спросить"), \
    ("specto",      "spectare",         "spectāvī",     1, "смотреть",  "посмотреть"), \
    ("sto",         "stare",            "stetī",        1, "стоять",    "постоя́ть"), \
    ("dēleo",       "dēlēre",           "dēlēvī",       2, "уничтожать","уничтожить"), \
    ("habeo",       "habēre",           "habuī",        2, "иметь",     "(no perf)"), \
    ("video",       "vidēre",           "vidī",         2, "видеть",    "увидеть"), \
    ("comprehendo", "comprehendere",    "comprehendī",  3, "понимать",  "понять"), \
    ("dīco",        "dīcere",           "dīxī",         3, "говорить",  "сказать"), \
    ("edo",         "edere",            "ēdī",          3, "есть",      "съесть"), \
    ("peto",        "petere",           "petīvī",       3, "искать",    "поискать"), \
    ("sīdo",        "sīdere",           "sīdī",         3, "сидеть",    "сесть"), \
    ("vīvo",        "vīvere",           "vīxī",         3, "жить",      "прожить"), \
    ("audio",       "audire",           "audīvī",       4, "слышать",   "услышать"), \
    ("scio",        "scire",            "scīvī",        4, "знать",     "узнать"), \
    ("venio",       "venire",           "vēnī",         4, "приходить", "прийти"), \
    ("capio",       "capere",           "cēpī",         5, "брать",     "взять"), \
    ("incipio",     "incipere",         "incēpī",       5, "начать",    "начинать"), \
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
    ("puella",  "puellae",  "1",    "F",    "girl"  ), \
    ("terra",   "terrae",   "1",    "F",    "land"  ), \
    ("femina",  "feminae",  "1",    "F",    "woman" ), \
    ("agricola","agricolae","1",    "M",    "farmer"), \
    ("puer",    "puerī",    "2",    "M",    "boy"   ), \
    ("vir",     "virī",     "2",    "M",    "man"   ), \
    ("filius",  "filiī",    "2",    "M",    "son"   ), \
    ("modus",   "modī",     "2",    "M",    "measure, manner"   ), \
    ("annus",   "annī",     "2",    "M",    "year"  ), \
    ("mūrus",   "mūrī",     "2",    "M",    "wall"  ), \
    ("servus",  "servī",    "2",    "M",    "slave" ), \
    ("liber",   "librī",    "2",    "M",    "book"  ), \
    ("bellum",  "bellī",    "2",    "N",    "war"   ), \
    ("dōnus",   "dōnī",     "2",    "N",    "gift"  ), \
    ("homō",    "hominis",  "3  ",  "M",    "human, person" ), \
    ("rex",     "regis",    "3  ",  "M",    "king"  ), \
    ("consul",  "consulis", "3  ",  "M",    "consul"), \
    ("pānis",   "pānis",    "3  ",  "M",    "bread" ), \
    ("laus",    "laudis",   "3  ",  "F",    "praise"), \
    ("jūs",     "jūris",    "3  ",  "N",    "law"   ), \
    ("flūmen",  "flūminis", "3  ",  "N",    "river" ), \
    ("tempus",  "temporis", "3  ",  "N",    "time"  ), \
    ("nōmen",   "nōminis",  "3  ",  "N",    "name"  ), \
    ("pōns",    "pōntis",   "3i ",  "M",    "bridge"), \
    ("mēnsis",  "mēnsis",   "3i ",  "M",    "month" ), \
    ("nox",     "noctis",   "3i ",  "F",    "night" ), \
    ("mors",    "mortis",   "3i ",  "F",    "death" ), \
    ("urbs",    "urbis",    "3i ",  "F",    "city"  ), \
    ("turris",  "turris",   "3i ",  "F",    "tower" ), \
    ("cīvis",   "cīvis",    "3ii",  "MF",   "citizen"   ), \
    ("nāvis",   "nāvis",    "3ii",  "F",    "ship"  ), \
    ("pārs",    "pārtis",   "3ii",  "F",    "part"  ), \
    ("clāvis",  "clāvis",   "3ii",  "F",    "key"   ), \
    ("animal",  "animālis", "3ii",  "N",    "animal"), \
    ("mare",    "maris",    "3ii",  "N",    "sea"   ), \
    ("manus",   "manūs",    "4",    "F",    "hand"  ), \
    ("portus",  "portūs",   "4",    "F",    "harbor, port"  ), \
    ("cornū",   "cornūs",   "4",    "N",    "horn"  ), \
    ("rēs",     "reī",      "5",    "F",    "thing" ), \
    ("diēs",    "diēī",     "5",    "M",    "day"   ),
]