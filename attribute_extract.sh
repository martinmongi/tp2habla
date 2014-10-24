rm ./attribute_extract.log ./attribute_extract.err

for f in ./tp2-dev/*.wav
do
	./opensmile/SMILExtract -C ./opensmile/config/IS10_paraling.conf -I "$f" -O "$f".arff >> ./attribute_extract.log 2>> ./attribute_extract.err
done