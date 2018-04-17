# Elizabeth Yam ey92
# -*- coding: utf-8 -*-
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

ire , FST , SG , PRES 
esse, TRD, PL, PLUP

macronLow = ['ā', 'ē', 'ī', 'ō', 'ū']

puella, puellae, ABL, PL, 1, F
"puella", "puellae", "1", "F", "ABL", "PL"

labor, laboris, ACC, SG, 3, M
"labor", "laboris", "3", "M", "ACC", "SG"

'pulcher','pulchra','12','N','ABL','SG'
 pulcher , pulchra , 12 , N , ABL , SG 

ā
ī
ū
ē
ō

['у','ёшь','ёт','ём','ёте','ут']
['ю','ешь','ет','ем','ете','ют']
['у','ищь','ит','им','ите','ат']
['ю','ишь','ит','им','ите','ат']

'читать','SND','PL','','PRES'
читать, SND, PL, , PRES

'прочитать','SND','PL','','PRES'
прочитать , SND , PL , , PRES

'сказать','','PL','F','PERF'
сказать , , PL , F , PERF 

'говорить','','PL','F','PERF'
говорить , , PL , F , PERF

'жить','FST','SG','','FUTR'
жить , FST , SG , , FUTR

'прожить','FST','SG','','FUTR'
прожить , FST , SG ,  , FUTR

Irregular verbs: 
мочь, дать, есть, взять/брать, 
закрыть, класть, ждать, жить, 
ехать, идти, писать, хотеть and their derivatives.

писать,закрыть is handled by going to 3P for root

['\xd1\x87\xd0\xb8\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c','\xd0\xbf\xd1\x80\xd0\xbe\xd1\x87\xd0\xb8\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c','\xd0\xb8\xd1\x81\xd0\xba\xd0\xb0\xd1\x82\xd1\x8c','\xd0\xbf\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba\xd0\xb0\xd1\x82\xd1\x8c','\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xb5\xd1\x82\xd1\x8c','\xd0\xbf\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xb5\xd1\x82\xd1\x8c','\xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x8c','\xd0\xbe\xd0\xb1\xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x8c']

'класть', 'положить' - положи́ть is regular

print(Russian.decline('время','NOM','PL'))
print(Russian.decline('время','GEN','PL'))
print(Russian.decline('время','DAT','PL'))
print(Russian.decline('время','ACC','PL'))
print(Russian.decline('время','PRP','PL'))
print(Russian.decline('время','INS','PL'))
print(Russian.decline('время','NOM','SG'))
print(Russian.decline('время','GEN','SG'))
print(Russian.decline('время','DAT','SG'))
print(Russian.decline('время','ACC','SG'))
print(Russian.decline('время','PRP','SG'))
print(Russian.decline('время','INS','SG'))