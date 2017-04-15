'''
Python script for generating a random passphrase based on the diceware list. 
Usage:
    - Run the script with no arguments to get a random 8 word phrase
    - Pass the --numwords or -n argument to change the length of your passphrase

e.g. 
    python diceware-generator.py -n 4
'''
from __future__ import print_function
import requests
import numpy as np
import argparse

def diceroll(numdice=5):
    return [np.random.randint(1,6) for i in range(numdice)]

def getword(worddict):
    roll = diceroll()
    roll = int(''.join([str(v) for v in roll]))
    word = worddict[roll]
    return word

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-n','--numwords', help='Number of Words to Generate', 
                        default=8, required=False)
    args = parser.parse_args()
    passphrase_length = int(args.numwords)

    r = requests.get('http://world.std.com/~reinhold/diceware.wordlist.asc')
    content = r.content.decode('utf-8').split('\n')[2:-16]
    words = [v.split('\t') for v in content]
    worddict = {int(v[0]):v[1] for v in words}

    passphrase = [getword(worddict) for i in range(passphrase_length)]
    print(" ".join(passphrase))
