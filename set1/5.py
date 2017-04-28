import sys
import os

def repeating_key_xor(string, key):
	exp_key = ''.join(key[i % len(key)] for i in range(len(string)))
	res = ''.join("%s" % chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(string, exp_key))
	return res

if __name__ == '__main__':

	string= """Burning 'em, if you ain't quick and nimble
	I go crazy when I hear a cymbal"""
	key = "ICE"

	result = repeating_key_xor(string, key)
	print "[+] Key: %s" % key
	print "[+] Hex encoded: %s" % result.encode('hex')