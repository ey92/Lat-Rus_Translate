vow = [u'а', u'е', u'ё', u'и', u'о', u'у', u'ы', u'э', u'ю', u'я']
vowCap = [u'А' , u'Е' , u'Ё' , u'И' , u'О' , u'У' , u'Ы' , u'Э' , u'Ю' , u'Я']
cons = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'к', u'л', u'м', u'н', u'п', u'р', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ъ', u'ь']
consCap = [u'Б', u'В', u'Г', u'Д', u'Ж', u'З', u'Й', u'К', u'Л', u'М', u'Н', u'П', u'Р', u'С', u'Т', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ь']
letters = vow+cons
letterCap = vowCap+consCap

print(consonants[0].encode('utf8'))

a = u'человек'
print a.encode('utf8')
print(u'человек')
# https://stackoverflow.com/questions/16218274/convert-unicode-cyrillic-symbols-to-string-in-python
# https://en.openrussian.org/list/nouns
# https://en.openrussian.org/list/verbs

'\xd1\x83'
u'\u0443'
consonants.index(('в').decode('utf8'))
def fooL(letter):
    return letters.index(letter)
# in: ч | out: ч

def foo(word):
    word = word.decode('utf8')
    lst = []
    for letter in word:
        lst.append(fooL(letter))
    return lst
print ','.join(map(str,foo(y)))

"eram" in Latin.plupEndings.values()
*future* m or o

1st sg
m: impf(12345), fut(345), plup(12345)
o: pres(12345), fut(12), futp(12345)
i: perf(12345)

ire , īvī , 0 , FST , SG , PRES 
esse, fuī, 0, TRD, PL, PLUP

macronLow = ['ā', 'ē', 'ī', 'ō', 'ū']

puella, puellae, 1, F, ABL, PL
"puella", "puellae", "1", "F", "ABL", "PL"

labor, laboris, 3, M, ACC, SG
"labor", "laboris", "3", "M", "ACC", "SG"

'pulcher','pulchra','12','N','ABL','SG'

ārum
ī
ā
ū
ēī
īs
ēs
ēbus
ūs
ōrum
ōs