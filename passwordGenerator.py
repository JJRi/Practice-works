import random

x = input('Aseta salasanan pituus, kiitos')
word_lenght = int(x)
nmbrs_how=int(input('Kuinka monta niistä on numeroa'))
count = word_lenght - nmbrs_how
new_word = ' '
while count != 0:
    new_word = new_word + random.choice('ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuyvwxz')
    count = count - 1
add_nmbrs = ''
while nmbrs_how != 0:
    x = random.randint(1,9)
    new_nmbr = str(x)
    add_nmbrs = add_nmbrs+new_nmbr
    nmbrs_how -= 1
new_word = new_word+add_nmbrs
print('Uusi salasani on: ' + new_word)
