import sys
import os

def xor_string(s1, s2):
	return ''.join('%s' % chr(ord(c1)^ord(c2)) for c1, c2 in zip(s1, s2))


if __name__ == '__main__':

	string1 = '1c0111001f010100061a024b53535009181c'.decode('hex')
	string2 = '686974207468652062756c6c277320657965'.decode('hex')

	print "[+] First string: %s" % string1
	print "[+] Second string: %s" % string2

	print "[+] XOR'ed: %s" % xor_string(string1, string2)