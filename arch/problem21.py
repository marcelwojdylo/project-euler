#!/usr/bin/env python3

def sumOfDivisors(number):
    sum = 0
    for n in range (1,number):
        if number % n == 0:
            # print(n)
            sum += n
    return sum

def sumOfDivisors2(number):
    

print(sumOfDivisors(220))

def areAmicable(a,b):
    if sumOfDivisors(a) == b and sumOfDivisors(b) == a:
        return True
    return False

print(areAmicable(220,284))

sum = 0

for n in range (1,10000):
    for m in range(1,10000):
        if n%2==0 and m%2!=0:
            continue
        if n%2!=0 and m%2==0:
            continue

        print("Checking "+str(n)+" and "+str(m))
        if areAmicable(m,n) and m != n:
            print(str(m)+" and "+str(n)+" are amicable, adding "+str(m)+" to sum.")
            sum+=m
print(sum)