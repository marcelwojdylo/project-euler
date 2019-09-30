#!/usr/bin/env python3

import time
import datetime
from tqdm import tqdm
from sympy import isprime

filename = __file__.replace(".py", "")
problemNumber = filename.replace("problem", "")

scratchpad = open("./"+filename+"_scratchpad.euler", "a+")

TEN_THOUSAND = 10000
ONE_HUNDRED_THOUSAND = 100000
ONE_MILION = 1000000
ONE_HUNDRED_MILLION = 100000000
ONE_BILLION = 1000000000

PRIME_CACHE_RANGE = 10000

def pad (string):
    scratchpad.write(string+"\n")

def getPrimesInRange(range_):
    primes = []
    # pad("Finding primes in range "+str(range_))
    for number in tqdm(range(1, range_), desc="primes in range "+str(range_)):
        if isprime(number):
            primes.append(number)
    # pad(str(primes))
    return primes

def getConsecutivePrimeSum(primes, startingPrimeN, numberOfTerms):
    # pad("Getting sum of consecutive primes \n"+
    #     "for n = "+str(startingPrimeN)+" through "+str(startingPrimeN+numberOfTerms-1)+"\n"+
    #     "("+str(numberOfTerms)+" terms)")
    sum_ = 0
    n = startingPrimeN
    for i in range(numberOfTerms):
        sum_+=primes[n-1]
        # pad("\t"+str(primes[n-1]))
        n += 1
    # pad("\t="+str(sum_))
    return sum_    

def findMagicalPrimesInRange(range_):
    primes = getPrimesInRange(PRIME_CACHE_RANGE)
    pad("Looking for primes under "+str(range_)+" which\n"+
        "are a sum of consecutive primes")
    sumsWhichArePrime = []
    for startingN in range(1, len(primes)):
        for numberOfTerms in range(2, len(primes)-startingN):
            sum_ = getConsecutivePrimeSum(primes,startingN,numberOfTerms)
            if sum_ >= range_: break
            elif isprime(sum_):
                sumsWhichArePrime.append((startingN, numberOfTerms, sum_))
    sumsWhichArePrime = sorted(sumsWhichArePrime, key=lambda x: x[1])
    pad(str(sumsWhichArePrime))
    return sumsWhichArePrime

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    )

    findMagicalPrimesInRange(ONE_MILION)

    finish = time.time()
    pad("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nThis took "+str(finish - start)+" s")

run()