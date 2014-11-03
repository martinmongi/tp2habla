#!/usr/bin/env python

import os
from os import listdir
from os.path import isfile, join

#mypath = 'tp2-dev'
mypath = '../../../Desktop/ith-tp2/test'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

totales = 0
aciertos = 0
print(len(onlyfiles))
for fname in onlyfiles:
	totales += 1
	os.system("./predictor.py ./tp2-dev/"+fname+" > out.out")
	f = open("out.out")
	fstr = f.read()
	f.close()
	os.system("rm out.out")
	print totales
	print(fstr[-2] == fname[-5])
	if fstr[-2] == fname[-5]:
		aciertos += 1
	
print aciertos
print totales
print (aciertos/totales)*100
	
	
