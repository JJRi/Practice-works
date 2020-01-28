#ex5 practice file to "Learn more python 3 the hardway"-book
import sys
import os

params = sys.argv
laskuri = 0
for p in params:
    if p == sys.argv[0] and laskuri == 0:
        laskuri += 1
        continue
    else:
        print(p * 15)
        f = open(p, 'r')
        while True:
            rivi = f.readline()
            print(rivi)
            if not rivi:
                break
        f.close()
