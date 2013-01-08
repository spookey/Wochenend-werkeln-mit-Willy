#!/bin/bash

if [ -z $1 ]; then
	echo "25 characters: "
	read charseq
else
	charseq=$1
fi

FOLDER="$HOME/coding/wochenend-werkeln-mit-willy.git/letterpress"

if [ ! -r $FOLDER"/dict.dat" ]; then
	/usr/bin/unzip -p $HOME'/Music/iTunes/iTunes Media/Mobile Applications/Letterpress 1.2.ipa' 'Payload/Letterpress.app/o/*txt' > $FOLDER"/dict.dat"
fi

/usr/bin/python $FOLDER"/letterpressbruteforce.py" -c $charseq -d $FOLDER"/dict.dat" -o $FOLDER"/"$charseq

if [ -f $FOLDER/$charseq".txt" ]; then
	$EDITOR $FOLDER/$charseq".txt"
fi

exit 1
