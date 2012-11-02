#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import argparse

# Wörterbuch erzeugen
def mkDict(file):
	d = defaultdict(list)
	with open(file, 'r') as f:
		for line in f.readlines():
			if line[0].isupper(): continue
			word = line.strip()
			key = ''.join(sorted(word.lower()))
			d[key].append(word)
	return d

# Sucht Wörter aus dem Wörterbuch raus (Achtung: Listen müssen sortiert sein!)
def contains(word, candidate):
	wchars = (c for c in word)
	for cc in candidate:
		while(True):
			try:
				wc = wchars.next()
			except StopIteration:
				return False
			if wc < cc: continue
			if wc == cc: break
			return False
	return True

# Ergebins auf Platte schreiben (lst: Liste der Elemente, name: Dateiname, noc: Mindestanzahl d. Buchstaben)
def writeout(lst, name, noc):
	t = open(name+'.txt', 'w')
	for line in lst:
		if len(line) >= noc: t.write(line+'\n')
	t.close()

def argParse():
	parser = argparse.ArgumentParser(description='Letterpress')
	parser.add_argument('-c', action='store', dest='charseq', help='Gib die 25 Buchstaben gleich als Argument an')
	parser.add_argument('-d', action='store', dest='dictpath', help='Ort der dict.txt')
	return parser.parse_args()

# Die schlimme Main-Funktion
def main():
	eingabe = argParse()

	if not eingabe.charseq:
		src = raw_input("Letterpress Characters: ")
	else:
		src = eingabe.charseq	
	
	if not eingabe.dictpath == None:
		dtxt = eingabe.dictpath
	else:
		dtxt = './dict.txt'
	
	print eingabe

	print src
	print dtxt

	dc = mkDict(dtxt) # Das Wörterbuch (Readme.md beachten)
	ml = 8 # Mindestanzahl von Buchstaben, die ein Wort haben soll
	
	
	
	w = sorted(src)
	result = []
	for k in dc.keys():
		if contains(w, k): result.extend(dc[k])
	
	writeout(sorted(result), str(src), ml)

if __name__ == '__main__':
	main()
