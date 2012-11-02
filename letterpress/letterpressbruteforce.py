#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mklist(file):
	l = []
	f = open(file, 'r')
	for line in f.readlines():
		word = line.strip()
		l.append(word)
	f.close()
	return l


def writeout(lst, name, noc):
	t = open(name+'.txt', 'w')
	for line in lst:
		if len(line) >= noc:
			t.write(line+'\n')
	t.close()


def main():
	worlist = mklist('dict.txt')
	chars = raw_input("Letterpress Characters: ")
	
	result = []

	for word in worlist:
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
		else:
			continue
	
	writeout(sorted(result), str(chars), 8)


if __name__ == '__main__':
	main()
