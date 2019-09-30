import time
import datetime
from tqdm import tqdm

problemNumber = 39

scratchpad = open("./problem"+str(problemNumber)+"_scratchpad", "w+")

def pad (string):
    scratchpad.write(string+"\n")

def getA (b, p):
    # pad("With perimeter p = "+str(p)+" and side b = "+str(b))
    p = float(p)
    a = p/2*((p-2*b)/((p-b)))
    # pad("a = "+str(a))
    return a

def getIntegerSolutions (p):
    integerSolutions = []
    # pad("Looking for integer solutions for p = "+str(p))
    for b in range (1, p/2):
        a = getA(b, p)
        # pad("\tFor b = "+str(b)+", a = "+str(a))
        if a % 1.0 == 0:
            # pad("\ta is an integer")
            solution = tuple(sorted((a, b)))
            if solution not in integerSolutions:
                integerSolutions.append(solution)
    # pad("Found "+str(len(integerSolutions))+" integer solutions for a:\n"+str(integerSolutions))
    return integerSolutions

def findBestPInRange(searchRange):
    pad("Looking for perimeter p with most integer solutions in range "+str(searchRange))
    bestP = 0
    mostSolutions = 0
    for p in range (2,searchRange,2):
        solutions = getIntegerSolutions(p)
        if len(solutions) > mostSolutions:
            mostSolutions = len(solutions)
            bestP = p
    pad("There are "+str(mostSolutions)+" solutions for perimeter p = "+str(bestP)+"\nThis is more than for any other perimeter value in range")
    return bestP

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    findBestPInRange(1001)

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()