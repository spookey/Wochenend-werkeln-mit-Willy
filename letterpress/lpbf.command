#!/bin/bash

if [ -z $1 ]; then
	echo "25 characters: "
	read charseq
else
	charseq=$1
fi

PATH="$HOME/coding/wochenend-werkeln-mit-willy.git/letterpress"

/usr/bin/python $PATH"/letterpressbruteforce.py" -c $charseq -d $PATH"/dict.txt" -o $PATH"/"$charseq

if [ -f $PATH/$charseq".txt" ]; then
	$EDITOR $PATH/$charseq".txt"
fi

exit 1
