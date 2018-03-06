#!/usr/local/bin/python

plains = ['Eat food.','Mostly plants.','Not too much.']
ciphers = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
key = 5

for plain in plains:
    cipher = ''
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
print ciphers

ciphers = ["Z YRMV DP WRKYVI'J VPVJ.", "REU DP DFKYVI'J EFJV.", "ZE R ARI LEUVI DP SVU."]
plains = []
key = 17

for cipher in ciphers:
    plain = ''
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
print plains


