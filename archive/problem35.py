import time
from sympy import isprime
import datetime
from tqdm import tqdm

scratchpad = open("./problem35_scratchpad", "a+")

def pad (string):
    scratchpad.write(string+"\n")

def rotateByOne (string) :
    string = string + string[0]
    string = string[1::]
    return string

def getRotations(string) :
    rotations = []
    # pad("\tFor string: "+string)
    for digit in string:
        string = rotateByOne(string)
        # pad(
        #     "\t"+
        #     string
        # )
        rotations.append(string)
    return rotations

def isCircularPrime(prime):
    prime = str(prime)
    # pad("Checking if prime "+prime+" is circular")
    rotations = getRotations(prime)
    for rotation in rotations:
        if not isprime(int(rotation)):
            # pad(prime+" is not circular")
            return False
    # pad(prime+" is circular")
    return True

def findCircularPrimesInRange(searchRange):
    pad("Searching for primes in range "+str(searchRange))
    circularPrimes = []
    for number in tqdm(range(searchRange)):
        if isprime(number) and isCircularPrime(number):
            pad(str(number)+" is circular")
            circularPrimes.append(number)
    pad("--- search finished ---")
    pad(str(len(circularPrimes))+" circular primes found")
    return circularPrimes

##########################################

def run () :
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )
    findCircularPrimesInRange(1000000)
    finish = time.time()
    pad("This took "+str(finish - start)+" s")
run()