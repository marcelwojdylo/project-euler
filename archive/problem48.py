#!/usr/bin/env python3

import time
import datetime
from tqdm import tqdm

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

def selfPower(number):
    return int(number**number)

def sumOfSeriesOfSelfPowers(n):
    pad("Computing the sum of natural numbers up to and including "+str(n)+", each raised to its own power")
    sum_ = 0
    for number in tqdm(range(1,n+1)):
        sum_+=selfPower(number)
    pad("...\nSum of all terms is "+str(sum_))
    return sum_

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    )

    sumOfSeriesOfSelfPowers(1000)

    finish = time.time()
    pad("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nThis took "+str(finish - start)+" s")

run()