# -*- coding: utf-8 -*-

x= raw_input('Παρακαλώ εισάγεται αριθμητική παράσταση:')

count_a = x.count("(")
count_b = x.count(")")

if (x[0] == ')') or (x[-1] == '('):

    print False
    print('Δεν έγινε εισαγωγή αριθμιτικής παράστασης,προσπαθείστε ξανά')

elif (count_a == count_b):

    print True
    print('Επιτυχής εισαγωγή αριθμιτικής παράστασης')

else:

    print False
    print ('Δεν έγινε εισαγωγή αριθμιτικής παράστασης,προσπαθείστε ξανά')
            
	

	
	
