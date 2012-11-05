#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

def mklist(file):
	l = []
	try: f = open(file, 'r')
	except IOError, err: sys.exit('ERROR! %s could not be read - %s\n' %(file, err))
	else:
		for line in f.readlines():
			word = line.strip()
			l.append(word)
		f.close()
	return l


def writeout(lst, name, noc):
	try: t = open(name+'.txt', 'w')
	except IOError, err: sys.exit('ERROR! %s could not be written - %s\n' %(file, err))
	else:
		for line in lst:
			if len(line) >= noc:
				t.write(line+'\n')
		t.close()


def aparse():
	parser = argparse.ArgumentParser(description='Letterpress')
	parser.add_argument('-c', action='store', dest='charseq', help='Gib die 25 Buchstaben gleich als Argument an')
	parser.add_argument('-d', action='store', dest='dictpath', help='Ort der dict.txt')
	parser.add_argument('-o', action='store', dest='out', help='Wohin soll die Ausgabe gespeichert werden ?')
	parser.add_argument('-n', action='store', dest='noc', help='Buchstaben mindestlänge')
	parser.add_argument('--version', action='version', version='%(prog)s - it\'s over 9000!!!!1!einself!')
	return parser.parse_args()

def setdefault(default, fallback):
	if default == None: return fallback
	else: return default

def main():
	entry = aparse()

	if entry.charseq is None: chars = raw_input("Letterpress Characters: ")
	else: chars = entry.charseq

	wordlist = mklist(setdefault(entry.dictpath, 'dict.txt'))
	noc = setdefault(entry.noc, 8)
	outlist = setdefault(entry.out, chars)


	result = []

	for word in wordlist:
		if set(word).issubset(set(chars)):
			for letter in word:
				if word.count(letter) <= chars.count(letter):
					goodWord = True
				else:
					goodWord = False
					break

		else:
			goodWord = False
			
		if goodWord:
			result.append(word)
	
	writeout(sorted(result), str(outlist), int(noc))


if __name__ == '__main__':
	main()
