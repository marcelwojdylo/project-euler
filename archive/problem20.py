#!/usr/bin/env python3
import math

def factorial(n):
    product = 1
    for integer in range (1,n):
        product*=integer
    return product

print(factorial(10))

def digitSum(number):
    string = str(number)
    sum = 0
    for char in string :
        sum+= int(char)
    return sum

print(digitSum(2323))
print(digitSum(factorial(100)))