import time
import math, datetime

start = time.time()
output = open("problem-32-output", "a+")
foundProducts = open("problem32-products", "w+")
numberOfProducts = 0

def isIdentityValid(multiplicand, multiplier, product):
    return True if multiplicand*multiplier==product else False

def isIdentityPandigital(multiplicand, multiplier, product):
    digitsOfIdentity = str(multiplicand)+str(multiplier)+str(product)
    for digit in '123456789':
        timesDigitInIdentity = digitsOfIdentity.count(digit)
        if timesDigitInIdentity != 1:
            return False
    return True

#util
def makeIdentityString(tuple):
    multiplicand = str(tuple[0])
    multiplier = str(tuple[1])
    product = str(tuple[2])
    return multiplicand+" * "+multiplier+" = "+product

# limiting conditions
def hasNineDigits(multiplicand, multiplier, product):
    numberOfDigits = len(str(multiplicand)) + len(str(multiplier)) + len(str(product))
    return True if numberOfDigits == 9 else False

def containsZero(number):
    return True if str(number).count("0") > 0 else False

def containZeros(multiplicand, multiplier, product):
    return True if containsZero(multiplicand) or containsZero(multiplier) or containsZero(product) else False

def areInRange(multiplicand, multiplier, product):
    multiplicandInRange = True if multiplicand >= 0 and multiplicand < 100 else False
    multiplierInRange = True if multiplier >= 100 and multiplier < 10000 else False
    productInRange =  True if product >= 1000 and product < 10000 else False
    return True if multiplicandInRange and multiplierInRange and productInRange else False


def checkProductCandidate (productCandidate):
    global numberOfProducts
    for multiplicandCandidate in range (1, int(math.ceil(math.sqrt(productCandidate)))):
        if not containsZero(multiplicandCandidate) and (productCandidate % multiplicandCandidate == 0):
            multiplierCandidate = productCandidate / multiplicandCandidate
            candidateTuple = (multiplicandCandidate, multiplierCandidate, productCandidate)
            print("\nChecking: "+makeIdentityString(candidateTuple))
            if isIdentityPandigital(multiplicandCandidate, multiplierCandidate, productCandidate):
                print("Checks out! "+makeIdentityString(candidateTuple)+" was found!")
                foundProducts.write(str(productCandidate)+"\n")
                output.write(str(candidateTuple)+"\r\n")
                numberOfProducts+=1

            else: 
                print("Nope")

# tuplesChecked = 0
for productCandidate in range (1111, 2000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (2111, 3000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (3111, 4000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (4111, 5000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (5111, 6000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (6111, 7000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (7111, 8000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (8111, 9000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
for productCandidate in range (9111, 10000):
    if not containsZero(productCandidate):
        checkProductCandidate(productCandidate)
                    
end = time.time()
# print("Checked "+str(tuplesChecked)+" tuples.")

dateTimeMessage = str(datetime.datetime.now())
print(dateTimeMessage)
output.write(dateTimeMessage+"\r\n")
endmessage = "This took "+str(end-start)+" s"
print(endmessage)
output.write(endmessage+"\r\n")
output.write("Found "+str(numberOfProducts)+" products")

foundProducts = open("problem32-products", "r")
uniqueProducts = []
for line in foundProducts.readlines(): 
    if uniqueProducts.count(int(line)) == 0:
        uniqueProducts.append(int(line))
output.write("\nUnique products: ("+str(len(uniqueProducts))+") "+str(uniqueProducts))
print(sum(uniqueProducts))

# tuple1 = (12,34,56789)
# print("\n"+makeIdentityString(tuple1))
# print(areInRange(tuple1[0], tuple1[1], tuple1[2]))
# print(containZeros(tuple1[0], tuple1[1], tuple1[2]))
# print(hasNineDigits(tuple1[0], tuple1[1], tuple1[2]))
# print(isIdentityValid(tuple1[0], tuple1[1], tuple1[2]))
# print(isIdentityPandigital(tuple1[0], tuple1[1], tuple1[2]))

# tuple2 = (10,10,100)
# print("\n"+makeIdentityString(tuple2))
# print(areInRange(tuple2[0], tuple2[1], tuple2[2]))
# print(containZeros(tuple2[0], tuple2[1], tuple2[2]))
# print(hasNineDigits(tuple2[0], tuple2[1], tuple2[2]))
# print(isIdentityValid(tuple2[0], tuple2[1], tuple2[2]))
# print(isIdentityPandigital(tuple2[0], tuple2[1], tuple2[2]))

# tuple3 = (39,186,7254)
# print("\n"+makeIdentityString(tuple3))
# print(areInRange(tuple3[0], tuple3[1], tuple3[2]))
# print(containZeros(tuple3[0], tuple3[1], tuple3[2]))
# print(isIdentityValid(tuple3[0], tuple3[1], tuple3[2]))
# print(hasNineDigits(tuple3[0], tuple3[1], tuple3[2]))
# print(isIdentityPandigital(tuple3[0], tuple3[1], tuple3[2]))