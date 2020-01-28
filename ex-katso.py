#ex5 practice file to "Learn more python 3 the hardway"-book
#versio 2.0, with argparse
#Takes any number of files and prints them to screen


## TODO: Works only with one file !!!

import argparse

parser = argparse.ArgumentParser(description='Takes files and looks in to them and prints on the screen.')
parser.add_argument('-f', '--file', type=argparse.FileType('r'))
args = parser.parse_args()


f = args.file
while True:
    rivi = f.readline()
    print(rivi)
    if not rivi:
        break
