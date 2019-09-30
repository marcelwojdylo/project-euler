import util
isPrime = util.isPrime

def countResultingConsecutivePrimes (a, b):
    n = 0
    consecutivePrimesCount = 0
    encounteredNonPrime = False
    while not encounteredNonPrime:
        quadraticsResult = quadratics(a,b,n)
        if isPrime(quadraticsResult):
            consecutivePrimesCount += 1
            n += 1
        else:
            encounteredNonPrime = True
    return consecutivePrimesCount

def quadratics (a, b, n) :
    return n*n + a*n + b

limit = 1000
bestPair = (0,0)
bestCount = 0
for a in range (-limit, limit):
    for b in range (-limit-1, limit+1):
        count = countResultingConsecutivePrimes(a,b)
        if count > bestCount:
            bestCount = count
            bestPair = (a,b)
        print(str(a)+","+str(b)+":"+str(count))
print(str(bestPair)+" best with "+str(bestCount))

-61 971