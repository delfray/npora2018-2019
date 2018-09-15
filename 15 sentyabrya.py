#5.1
#import random
#con = 'ptk'
#vow = 'ao'
#for v in vow:
 #   for c in con:
  #      print(c+v)

#5.2
#nouns = 'mama rama'
#verbs = 'myla krasila'
#for s in nouns.split():
 #   for v in verbs.split():
  #      for o in nouns.split():
   #         print(s+''+v+''+o)
              
nouns = 'Jenechek pirozhochek'
verbs = 'botaet rabotaet'
for n in nouns.split():
    for v in verbs.split():
        for o in nouns.split():
            print(n+' '+v+' '+o)
