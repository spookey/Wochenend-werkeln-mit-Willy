#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

def mkdict(file):
	d = defaultdict(list)
	with open(file, 'r') as f:
		for line in f.readlines():
			if line[0].isupper(): continue
			word = line.strip()
			key = ''.join(sorted(word.lower()))
			d[key].append(word)
	return d

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

def writeout(lst, name, noc):
	t = open(name+'.txt', 'w')
	for line in lst:
		if len(line) >= noc:
			t.write(line+'\n')
	t.close()

def main():
	dict = mkdict('dict.txt')
	
	src = raw_input("Letterpress Characters: ")
	
	w = sorted(src)
	result = []
	for k in dict.keys():
		if contains(w, k): result.extend(dict[k])
	
	writeout(sorted(result), str(src), 8)

if __name__ == '__main__':
	main()
