# Russian devoicing example from Kenstowicz and Kisseberth
# p 46
# This version defines moprphological relation Mor
# and phonological relation Phon.  Compose them as
# VMor .o. Phon to map morphology to surface.


# Russian consonants
define Russianc б | в | г | д | ж | з | й | к | л | м | н | п | р | с | т | ф | х | ц | ч | ш | щ | ъ | ь ;
define RussianC Б | В | Г | Д | Ж | З | Й | К | Л | М | Н | П | Р | С | Т | Ф | Х | Ц | Ч | Ш | Щ | Ъ | Ь ;

# Russian vowels
define Russianv а | е | ё | и | о | у | ы | э | ю | я ;
define RussianV А | Е | Ё | И | О | У | Ы | Э | Ю | Я ;

# 20 Noun stems
define Nstem [
 [ {man,person} .x. {человек}] |
 [ {time} .x. {время}] |
 [ {hand,arm,handwriting} .x. {рука}] |
 [ {affair,business,thing,matter} .x. {дело}] |
 [ {time} .x. {раз}] |
 [ {eye} .x. {глаз}] |
 [ {day,afternoon} .x. {день}] |
 [ {life,existence} .x. {жизнь}] |
 [ {here} .x. {тут}] |
 [ {head} .x. {голова}] |
 [ {friend} .x. {друг}] |
 [ {house,home,household} .x. {дом}] |
 [ {word,speech} .x. {слово}] |
 [ {place,site,region,area} .x. {место}] |
 [ {face,right side,person} .x. {лицо}] |
 [ {side,party,land,place,part} .x. {сторона}] |
 [ {foot,leg} .x. {нога}] |
 [ {work,job} .x. {работа}] |
 [ {end,ending} .x. {конец}] |
 [ {door} .x. {дверь}] ];

 # 20 Verb stems
 define Vstem [
  [ {be} .x. {быть}] |
  [ {say,speak,talk,indicate} .x. {сказать}] |
  [ {be able, can} .x. {мочь}] |
  [ {know} .x. {знать}] |
  [ {speak,say,tell} .x. {говорить}] |
  [ {begin,come,become} .x. {стать}] |
  [ {eat,exists} .x. {есть}] |
  [ {want} .x. {хотеть}] |
  [ {see} .x. {видеть}] |
  [ {start,leave,go} .x. {идти}] |
  [ {stand,be,lie,stop} .x. {стоять}] |
  [ {think,consider,believe} .x. {думать}] |
  [ {ask,inquire,demand} .x. {спросить}] |
  [ {live} .x. {жить}] |
  [ {look,see,watch,inspect} .x. {смотреть}] |
  [ {have} .x. {иметь}] |
  [ {understand,comprehend,realize} .x. {понять}] |
  [ {sit,be} .x. {сидеть}] |
  [ {make,do} .x. {делать}] |
  [ {make,do(perf)} .x. {сделать}] |
 ];


# ***** Define the inflections 
define Infl [NomSg : 0] | [DatSg : u];

# **** Define underlying inflected words
define PHRASE Nstem.u "+" Infl.u;

# ***** Define the morphology MOR, mapping a sequence of morphemes to an 
# ***** underlying phone spelling
define M Nstem | "+":0 | Infl; 
define MOR M+;

# Underlying words in their spelling form
define Uword [PHRASE .o. MOR].l;

# Phonology
# ***** Define LDrop, a rule which deletes l in certain contexts.
define LDrop l -> 0 || C _ .#.;

# ***** Define Devoi, a rule which devoices b,d,g,z,ž in final context.
define Devoi b -> p, d -> t, g -> k, z -> s, ž -> š  || _ .#.;

# ***** Define DSD (dental stop deletion), a rule which deletes t,d
# before an l.
# Be careful here to use the right unicode character ť.
define DSD [ t | d | ť ] -> 0 || _ l;

# ***** Define the relation PHON.
define PHON DSD .o. LDrop .o. Devoi;

# ***** Define a finite state lexicon in terms of Phon, Mor, and Phrase.
define Russian PHRASE .o. MOR .o. PHON;

# Define a relation that maps just between underlying and surface phonological forms.
define Russian2 Uword.o. PHON;

