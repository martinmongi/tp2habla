#!/usr/bin/env python
import sys, os, re

WEKA_PATH = "/usr/share/java/weka.jar"

#==== Extraigo los atributos ======================================================================

args = sys.argv
os.system("rm -f output.arff")
os.system("rm -f output_filtered.arff")
os.system("rm -f pred.arff")
os.system("./opensmile/SMILExtract  -noconsoleoutput -C ./opensmile/config/IS10_paraling.conf -I " + args[1] + " -O output.arff > /dev/null")

# Dejamos solo los 40 atributos mas relevantes
os.system("java -cp " + WEKA_PATH + " weka.filters.unsupervised.attribute.Remove -V -R 685,684,676,1441,1432,1442,678,686,1440,691,713,712,256,327,258,271,277,1330,279,285,270,663,664,655,1343,706,1321,1391,291,292,598,78,313,83,245,235,640,133,1547,943,1584 -i output.arff -o output_filtered.arff")

# Cambiamos el gender a mano del archivo
f = open("output_filtered.arff","r")
f.readline()
fstr = f.read()
f.close()

result = re.sub(r"@attribute numeric_class numeric", "@attribute gender {m,f}", fstr)
result = "@relation 'instance'\n" + result[:-2] + "?\n"

f = open("output_filtered.arff",'w')
f.write(result)
f.close()

# Ejecutamos el clasificador
os.system("java -cp " + WEKA_PATH + " weka.filters.supervised.attribute.AddClassification \
  -serialized smo.model \
  -classification \
  -remove-old-class \
  -i output_filtered.arff \
  -o pred.arff \
  -c last")

# Devolvemos la ultima linea del archivo de salida
f = open("pred.arff","r")
f.readline()
fstr = f.read()
f.close()

print(fstr[-2])

# Limpiamos
os.system("rm -f output.arff")
os.system("rm -f output_filtered.arff")
os.system("rm -f pred.arff")