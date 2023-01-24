# mode 1 lower case ASCII
# mode 2 lower and upper case ASCII
# mode 3 memorable word
# mode 4 alphanumeric upper and lower case
# mode 5 numberic
# mode 6 hexadecimal

# used for currently unidentified routers from either Zyxel or D-link
# found in /usr/bin of the binwalked firmware of the
# Zyxel LTE3301-M209 (LTE3301-M209_V1.00(ABLG.0)C0.zip)

import hashlib
import argparse
import numpy
from numpy.linalg import matrix_power

def passgen(input, pwd_length, mode):

	numbers = "0123456789"
	vowels_lc = "aeiou"
	vowels_uc = "AEIOU"
	cons_lc = "bcdfghjklmnpqrstvwxyz"
	cons_uc = "BCDFGHJKLMNPQRSTVWXYZ"
	hexx = "abcdef"

	if mode == 1:
		charset = vowels_lc + cons_lc
	elif mode == 2:
		charset = vowels_lc + vowels_uc + cons_lc + cons_uc
	elif mode == 3:
		charset = cons_uc
	elif mode == 4:
		charset = vowels_lc + vowels_uc + cons_lc + cons_uc + numbers
	elif mode == 5:
		charset = numbers
	elif mode == 6:
		charset = numbers + hexx

	hashh = hashlib.md5()
	hashh.update(input.encode())
	digest = hashh.digest()

	pwd = ''
	for i in range(pwd_length):
		hashh2 = hashlib.md5()
		hashh2.update(digest)
		new_digest = hashh2.digest()
		long_int = 0
		long_int = long_int + new_digest[0]
		long_int = long_int + new_digest[1] * 2 ** 8
		long_int = long_int + new_digest[2] * 2 ** 16
		long_int = long_int + new_digest[3] * 2 ** 24

		char_pos = long_int % len(charset)
		letter = charset[char_pos]
		pwd += letter
		if mode == 3:
			if len(charset) == 5:
				charset = cons_lc
			else:
				charset = vowels_lc
		digest = new_digest
	print(pwd)



parser = argparse.ArgumentParser(description='Passgen')
parser.add_argument('input', help='Input')
parser.add_argument('mode', help='Mode to use.', choices=[1,2,3,4,5,6], type=int)
parser.add_argument('-length', help='Password length, default is 10.', default=10, type=int)
args = parser.parse_args()

passgen(args.input, args.length, args.mode)
