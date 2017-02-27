# -*- coding: utf-8 -*-

p = raw_input('Παρακαλώ εισάγεται αριθμητική παράσταση:')

a = p.count("(")
b = p.count(")")

if (p[0] == ')') or (p[-1] == '('):

    print False

elif (a == b):

    print True

else:

    print False
            
	

	
	
