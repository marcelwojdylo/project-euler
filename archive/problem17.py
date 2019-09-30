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

WORDS = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100: "hundred",
}

def pad (string):
    scratchpad.write(string+"\n")

def getNumberOfLetters(number):
    # pad("Getting number of letters in English word for "+str(number))
    if number < 20:
        word = WORDS[number]
    elif number < 100:
        decade = int(number/10)
        word = WORDS[decade*10]+" "+WORDS[number%(decade*10)]
    elif number < 1000:
        centade = int(number/100)
        decade = int((number-100*centade)/10)
        if number % 100 == 0:
            centade = int(number/100)
            word = (
                WORDS[centade]+" "+
                WORDS[100]
            )
        elif decade == 0:
            word = (
                WORDS[centade]+" "+
                WORDS[100]+" and "+
                WORDS[(number%100)]
            )
        elif decade == 1:
            word = (
                WORDS[centade]+" "+
                WORDS[100]+" and "+
                WORDS[number-centade*100]
            )
        else: 
            word = (
                WORDS[centade]+" "+
                WORDS[100]+" and "+
                WORDS[decade*10]+" "+
                WORDS[(number-100*centade)%(10)]
            )
    elif number == 1000:
        word = "one thousand"
    pad(word)
    letters = len(word.replace(" ", ""))
    # pad("\t\""+word+"\" has "+str(letters)+" letters")
    return letters

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    )

    pad("Looking for the sum of numbers of letters\n"+
        "in English expressions for numbers between\n"+
        "1 and 1000.")
    sum_ = 0
    for x in range(1,1001):
        sum_+=getNumberOfLetters(x)
    pad("\t"+str(sum_))
    finish = time.time()
    pad("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nThis took "+str(finish - start)+" s")

run()