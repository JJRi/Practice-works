#learn more python 3 the hardway ex4 practice

import sys
import os
print('Ohjelman nimi: ', sys.argv[0])
print('Ohjelman parametrit:', str(sys.argv))

parametrit = sys.argv
print(parametrit)
if '-h' or '--help' in parametrit:
    print('''Apuja tähän ohjelmaan:
    -h tai --help parametri tuo tämän tekstin esille.
    -d parametri kertoo nykyisen työskentely kansion
    -kopio parametri kopioi kopio.py:n alikansioon kopio-kansio ja tulostaa
    sen kansion sisällön. ''')
if '-d' in parametrit:
    print('Nykyinen työskentely kansio on:')
    os.system('pwd')
if '-kopioi' in parametrit:
    os.system('mkdir kopio-kansio')
    os.system('cp kopio.py kopio-kansio')
    os.system('ls kopio-kansio')
