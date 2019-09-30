from math import gcd

def  φ(n):
    return sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def willReciprocalTerminate (denominator):
    primefacs = prime_factors(denominator)
    for primefac in primefacs:
        if primefac not in (2,5):
            return False
    return True


def ManualDivision(Dividend, Divisor, acQPrecision, BreakOnRepetitive):

    Repetitive = False
    RepetitiveIndex = 0
    bcQComplete = False
    acQComplete = False
    bcQ = ''   #before comma Quotient
    acQ = ''   #after comma Quotient
    history = []
    a = 0
    b = 0
    RepetendLength = 0

    while (not bcQComplete or not acQComplete):
        if not bcQComplete:
            for digit in map(int, str(Dividend)):
                a = int(str(a) + str(digit))
                if a in history:
                    if not Repetitive:
                        Repetitive = True
                        RepetitiveIndex = len(history) - len(bcQ)
                    if BreakOnRepetitive:
                        break
                else:
                    history.append(a)
                if a < Divisor:           
                    b = 0
                    bcQ += '0'
                else:
                    pQ = 0
                    result = a - Divisor
                    while result >= 1:
                        pQ += 1
                        result -= Divisor
                    b = pQ * Divisor
                    bcQ += str(pQ) 
                a -= b
            bcQComplete = True

        if not acQComplete:
            acQPrecision -= 1
            if acQPrecision <= 0:
                acQComplete = True
            a = int(str(a) + str('0'))
            # print(str(a))

            if a in history:
                if not Repetitive:
                    Repetitive = True
                    RepetitiveIndex = len(history)
                    RepetendLength = RepetitiveIndex - history.index(a)
                if BreakOnRepetitive:
                    break
            else:
                history.append(a)

            # print(history)



            if a < Divisor:
                b = 0
                acQ += '0'

            else:
                pQ = 0
                result = a - Divisor
                while result >= 1:
                    pQ += 1
                    result -= Divisor
                b = pQ * Divisor
                acQ += str(pQ) 
            a-=b
            # print(str(a))
    return RepetendLength
    # return str(Dividend)+"/"+str(Divisor)+' = {0}.{1} \nRepetitive: {2} from position {3} acQ \nHistory:{4} \nRepetend length = {5}'.format(bcQ, acQ, Repetitive, RepetitiveIndex, history, RepetendLength)


n_with_longest_repetend = 0
longest_repetend = 0
for n in range (1000):
    if not willReciprocalTerminate(n):
        print(n)
        print (ManualDivision(1,n,n,False))
        repetend = ManualDivision(1,n,n,False)
        if longest_repetend < repetend:
            longest_repetend = repetend
            n_with_longest_repetend = n

print(longest_repetend, n_with_longest_repetend)





def acQ(Dividend, Divisor, acQPrecision, BreakOnRepetitive):

    Repetitive = False
    RepetitiveIndex = 0
    bcQComplete = False
    acQComplete = False
    bcQ = ''   #before comma Quotient
    acQ = ''   #after comma Quotient
    repetend = ''
    history = []
    a = 0
    b = 0

    while (not bcQComplete or not acQComplete):
        if not bcQComplete:
            for digit in map(int, str(Dividend)):
                a = int(str(a) + str(digit))
                if a in history:
                    if not Repetitive:
                        Repetitive = True
                        RepetitiveIndex = len(history) - len(bcQ)
                    if BreakOnRepetitive:
                        break
                else:
                    history.append(a)
                if a < Divisor:           
                    b = 0
                    bcQ += '0'
                else:
                    pQ = 0
                    result = a - Divisor
                    while result >= 1:
                        pQ += 1
                        result -= Divisor
                    b = pQ * Divisor
                    bcQ += str(pQ) 
                a -= b
            bcQComplete = True

        if not acQComplete:
            acQPrecision -= 1
            if acQPrecision <= 0:
                acQComplete = True
            a = int(str(a) + str('0'))
            if a in history:

                if not Repetitive:
                    Repetitive = True
                    RepetitiveIndex = len(history) - len(bcQ)
                if BreakOnRepetitive:
                    break
            else:
                history.append(a)
            if a < Divisor:
                b = 0
                acQ += '0'
                repetend += '0  Q1'
            else:
                pQ = 0
                result = a - Divisor
                while result >= 1:
                    pQ += 1
                    result -= Divisor
                b = pQ * Divisor
                acQ += str(pQ) 
                if Repetitive:
                    repetend += str(pQ)

            a-=b
    
    
    # results = ['{0}.{1}'.format(bcQ,acQ),RepetitiveIndex, repetend]
    return acQ

























# def getFunky(element):
#     return element[3]

# def repetend_length_in_acQ(acQ, divisor):
#     largest_funky = 0
#     repeated_substrings = []
#     for x in range (0, len(acQ)-divisor):
#         for y in range (x+1, x+divisor):
#             substring = acQ[x:y]
#             length = len(substring)
#             repeats = number_of_repeats(substring, acQ)
#             index = x
#             distance_from_end = len(acQ) - index
#             funky = repeats * (len(acQ) - index) * length
#             repeated_substrings.append((substring, repeats, distance_from_end, funky))
#             if (funky > largest_funky):
#                 largest_funky = funky
#                 most_repeated_substring = (substring, repeats, distance_from_end, funky)
#     print(acQ)
#     # print(repeated_substrings)
#     print(sorted(repeated_substrings,key=getFunky))
#     print(most_repeated_substring)
#     return len(most_repeated_substring[0])


# def number_of_repeats(substring, string):
#     repeats = 0
#     for x in range (0, len(string)):
#         if string[x:x+len(substring)] == substring:
#             repeats += 1
#     return repeats

# repetend_length_in_acQ('0765656596565659656565965656', 8)







# def search (range_of_search) :
#     n_with_highest_repetend_length = 2
#     highest_repetend_length = 0
#     for n in range (2, range_of_search):
#         if not willDecimalTerminate(n):
#             print("n = "+str(n))
#             after_comma_quotient = acQ(1, n, 10*n, False)
#             print("acQ = "+after_comma_quotient)
#             repetend_length = repetend_length_in_acQ(after_comma_quotient, n)
#             print("repetend length = "+str(repetend_length))
#             if repetend_length > highest_repetend_length:
#                 highest_repetend_length = repetend_length
#                 n_with_highest_repetend_length = n
#     print ("n with highest repetend is "+str(n_with_highest_repetend_length)+", its repetend length is "+str(highest_repetend_length))
#     return n_with_highest_repetend_length

# # search(10)

















































# def pattern(string):
#     for x in range(1,len(string)):
#         substring = string[:x]

#         if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
#             # print(substring)
#             return substring

#     return "fuck you"



# search (10)



# def repetendString (divisor):
#     div_results = ManualDivision(1,divisor,1000,False)
#     return div_results[2]


# n_with_highest_repetend = 2
# for n in range (300):
#     if not willDecimalTerminate(n):    
#         print("n: "+str(n))
#         print("1/n: "+ManualDivision(1,n,20,False)[0])
#         print("string with repetend: "+repetendString(n))
#         repetend = pattern(repetendString(n))
#         longest_repetend = pattern(repetendString(n_with_highest_repetend))
#         if len(str(repetend)) > len(str(longest_repetend)):
#             n_with_highest_repetend = n
#         print(repetend)

# print(n_with_highest_repetend)
# print(longest_repetend)


# Quotient = ManualDivision(91,256,100,False) #Dividend = 91, Divisor = 256, precision= 100, breakonrepetitive=False
# print(Quotient)

# import math


# def remove_beginning(string, beginning, remainder=""):
#     beginning = str(beginning)
#     string = str(string)
#     print(string)
#     if (remainder != ""):
#         beginning = str(remove_beginning(beginning,remainder))
#     # print("Remove was called!")
#     if len(string) == len(beginning):
#         return 0
#     string = string[len(beginning):]
#     return string

# def get_next_subdividend (left_under_division_sign, divisor, remainder=0) :
#     l = 0
#     m = 1
#     while True:
#         subdividend = float(str(int(math.floor(remainder)))+left_under_division_sign[l:m])    
#         if subdividend > divisor:
#             return subdividend
#         else:
#             m+=1

        
# def long_division(dividend, divisor):
#     quotient = ""
#     left_under_division_sign = str(dividend)
#     subdividend = get_next_subdividend(left_under_division_sign, divisor)
#     remainder = ""
#     print("First subdividend is: "+str(subdividend))
#     while True:
#         subquotient = int(math.floor(subdividend/divisor))

#         print("Got subquotient of "+str(subquotient))
#         quotient = quotient + str(subquotient)
#         print(quotient)
#         print("Left under division sign "+left_under_division_sign)

#         if left_under_division_sign == 0:
#             break
#         left_under_division_sign = remove_beginning(left_under_division_sign, subdividend, remainder)
#         print("Left under division sign "+left_under_division_sign)
#         remainder = subdividend  % divisor

#         if(len(left_under_division_sign)!=1):
#             subdividend = get_next_subdividend(left_under_division_sign, divisor, remainder)
#         else:
#             subdividend = float(left_under_division_sign)
        
#         print("Got remainder of "+str(remainder))
#         print("Left under division sign "+left_under_division_sign)

#         print("Subdividend "+str(subdividend))
#         print("-------")
#     print("-------------------")
#     return float(quotient)

# print(long_division(4536.0,216.0))


    
    







# def getReptendOfFraction (denominator, numerator=1):
#     reptend = 0
#     return reptend



# print(1/61.0)
# print(willDecimalTerminate(2))
# print(willDecimalTerminate(3))
# print(willDecimalTerminate(5))
# print(willDecimalTerminate(6))
# print(willDecimalTerminate(7))
# print(willDecimalTerminate(8))
# print(willDecimalTerminate(9))