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
    ("eo","ire","īvī",0), \
    ("sum","esse","fuī",0), \
    ("possum","posse","potuī",0), \
    ("volo","velle","voluī",0), \
    ("nōlo","nōlle","nōluī",0), \
    ("fero","ferre","tulī",0), \
    ("amo","amare","amāvī",1), \
    ("dēleo","dēlēre","dēlēvī",2), \
    ("peto","petere","petīvī",3), \
    ("venio","venire","vēnī",4), \
    ("capio","capere","cēpī",5) \
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
    ("puella","puellae","1","F"), \
    ("agricola","agricolae","1","M"), \
    ("puer","puerī","2","M"), \
    ("filius","filiī","2","M"), \
    ("mūrus","mūrī","2","M"), \
    ("bellum","bellī","2","N"), \
    ("manus","manūs","4","F"), \
    ("cornū","cornūs","4","N"), \
    ("rēs","reī","5","F"), \
    ("diēs","diēī","5","N")
]