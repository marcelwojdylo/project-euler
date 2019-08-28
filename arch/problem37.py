import time
import datetime
from tqdm import tqdm
from sympy import isprime
import matplotlib.pyplot as plt 


scratchpad = open("./problem37_scratchpad", "a+")

def pad (string):
    scratchpad.write(string+"\n")

def truncateFromRight(string):
    truncated = string[:len(string)-1:] 
    # pad("Right-side truncating of "+string+" results in "+truncated)
    return truncated

def truncateFromLeft(string):
    truncated = string[1::] 
    # pad("Left-side truncating of "+string+" results in "+truncated)
    return truncated

def getConsecutiveLeftTruncations(string):
    # pad("Possible left-side truncations of \""+string+"\"  are:")
    truncations = []
    for characters in string:
        string = truncateFromLeft(string)
        if len(string)>0:
            truncations.append(string)
    # pad(str(truncations))
    return truncations

def getConsecutiveRightTruncations(string):
    # pad("Possible right-side truncations of \""+string+"\"  are:")
    truncations = []
    for characters in string:
        string = truncateFromRight(string)
        if len(string)>0:
            truncations.append(string)
    # pad(str(truncations))
    return truncations

def getPossibleTruncationResults(string):
    # pad("Possible left- and right-side truncations of \""+string+"\" are:")
    truncations = getConsecutiveLeftTruncations(string) + getConsecutiveRightTruncations(string)
    # pad("\t"+str(truncations))
    return truncations

def hasInterestingProperty(number):
    number = str(number)
    # pad("Checking if "+number+" has the interesting property")
    truncations = getPossibleTruncationResults(number)
    for truncation in truncations:
        if not isprime(int(truncation)):
            # pad(str(truncation)+" is not prime, "+number+" does not have the interesting property")
            return False
    pad("\tAll possible truncations of "+number+" are prime")
    return True
    
def findInterestingNumbersInRange(searchRange):
    interestingNumbers = []
    pad("Looking for interesting numbers in range "+str(searchRange))
    for number in tqdm(range(8, searchRange)):
        if isprime(number) and hasInterestingProperty(number):
            interestingNumbers.append(number)
    pad("Found "+str(len(interestingNumbers))+" interesting numbers"+"\n"+
        str(interestingNumbers)
    )
    return interestingNumbers
##########################################

def run () :
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    interestingNumbers = findInterestingNumbersInRange(739398)
    pad("The sum of all 11 numbers with the interesting property is: "+str(sum(interestingNumbers)))

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()