#!/usr/local/bin/python

message = 'Three can keep a secret, if two of them are dead.'

str = raw_input("The input message is : ")
inv = ''

for c in str:
    inv = c + inv

print inv
