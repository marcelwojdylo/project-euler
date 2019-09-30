import time
start = time.time()
import datetime
from sympy import isprime
from tqdm import tqdm

problemNumber = 41

scratchpad = open("./problem"+str(problemNumber)+"_scratchpad", "a+")

def pad (string):
    scratchpad.write(string+"\n")

def isNumberPandigital(number):
    number = str(number)
    numberOfDigits = len(number)
    # pad("Checking if "+number+" is "+str(numberOfDigits)+"-digit pandigital")
    
    digits = '123456789'[0:len(number)]
    for digit in digits:
        if number.count(digit) != 1:
            # pad("\tFailed")
            return False
    # pad("\tPassed")
    return True

def findPandigitalPrimes(lowerSearchLimit, upperSearchLimit):
    pps = []
    
    pad("\n\nLooking for pandigital prime numbers between "+str(lowerSearchLimit)+" and "+str(upperSearchLimit))
    for number in tqdm(range(lowerSearchLimit, upperSearchLimit, 2)):
        if isNumberPandigital(number) and number%3 != 0 and number%5!=0 and isprime(number):
            pps.append(number)
            pad("\tFound: "+str(number))
    if len(pps) > 0:
        pad("Found "+str(len(pps))+" pandigital primes")
        pad("Largest n-digit pandigital prime is "+str(max(pps)))
    else:
        pad("Found no n-digit pandigital primes in this range")
    return pps


##########################################

def run () :
    global problemNumber
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    # findPandigitalPrimes(1, 7412654)
    # findPandigitalPrimes(7412654, 10000000)
    # findPandigitalPrimes(10000000, 100000000)
    # findPandigitalPrimes(100000000, 1000000000)
    
    bottomLimit = 1
    topLimit = 5000000
    while topLimit < 1000000000:
        findPandigitalPrimes(bottomLimit, topLimit)
        bottomLimit += 5000000
        topLimit += 5000000
        print(bottomLimit, topLimit)

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()