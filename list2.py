# -*- coding: utf-8 -*-

n=raw_input('Παρακαλώ εισάγεται αριθμούς:')
n=list(n)
count=n.count('0')
for i in range(len(n)):
    if (n[i]=='0'):
        n.remove('0')
        n.append('0')
    print n
