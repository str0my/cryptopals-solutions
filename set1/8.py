import os
import sys
import itertools

def detect_ECB(string):
	k = 16
	blocks = [string[i:i+k] for i in range(0, len(string), k)]
	counter = 0
	for x in itertools.combinations(blocks, 2):
		if x[0] == x[1]:
			counter+=1
	return counter

if __name__ == '__main__':
	with open('8.txt', 'r') as f:
		d = f.readlines()
	scores = []
	for i, l in enumerate(d):
		scores.append((i,detect_ECB(l)))
	print "[+] ECB most probably in line: %d" % max(scores, key=lambda scores: scores[0])[0]