import time
import datetime
from tqdm import tqdm
import math

filename = __file__.replace(".py", "")
problemNumber = filename.replace("problem", "")

scratchpad = open("./"+filename+"_scratchpad.euler", "a+")


def pad (string):
    scratchpad.write(string+"\n")

def getEnthPentagonal(n):
    return (3*n*n-n)/2

def isPentagonal(number):
    n = (math.sqrt(24*number+1)+1)/6
    return True if n % 1 == 0 and n > 0 else False

def getPentagonals(n):
    pentagonals = []
    # pad("Generating the first "+str(n)+" pentagonals")
    for number in range (1,n+1):
        pent = getEnthPentagonal(number)
        pentagonals.append(pent)
        # pad("\t"+str(pent))
    # pad("Found "+str(len(pentagonals))+" pentagonals")
    return pentagonals

def getSumOfPentagonals(j, k):
    return getEnthPentagonal(j) + getEnthPentagonal(k)

def getDifferenceOfPentagonals(j,k):
    difference = getEnthPentagonal(k) - getEnthPentagonal(j)
    difference = int(math.sqrt(difference*difference))
    return difference

def isPairInteresting(j,k):
    # pad("Checking P"+str(j)+" and P"+str(k))
    sumOfPair = getSumOfPentagonals(j,k)
    differenceOfPair = getDifferenceOfPentagonals(j,k)
    # pad("\t"+str(getEnthPentagonal(j))+" + "+str(getEnthPentagonal(k))+" = "+str(sumOfPair))
    # pad("\t\tPentagonal? "+str(isPentagonal(sumOfPair)))
    # pad("\t"+str(getEnthPentagonal(k))+" - "+str(getEnthPentagonal(j))+" = "+str(differenceOfPair))
    # pad("\t\tPentagonal? "+str(isPentagonal(differenceOfPair)))
    if isPentagonal(sumOfPair) and isPentagonal(differenceOfPair):
        return True
    return False

def checkConsecutivePairs(searchLimit):
    # pad("Checking consecutive pairs of pentagonal numbers with max n = "+str(searchLimit))
    interestingPairs = []
    for number in tqdm(range(1, searchLimit)):
        if isPairInteresting(number, number+1):
            # pad("\tFound pair: "+str((number, number+1)))
            interestingPairs.append((number, number+1))
    # pad("Found "+str(len(interestingPairs))+" interesting pairs")
    pad(str(interestingPairs))
    return interestingPairs

def checkPairsApartBy(searchLimit, distance):
    # pad("Checking pairs of pentagonal numbers with max n = "+str(searchLimit)+" and difference nk-nj = "+str(distance))
    interestingPairs = []
    for number in tqdm(range(1, searchLimit)):
        if isPairInteresting(number, number+distance):
            pad("\tFound pair: "+str((number, number+distance)))
            interestingPairs.append((number, number+distance))
    # pad("Found "+str(len(interestingPairs))+" interesting pairs")
    if len(interestingPairs)>0: pad(str(interestingPairs))
    return interestingPairs

##########################################

def run () :
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    interestingPairs = []
    for x in tqdm(range (1,1000)):
        interestingPairs += checkPairsApartBy(1000000, x)
    pad("Found "+str(len(interestingPairs))+" interesting pairs")
    if len(interestingPairs)>0: pad(str(interestingPairs))

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()