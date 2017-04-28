import base64

hex_string= '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

if __name__ == '__main__':
	plain_string = hex_string.decode('hex')
	print "[+] Plain string: %s" % plain_string
	base64_encoded = base64.b64encode(plain_string)
	print "[+] Base64 encoded: %s" % base64_encoded 
