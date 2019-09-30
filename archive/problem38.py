import time
import datetime
from tqdm import tqdm
import matplotlib.pyplot as plt 


scratchpad = open("./problem38_scratchpad", "a+")

def pad (string):
    scratchpad.write(string+"\n")

def multiplyBySequence(number=1, sequence=[1,2,3]):
    products = []
    # pad("Multiplying "+str(number)+" by each element of sequence "+str(sequence)+":")
    for integer in sequence:
        products.append(number * integer)
    # pad("\t"+str(products))
    return products

def concatenateNumbers(list):
    result = ""
    # pad("Concatenating numbers in sequence "+str(sequence)+":")
    for integer in list:
        result = result + str(integer)
    # pad("\t"+result)
    return int(result)

def getConsecutiveIntegersLessOrEqualTo(limit):
    integers = []
    # pad("Getting consecutive integers up to and including "+str(limit))
    for integer in range(1, limit+1):
        integers.append(integer)
    # pad("\t"+str(integers))
    return integers

def getConcatenatedProduct(number, sequence):
    # pad("Getting concatenated produt of "+str(number)+" and "+str(sequence))
    products = multiplyBySequence(number, sequence)
    concatenatedProduct = concatenateNumbers(products)
    # pad("\t"+str(concatenatedProduct))
    return concatenatedProduct
    
def isNumberPandigital(number):
    number = str(number)
    for digit in '123456789':
        if number.count(digit) != 1:
            return False
    return True

def findPandigitalConcatenatedProducts(number):
    products = []
    sequenceLimit = 2
    finished = False
    # pad("Looking for pandigital concatenated products of "+str(number))
    while not finished:
        sequence = getConsecutiveIntegersLessOrEqualTo(sequenceLimit)
        concatenatedProduct = getConcatenatedProduct(number, sequence)
        # pad("\tfor sequence "+str(sequence)+" product is "+str(concatenatedProduct))
        lengthOfProduct = len(str(concatenatedProduct))
        if lengthOfProduct == 9 and isNumberPandigital(concatenatedProduct):
            # pad("\t\tthis product is pandigital")
            products.append((concatenatedProduct, number, sequenceLimit))
        
        sequenceLimit = sequenceLimit + 1
        if lengthOfProduct > 9 :
            finished = True
    # pad("Found following pandigital products: "+str(products))
    return products

def findPCPsInRange(searchRange):
    pcps = []
    pad("Looking for PCPs in range "+str(searchRange)+"\n"+
        "(Pandigital Concatenated Product)"
    )
    for number in tqdm(range(1, searchRange)):
        products = findPandigitalConcatenatedProducts(number)
        if len(products) > 0:
            pcps = pcps + products
            # # pad("\tFound PCPs for number "+str(number)+":\n"+
            #     str(products))
    pad("Found following "+str(len(pcps))+" PCPs:\n"+str(pcps))
    return pcps

def makeGraph(maxRange):
    ranges = []
    numberOfPCPsInRanges = []
    for searchRange in tqdm(range(1, maxRange)):
        pcps = findPCPsInRange(searchRange)
        ranges.append(searchRange)
        numberOfPCPsInRanges.append(len(pcps))
    plt.plot(ranges,numberOfPCPsInRanges)
    plt.show()

def getHighestPCP(listOfPCPs):
    highestPCP = 0
    for pcp in listOfPCPs:
        if pcp[0] > highestPCP:
            highestPCP = pcp[0]
    pad("The highest PCP on the list is "+str(highestPCP))
    return highestPCP


##########################################

def run () :
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )
    
    pcps = findPCPsInRange(1000000)
    getHighestPCP(pcps)

    finish = time.time()
    pad("This took "+str(finish - start)+" s")
    
run()