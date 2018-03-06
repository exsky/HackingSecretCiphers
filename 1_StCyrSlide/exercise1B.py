#!/usr/local/bin/python

plains = [
	'AMBIDEXTROUS: Able to pick with equal skill a right-hand pocket or a left.',
	'GUILLOTINE: A machine which makes a Frenchman shrug his shoulders with good reason.',
	'IMPIETY: Your irreverence toward my deity.'
]
ciphers = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
keys = [ 4, 17, 21 ]

for plain in plains:
    cipher = ''
    key = keys[ plains.index(plain) ]
    for c in plain:
        if c.isupper():
            index = alpha.index(c.lower())
            cipher += alpha[(index+key)%len(alpha)].upper()
        elif c.islower():
            index = alpha.index(c)
            cipher += alpha[(index+key)%len(alpha)]
        else:
            cipher += c
    ciphers.append(cipher)

for i in ciphers:
    print i


ciphers = [
	'ZXAI: P RDHIJBT HDBTIXBTH LDGC QN HRDIRWBTC XC PBTGXRP PCS PBTGXRPCH XC HRDIAPCS.',
	'MQTSWXSV: E VMZEP EWTMVERX XS TYFPMG LSRSVW.'
]
plains = []
keys = [ 15, 4]

for cipher in ciphers:
    plain = ''
    key = keys[ ciphers.index(cipher) ]
    for c in cipher:
        if c.isupper():
            index = alpha.index(c.lower())
            plain += alpha[(index-key)].upper()
        elif c.islower():
            index = alpha.index(c)
            plainr += alpha[(index-key)]
        else:
            plain += c
    plains.append(plain)

for i in plains:
    print i

