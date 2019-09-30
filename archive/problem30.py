import math

def sumOfPowersOfDigits(number, exponent):
    string = str(number)
    sum = 0
    for digit in string:
        sum += math.pow(float(digit),exponent)
    return sum

def meetsConditions(number, exponent):
    afterTransform = sumOfPowersOfDigits(number, exponent)
    if afterTransform == number:
        print("Found "+str(number))
        return True
    # else:
        # print(str(number)+" does not meet conditions with sum of "+str(afterTransform))
    return False

number = 2
sum = 0
while number<1000000:
    if meetsConditions(number, 5):
        sum += number
    number += 1

print(sum)