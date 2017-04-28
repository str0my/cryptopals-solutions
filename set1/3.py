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


if __name__ == '__main__':

	string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

	key = break_single_XOR(string)
	print "[+] Decrypted messege: %s" % ''.join(chr( ord(string[i]) ^ key) for i in range(len(string)))