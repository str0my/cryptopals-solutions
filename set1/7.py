import os
import sys
import base64	
from Crypto.Cipher import AES

def decrypt_AES(key, text):
	a = AES.new(key, AES.MODE_ECB)
	return a.decrypt(text)

if __name__ == '__main__':
	with open("7.txt", 'r') as f:
		d = f.read()
	string = base64.b64decode(d)
	key = b'YELLOW SUBMARINE'
	print "[+] Decrypted messege: %s" %decrypt_AES(key, string)