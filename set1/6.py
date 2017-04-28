import os
import sys
from base64 import b64decode, b64encode
import bitarray
import itertools
from collections import defaultdict

# http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

def break_single_XOR(string):
	strings = [(i, ''.join('%s' % chr(ord(cs) ^ i) for cs in string)) for i in range(256)]
	result=[]
	for i, s in strings:
		counter = 0 
		for c in s:
			c = c.lower()	
			if c in freqs:
				counter+=freqs[c]
		result.append((i, counter))	
	return max(result, key=lambda result: result[1])[0]

def count_distance(string1, string2):
	if(len(string1) != len(string2)):
		return 0
	result=0
	b1 = bitarray.bitarray()
	b1.fromstring(string1)
	l1 = b1.tolist()
	b2 = bitarray.bitarray()
	b2.fromstring(string2)
	l2 = b2.tolist()
	for c1,c2 in zip(l1, l2):
		if c1 != c2:
			result+=1
	return result
	
def separate_strings(string, k):
	s = defaultdict(list)
	for i in range(len(string)):
		s[i % k].append(string[i])
	ka = []
	for key in s:
		n = break_single_XOR(''.join(s[key]))
		ka.append(n)
	return ka
	
def get_keysize_scores(string, r):
	scores = []
	for i in range(2, r):
		blocks = [string[x:x+i] for x in range(0, len(string), i)][0:4]
		res = [count_distance(p[0], p[1]) / float(i) for p in list(itertools.combinations(blocks, 2))][0:6]
		scores.append((i, (sum(res) / len(res))))
	return scores

def repeating_key_xor(string, key):
	exp_key = ''.join(key[i % len(key)] for i in range(len(string)))
	res = ''.join("%s" % chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(string, exp_key))
	return res


if __name__ == '__main__':
	with open("6.txt", 'r') as f:
		d = f.read()

	stringd = b64decode(d)

	if count_distance("this is a test", "wokka wokka!!!") != 37:
		print "[-]Test failed!"


	k_size = min(get_keysize_scores(stringd, 40), key = lambda k: k[1])
	key = separate_strings(stringd, k_size[0])
	key = ''.join(chr(c) for c in key)
	print "[+] Found key: %s " % key
	message = repeating_key_xor(stringd, key)
	print "[+] Found messege: \n %s " % message






