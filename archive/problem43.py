import time
import datetime
from tqdm import tqdm
from itertools import permutations

problemNumber = 43

scratchpad = open("./problem"+str(problemNumber)+"_scratchpad", "a+")

def pad (string):
    scratchpad.write(string+"\n")

def isZeroThroughNinePandigital(number):
    number = str(number)
    digits = '0123456789'
    for digit in digits:
        if number.count(digit) != 1:
            return False
    return True

def getPossibleZeroThroughNinePandigitals():
    possiblePermutations = [''.join(permutation) for permutation in permutations("0123456789")]
    validNumbers = []
    for permutation in possiblePermutations:
        if permutation[0] != '0':
            validNumbers.append(int(permutation))
    return validNumbers

def hasInterestingProperty(number):
    number = str(number)
    # pad("Checking if "+number+" has the rather interesting sub-string divisibility property")
    if (
        int(number[1:4:]) % 2 != 0 or
        int(number[2:5:]) % 3 != 0 or
        int(number[3:6:]) % 5 != 0 or
        int(number[4:7:]) % 7 != 0 or
        int(number[5:8:]) % 11 != 0 or
        int(number[6:9:]) % 13 != 0 or
        int(number[7:10:]) % 17 != 0

    ) : 
        # pad("\tFailed")
        return False
    # pad("\tPassed")
    return True

def findInterestingNumbers() :
    interestingNumbers = []
    candidates = getPossibleZeroThroughNinePandigitals()
    pad("Looking for numbers which have the rather interesting sub-string divisibility property")
    for number in tqdm(candidates):
        if hasInterestingProperty(number):
            pad(str(number)+" was found")
            interestingNumbers.append(number)
    pad("Found "+str(len(interestingNumbers))+" such numbers:")
    for number in interestingNumbers:
        pad(str(number))
    pad("Their sum is "+str(sum(interestingNumbers)))

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    findInterestingNumbers()

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()