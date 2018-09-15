Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = '{} Sasha'
>>> h = s.format('Hello')
>>> h
'Hello Sasha'
>>> s = '{} Sasha. {}?'
>>> h = s.format('Hello','How are you')
>>> h
'Hello Sasha. How are you?'
>>> s = '{}k{}t{}b{}'
>>> s
'{}k{}t{}b{}'
>>> s.format('','u','taa',''))
SyntaxError: invalid syntax
>>> s.format('','u','taa','')
'kuttaab'
>>> x = 'happiness'
>>> x[5]
'n'
>>> x.count('s')
2
>>> x[2:4]
'pp'
>>> l = [2,3,6,7]
>>> len(l)
4
>>> l[3]
7
>>> l.append('light')
>>> l
[2, 3, 6, 7, 'light']
>>> l.pop(2)
6
>>> l
[2, 3, 7, 'light']
>>> l.insert(1, 'zhenka')
>>> l
[2, 'zhenka', 3, 7, 'light']
>>> x = list(range(4))
>>> x
[0, 1, 2, 3]
>>> x = [5,7,8,2]
>>> x
[5, 7, 8, 2]
>>> 7 in x
True
>>> z = (4,7,8)
>>> type(z)
<class 'tuple'>
>>> len(z)
3
>>> z[0]
4
>>> 9 in z
False
>>> d = {'cat':'koshka','chair':'stul'}
>>> type(d)
<class 'dict'>
>>> d['cat']
'koshka'
>>> len(d)
2
>>> 'dom' in d
False
>>> 'stul' in d
False
>>> del(d['chair'])
>>> d
{'cat': 'koshka'}
>>> list(d.keys())
['cat']
>>> list(d.values())
['koshka']
>>> list(d.items())
[('cat', 'koshka')]
>>> r = {'apple', 'banana'}
>>> 
>>> 
========== RESTART: D:/Новый питоша/2 курс питошим/15 sentyabrya.py ==========
pa
ta
ka
po
to
ko
>>> 
========== RESTART: D:/Новый питоша/2 курс питошим/15 sentyabrya.py ==========
mamamylamama
mamamylarama
mamakrasilamama
mamakrasilarama
ramamylamama
ramamylarama
ramakrasilamama
ramakrasilarama
>>> 
========== RESTART: D:/Новый питоша/2 курс питошим/15 sentyabrya.py ==========
JenechekbotaetJenechek
Jenechekbotaetpirozhpchek
JenechekrabotaetJenechek
Jenechekrabotaetpirozhpchek
pirozhpchekbotaetJenechek
pirozhpchekbotaetpirozhpchek
pirozhpchekrabotaetJenechek
pirozhpchekrabotaetpirozhpchek
>>> 
========== RESTART: D:/Новый питоша/2 курс питошим/15 sentyabrya.py ==========
Jenechek botaet Jenechek
Jenechek botaet pirozhpchek
Jenechek rabotaet Jenechek
Jenechek rabotaet pirozhpchek
pirozhpchek botaet Jenechek
pirozhpchek botaet pirozhpchek
pirozhpchek rabotaet Jenechek
pirozhpchek rabotaet pirozhpchek
>>> 
=============== RESTART: D:/Новый питоша/2 курс питошим/-1.py ===============
>>> 
