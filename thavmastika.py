# -*- coding: utf-8 -*-

p=raw_input('Παρακαλώ εισάγεται την πρόταση που επιθυμείτε:')

count=p.count("!")-1
new_p=p.replace('!','',count)

      
print "".join(new_p)

        
