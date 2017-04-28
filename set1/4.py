import sys
import os

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

def get_correct_hex_strings(f):
	strings = []
	for s in f:
		try:
			strings.append(s.strip().decode('hex'))
		except TypeError:
			continue
	return strings

def repeating_key_xor(string, key):
	exp_key = ''.join(key[i % len(key)] for i in range(len(string)))
	res = ''.join("%s" % chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(string, exp_key))
	return res

if __name__ == '__main__':
	with open('4.txt', 'r') as f:
		d = f.readlines()
	strings = get_correct_hex_strings(d)
	result=[]
	for s in strings:
		s = repeating_key_xor(s, chr(break_single_XOR(s)))
		counter = 0 
		for c in s:
			c = c.lower()	
			if c in freqs:
				counter+=freqs[c]
		result.append((counter, s))	
	print "[+] Found messege: %s" % max(result, key=lambda result: result[0])[1]