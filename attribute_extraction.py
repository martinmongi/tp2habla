#!/usr/bin/env python

import sys
import os
import re

#==== Extraigo todos los atributos de los archivos ================================================

dir_wavs = os.getcwd() + "/tp2-dev/"

files =  os.listdir(dir_wavs)
files.sort()

os.system("rm attribute_data_raw.arff")

for f in files:
	print "Procesando " + f
	os.system("./opensmile/SMILExtract -C ./opensmile/config/IS10_paraling.conf -I ./tp2-dev/" + f + " -O attribute_data_raw.arff > /dev/null 2> /dev/null")

#==== Ahora tengo que incluir en los atributos de cada archivo si es hombre o mujer ===============

raw_data = open("./attribute_data_raw.arff",'r')
mod_data = open("./attribute_data.arff",'w')

line = raw_data.readline()

while line != "@data\n" and line != "":
	mod_data.write(line)
	line = raw_data.readline()

mod_data.write(line) #@data

line = raw_data.readline()
mod_data.write(line) # linea vacia




for f in files:
	line = raw_data.readline()
	split_line = line.split(',')
	split_line[0] = "\'" + f + "\'"
	if f[4] == 'm':
		split_line[-1] = '1.0\n'
	mod_data.write(','.join(split_line))


raw_data.close()
mod_data.close()

os.system("rm attribute_data_raw.arff")