#!/usr/bin/env python3

import time
import datetime
from tqdm import tqdm
from sympy import isprime
from itertools import permutations, combinations

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

def areInterpermutable(number1, number2, number3):
    # pad("Are "+str(number3)+" and "+str(number2)+" permutations of "+str(number1)+"?")
    permutations_ = list(('').join(tuple) for tuple in permutations(str(number1)))
    # pad(str(permutations_))
    if str(number2) in permutations_ and str(number3) in permutations_:
        # pad("\tPass")
        return True
    # pad("\tFail")
    return False

def areInterpermutablePrimes(number1, number2, number3):
    # pad("Are "+str(number1)+", "+str(number2)+", "+str(number3)+" interpermutable primes?")
    if (not isprime(number1) 
        or not isprime(number2) 
        or not isprime(number3)
        or not areInterpermutable(number1, number2, number3)):
        # pad("\tFail")
        return False
    # pad("\tPass")
    return True

def getFourDigitPrimes():
    primes = []
    # pad("Looking for four-digit primes:")
    for number in range(1000, 10000):
        if isprime(number):
            primes.append(number)
    # pad(str(primes))
    return primes


def getCombinations(numbers, length):
    # pad("Getting "+str(length)+"-element combinations of four-digit primes\n["+
    #    str(numbers[1])+", "+str(numbers[2])+" ... "+str(numbers[len(numbers)-1:len(numbers):][0])+"]")
    combos = list(combinations(numbers, length))
    # pad("Found "+str(len(combos))+" combos:"+str(combos[0:1][0])+" etc.")
    return combos

def isArithmetic(sequence):
    # pad("Checking if "+str(sequence)+" is arithmetic")
    # pad("\tSorting sequence:")
    sequence = sorted(sequence)
    # pad("\t"+str(sequence))
    if (sequence[2]-sequence[1]==sequence[1]-sequence[0]):
        # pad("\tPass")
        return True
    # pad("\tFail")
    return False

def findInterpermutableArithmeticSequences():
    combosOfFourDigitPrimes = getCombinations(getFourDigitPrimes(), 3)
    pad("Looking for 3-element interpermutable arithmetic series of four-digit primes")
    sequences = []
    for combo in tqdm(combosOfFourDigitPrimes):
        if isArithmetic(combo) and areInterpermutable(combo[0],combo[1],combo[2]):
            pad("\tCombination found: "+str(combo[0])+", "+str(combo[1])+", "+str(combo[2]))
            sequences.append(combo)
    pad("\tFound "+str(len(sequences))+" out of 2:\n"+
        "\t"+str(sequences)
    )
    return sequences

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    )

    findInterpermutableArithmeticSequences()


    finish = time.time()
    pad("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nThis took "+str(finish - start)+" s")

run()