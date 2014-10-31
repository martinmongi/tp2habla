import sys, os

#==== Extraigo los atributos ======================================================================

args = sys.argv
os.system("rm output.arff")
os.system("./opensmile/SMILExtract -C ./opensmile/config/IS10_paraling.conf -I " + args[1] + " -O output.arff")
