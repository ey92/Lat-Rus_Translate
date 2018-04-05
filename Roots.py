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

# 26 Verb stems
VMap = [
    ("ire",              "пойти",       "to go"             ), \
    ("esse",             "есть",        "to be"             ), \
    ("posse",            "мочь",        "to be able"        ), \
    ("velle",            "хотеть",      "to want"           ), \
    ("nōlle",            "нехотеть",    "to not want"       ), \
    ("ferre",            "нести",       "to bring, carry"   ), \
    ("amare",            "любить",      "to love"           ), \
    ("cōgitare",         "думать",      "to think"          ), \
    ("parare",           "готовить",    "to prepare"        ), \
    ("rogare",           "спрашивать",  "to ask"            ), \
    ("spectare",         "смотреть",    "to watch"          ), \
    ("stare",            "стоять",      "to stand"          ), \
    ("dēlēre",           "уничтожать",  "to destroy"        ), \
    ("habēre",           "иметь",       "to have"           ), \
    ("vidēre",           "видеть",      "to see"            ), \
    ("comprehendere",    "понимать",    "to understand"     ), \
    ("dīcere",           "говорить",    "to say"            ), \
    ("edere",            "есть",        "to eat"            ), \
    ("petere",           "искать",      "to seek"           ), \
    ("sīdere",           "сидеть",      "to sit"            ), \
    ("vīvere",           "жить",        "to live"           ), \
    ("audire",           "слышать",     "to hear"           ), \
    ("scire",            "знать",       "to know"           ), \
    ("venire",           "приходить",   "to come"           ), \
    ("capere",           "брать",       "to take"           ), \
    ("incipere",         "начать",      "to begin"          ) \
]
VMap_lat = [x[0] for x in VMap]
VMap_rus = [x[1] for x in VMap]
VMap_eng = [x[2] for x in VMap]

# -------------------------------------------------------------
# LATIN
LatinV = [
    ("eo",          "ire",              "īvī",          0, "to go",             "пойти",     "идти"), \
    ("sum",         "esse",             "fuī",          0, "to be",             "есть",      "быть"), \
    ("possum",      "posse",            "potuī",        0, "to be able",        "мочь",      "смочь"), \
    ("volo",        "velle",            "voluī",        0, "to want",           "хотеть",    "захотеть"), \
    ("nōlo",        "nōlle",            "nōluī",        0, "to not want",       "нехотеть",  "незахотеть"), \
    ("fero",        "ferre",            "tulī",         0, "to bring, carry",   "нести",     "понести"), \
    ("amo",         "amare",            "amāvī",        1, "to love",           "любить",    "полюбить"), \
    ("cōgito",      "cōgitare",         "cōgitāvī",     1, "to think",          "думать",    "подумать"), \
    ("paro",        "parare",           "parāvī",       1, "to prepare",        "готовить",  "подготовить"), \
    ("rogo",        "rogare",           "rogāvī",       1, "to ask",            "спрашивать","спросить"), \
    ("specto",      "spectare",         "spectāvī",     1, "to watch",          "смотреть",  "посмотреть"), \
    ("sto",         "stare",            "stetī",        1, "to stand",          "стоять",    "постоя́ть"), \
    ("dēleo",       "dēlēre",           "dēlēvī",       2, "to destroy",        "уничтожать","уничтожить"), \
    ("habeo",       "habēre",           "habuī",        2, "to have",           "иметь",     "(no perf)"), \
    ("video",       "vidēre",           "vidī",         2, "to see",            "видеть",    "увидеть"), \
    ("comprehendo", "comprehendere",    "comprehendī",  3, "to understand",     "понимать",  "понять"), \
    ("dīco",        "dīcere",           "dīxī",         3, "to say",            "говорить",  "сказать"), \
    ("edo",         "edere",            "ēdī",          3, "to eat",            "есть",      "съесть"), \
    ("peto",        "petere",           "petīvī",       3, "to seek",           "искать",    "поискать"), \
    ("sīdo",        "sīdere",           "sīdī",         3, "to sit",            "сидеть",    "сесть"), \
    ("vīvo",        "vīvere",           "vīxī",         3, "to live",           "жить",      "прожить"), \
    ("audio",       "audire",           "audīvī",       4, "to hear",           "слышать",   "услышать"), \
    ("scio",        "scire",            "scīvī",        4, "to know",           "знать",     "узнать"), \
    ("venio",       "venire",           "vēnī",         4, "to come",           "приходить", "прийти"), \
    ("capio",       "capere",           "cēpī",         5, "to take",           "брать",     "взять"), \
    ("incipio",     "incipere",         "incēpī",       5, "to begin",          "начать",    "начинать") \
]
LatinV_fs = [x[0] for x in LatinV]
LatinV_inf = [x[1] for x in LatinV]
LatinV_perf = [x[2] for x in LatinV]
LatinV_conj = [x[3] for x in LatinV]
LatinV_eng = [x[4] for x in LatinV]
LatinV_rus_impf = [x[5] for x in LatinV]
LatinV_rus-perf = [x[6] for x in LatinV]

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
    ("puella",  "puellae",  "1",    "F",    "girl",             "девочка"), \
    ("terra",   "terrae",   "1",    "F",    "land",             "земля"), \
    ("femina",  "feminae",  "1",    "F",    "woman",            "женщина"), \
    ("agricola","agricolae","1",    "M",    "farmer",           "земледелец"), \
    ("puer",    "puerī",    "2",    "M",    "boy",              "мальчик"), \
    ("vir",     "virī",     "2",    "M",    "man",              "мужчина"), \
    ("filius",  "filiī",    "2",    "M",    "son",              "сын"), \
    ("modus",   "modī",     "2",    "M",    "measure, manner",  "способ"), \
    ("annus",   "annī",     "2",    "M",    "year",             "год"), \
    ("mūrus",   "mūrī",     "2",    "M",    "wall",             "стена"), \
    ("servus",  "servī",    "2",    "M",    "slave, servant",   "раб"), \
    ("liber",   "librī",    "2",    "M",    "book",             "книга"), \
    ("bellum",  "bellī",    "2",    "N",    "war",              "война"), \
    ("dōnus",   "dōnī",     "2",    "N",    "gift",             "подарок"), \
    ("homō",    "hominis",  "3  ",  "M",    "human, person",    "человек"), \
    ("rex",     "regis",    "3  ",  "M",    "king",             "царь"), \
    ("consul",  "consulis", "3  ",  "M",    "consul",           "консул"), \
    ("pānis",   "pānis",    "3  ",  "M",    "bread",            "хлеб"), \
    ("laus",    "laudis",   "3  ",  "F",    "praise",           "похвала"), \
    ("jūs",     "jūris",    "3  ",  "N",    "law",              "право"), \
    ("flūmen",  "flūminis", "3  ",  "N",    "river",            "река"), \
    ("tempus",  "temporis", "3  ",  "N",    "time",             "время"), \
    ("nōmen",   "nōminis",  "3  ",  "N",    "name",             "имя"), \
    ("pōns",    "pōntis",   "3i ",  "M",    "bridge",           "мост"), \
    ("mēnsis",  "mēnsis",   "3i ",  "M",    "month",            "месяц"), \
    ("nox",     "noctis",   "3i ",  "F",    "night",            "ночь"), \
    ("mors",    "mortis",   "3i ",  "F",    "death",            "смерть"), \
    ("urbs",    "urbis",    "3i ",  "F",    "city",             "город"), \
    ("turris",  "turris",   "3i ",  "F",    "tower",            "башня"), \
    ("cīvis",   "cīvis",    "3ii",  "M",    "citizen",          "гражданин"), \
    ("nāvis",   "nāvis",    "3ii",  "F",    "ship",             "корабль"), \
    ("pārs",    "pārtis",   "3ii",  "F",    "part",             "доля"), \
    ("clāvis",  "clāvis",   "3ii",  "F",    "key",              "ключ"), \
    ("animal",  "animālis", "3ii",  "N",    "animal",           "животное"), \
    ("mare",    "maris",    "3ii",  "N",    "sea",              "море"), \
    ("manus",   "manūs",    "4",    "F",    "hand",             "рука"), \
    ("portus",  "portūs",   "4",    "F",    "harbor, port",     "порт"), \
    ("cornū",   "cornūs",   "4",    "N",    "horn",             "рог"), \
    ("rēs",     "reī",      "5",    "F",    "thing",            "вещь"), \
    ("diēs",    "diēī",     "5",    "M",    "day",              "день") \
]
LatinN_ns = [x[0] for x in LatinN]
LatinN_gs = [x[1] for x in LatinN]
LatinN_decl = [x[2] for x in LatinN]
LatinN_gender = [x[3] for x in LatinN]
LatinN_eng = [x[4] for x in LatinN]
LatinN_rus = [x[5] for x in LatinN]