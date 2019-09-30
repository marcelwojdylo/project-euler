#!/usr/bin/env python3

import time
import datetime
from tqdm import tqdm
import primefac

filename = __file__.replace(".py", "")
problemNumber = filename.replace("problem", "")

scratchpad = open("./"+filename+"_scratchpad.euler", "a+")

TEN_THOUSAND = 10000
ONE_HUNDRED_THOUSAND = 100000
ONE_MILION = 1000000
ONE_HUNDRED_MILLION = 100000000
ONE_BILLION = 1000000000

def pad (string):
    scratchpad.write(string+"\n")

def hasExDistinctPrimeFactors(number, x):
    # pad("Looking for prime factors of "+str(number))
    primeFactors = primefac.factorint(number).keys()
    if len(primeFactors) >= x:
        # pad(str(number)+" has "+str(len(primeFactors))+">="+str(x)+" prime factors")
        # pad(str(primeFactors))
        return True
    # pad(str(number)+" does not have "+str(x)+" distinct prime factors")
    return False

def getEnConsecutiveNumbers(rootNumber, n):
    return [x for x in range (rootNumber, rootNumber+n)]

def isSequenceEnMagical(sequence):
    n = len(sequence)
    # pad("\tChecking if sequence "+str(sequence)+" of length "+str(n)+" is n-magical")
    for number in sequence:
        if not hasExDistinctPrimeFactors(number, n):
            # pad("\t\t"+str(number)+" does not have "+str(n)+" distinct prime factors.\n\t\tSequence is not magical.")
            return False
    # pad("\t\t"+str(sequence)+" is an n-magical sequence!")
    return True

# n-magical sequence = n consecutive numbers each of which has n distinct prime factors
def findEnMagicalSequencesInRange(range_, n):
    pad("Looking for "+str(n)+"-magical sequences in range "+str(range_))
    magicalSequences = []
    for integer in tqdm(range(1,range_-n)):
        sequence = getEnConsecutiveNumbers(integer, n)
        if isSequenceEnMagical(sequence):
            magicalSequences.append(sequence)
    pad("Found "+str(len(magicalSequences))+" "+str(n)+"-magical sequences")
    if len(magicalSequences) > 0 :
        pad(str(magicalSequences))
    return magicalSequences


##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    )

    findEnMagicalSequencesInRange(10*ONE_MILION, 7)

    finish = time.time()
    pad("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nThis took "+str(finish - start)+" s")

run()