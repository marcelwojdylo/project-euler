import datetime

scratchpad = open("problem33_scratchpad", "a+")
results = open("problem33_results", "w+")


def checkFraction(numerator, denominator):
    numerator = str(numerator)
    denominator = str(denominator)
    for digit in range (1,10):
        digit = str(digit)
        combinations = [(numerator+digit,denominator+digit),(numerator+digit, digit+denominator), (digit+numerator, digit+denominator), (digit+numerator, denominator+digit)]
        for combination in combinations:
            if int(combination[0])/float(combination[1])==int(numerator)/float(denominator):
                results.write(str(datetime.datetime.now())+"\n")
                results.write("Fraction found:\n"
                +numerator+" / "+denominator+" = "+str(int(numerator)/float(denominator))+"\n"
                +combination[0]+" / "+combination[1]+" = "+ str(int(combination[0])/float(combination[1]))+"\n")
                # print(results.read)
                return True
    return False
# checkFraction(4, 8)
# checkFraction(2,8)
# checkFraction(1,3)
productOfNumerators = 1
productOfDenominators = 1
for numerator in range (1,10):
    for denominator in range (2,10):
        if numerator/denominator<1:
            if checkFraction(numerator, denominator):
                productOfNumerators = productOfNumerators * numerator
                productOfDenominators = productOfDenominators * denominator
print(productOfNumerators)
print(productOfDenominators)

