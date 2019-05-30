#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3 code implementing the Vigenère Cipher using the base58 alphabet 
import argparse
B58_DIGITS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
replacement_characters = {'0':'o','l':'1','I':'1','O':'o'}

def get_base_58_index(character):
	replaced_char = replacement_characters.get(character,character)
	if(replaced_char is not character):
	    print("Replacing '"+character+"' with '"+replaced_char+"'")
	for i in range(len(B58_DIGITS)):
		if(replaced_char==B58_DIGITS[i]):
			return i
	print("No char: '"+character+"' (or suitable) in base58 alphabet so replacing with 'X'")
	return 30

parser = argparse.ArgumentParser(prog='base58vigenere', usage='python base58vigenere.py --encrypt/--decrypt [message] [key]')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encrypt', action="store_const", 
    dest="mode", const="encrypt")
group.add_argument('-d', '--decrypt', action="store_const", 
    dest="mode", const="decrypt")
parser.add_argument('message', help='message or ciphertext to encrypt/decrypt')
parser.add_argument('key', help='Vigenère key')
args = parser.parse_args()

vargs = vars(args)
operating_direction = 0
if vargs['mode']=="decrypt":
	print("Decrypting: "+vargs['message'])
	operating_direction = -1
else:
	print("Encrypting: "+vargs['message'])
	operating_direction = 1

message = vargs['message']
key = list(vargs['key'])

# Buff the key to the full length of the message if necessary
for i in range(len(message) - len(key)): 
            key.append(key[i % len(key)]) 
key = ("" . join(key))

resulting_text = []
for i in range(len(message)): 
        x = (get_base_58_index(message[i]) +
         (operating_direction * ord(key[i]))) % 58
        resulting_text.append(B58_DIGITS[x]) 
		
resulting_text = ("" . join(resulting_text))
print(resulting_text)