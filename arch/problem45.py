
import time
import datetime
from tqdm import tqdm
import math

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

def triangular(n): return (n*(n+1))/2

def pentagonal(n): return (3*n*n-n)/2

def hexagonal(n): return n*(2*n-1)

def isTriangular(number):
    n = (math.sqrt(8*number+1)-1)/2
    return True if n % 1 == 0 and n > 0 else False

def isPentagonal(number):
    n = (math.sqrt(24*number+1)+1)/6
    return True if n % 1 == 0 and n > 0 else False

def isHexagonal(number):
    n = (math.sqrt(8*number+1)+1)/4
    return True if n % 1 == 0 and n > 0 else False

def isMagical(n):
    # pad("For n = "+str(n)+", checking if nth triangular number is also pentagonal and hexagonal")
    tri = triangular(n)
    if isPentagonal(tri) and isHexagonal(tri):
        # pad("\t"+str(tri)+" is triangular, pentagonal and hexagonal")
        return True
    return False    

def findMagicalNsInRange(range_):
    magicalNs = []
    pad("Looking for magical ns in range "+str(range_))
    for n in tqdm(range(1, range_)):
        if isMagical(n):
            magicalNs.append(n)
            pad("\tFound magical number at n = "+str(n)+": "+str(triangular(n)))
    pad("\tFound "+str(len(magicalNs))+" ns that generate a magical number")
    if len(magicalNs) != 0: pad(str(magicalNs))
    return magicalNs

##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    findMagicalNsInRange(ONE_HUNDRED_MILLION)

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()