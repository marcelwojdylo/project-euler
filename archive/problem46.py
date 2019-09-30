#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
from tqdm import tqdm
from sympy import isprime
import math
from itertools import product

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

def evaluatesTrue(oddComposite, prime, sqrt):
    return True if oddComposite == prime + 2 * (sqrt*sqrt) else False

def getPrimesInRange(range_):
    primes = []
    # pad("Looking for primes in range "+str(range_))
    for number in range(1, range_, 2):
        if isprime(number):
            primes.append(number)
    # pad("Found "+str(len(primes))+" primes.")
    # if len(primes) != 0 : pad(str(primes))
    return primes

def getPossibleSquareRoots(oddComposite):
    # pad("Looking for possible square roots given the odd composite "+str(oddComposite))
    possiblesqrts = [number for number in range(1, int(math.ceil(math.sqrt(oddComposite/2))))]
    # for sqrt in possiblesqrts:
        # pad("2 * "+str(sqrt)+" * "+str(sqrt)+" = "+str(2*sqrt*sqrt)+" < "+str(oddComposite)+"? "+str(2*sqrt*sqrt<oddComposite))
    # pad(str(possiblesqrts))
    return possiblesqrts

def isCounterexample(oddComposite):
    possiblePrimes = getPrimesInRange(oddComposite-1)
    possibleSqrts = getPossibleSquareRoots(oddComposite)
    combos = list(product(possiblePrimes, possibleSqrts))
    # pad("\nLooking for possible solutions for odd composite "+str(oddComposite))
    solutions = []
    for combo in combos:
        if evaluatesTrue(oddComposite, combo[0], combo[1]):
            solutions.append((combo[0], combo[1]))
    # pad("Found "+str(len(solutions))+" solutions")
    if len(solutions) == 0:
        return True
    else:
        # pad(str(solutions))
        return False

def lookForCounterexamplesInRange(range_):
    counterexamples = []
    pad("Looking for counterexamples to Goldbach's other theorem in range "+str(range_))
    for x in tqdm(range(1, range_, 2)):
        if not isprime(x) and isCounterexample(x):
            counterexamples.append(x)
    pad("Found "+str(len(counterexamples))+" counterexamples.")
    if len(counterexamples) != 0 : pad(str(counterexamples))
    return counterexamples

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    lookForCounterexamplesInRange(TEN_THOUSAND)


    finish = time.time()
    pad("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nThis took "+str(finish - start)+" s")

run()
