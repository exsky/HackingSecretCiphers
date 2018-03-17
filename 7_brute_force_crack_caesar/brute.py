#!/usr/local/bin/python

ciphers = [
	'R UXEN VH TRCCH,',
	'FR DBMMR EHOXL FX,',
	'CXPNCQNA FN\'AN BX QJYYH,',
	'OBR OZKOMG QOFSTFSS.',
	'PDKQCD IU DAWZ DWO OQOLEYEKJO,',
	'FTMF U WQQB GZPQD YK TMF,',
	'AR ITMF YUSTF TMBBQZ,',
	'DA D NCMVIF OJ OCZ NDUZ JA V MVO.',
	'ZFBI. J\'N QSFUUZ TVSF NZ DBU XPVME FBU NF.'
]
plains = []
alpha = 'abcdefghijklmnopqrstuvwxyz'

for cipher in ciphers:
    for key in range(len(alpha)):
        plain = ''
        for c in cipher:
            if c.isupper():
                index = alpha.index(c.lower())
                plain += alpha[(index+key)%len(alpha)].upper()
            elif c.islower():
                index = alpha.index(c)
                plain += alpha[(index+key)%len(alpha)]
            else:
                plain += c
        plains.append(plain)

for i in plains:
    print i

