rm attribute_data.arff

for f in ./tp2-dev/*.wav
do
	./opensmile/SMILExtract -C ./opensmile/config/IS10_paraling.conf -I "$f" -O attribute_data.arff > /dev/null 2> /dev/null
done