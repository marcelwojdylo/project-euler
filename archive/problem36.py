import time
import datetime
from tqdm import tqdm

scratchpad = open("./problem36_scratchpad", "a+")

def pad (string):
    scratchpad.write(string+"\n")

def getBinaryString(number):
    # pad("Converting "+str(number)+" to binary: ")
    number = "{0:b}".format(int(number))
    # pad("Result: "+number)
    return number

def reverse(string):
    rev = ""
    for char in reversed(string):
        rev = rev + char
    return rev

def isPalindrome(string):
    # pad("Checking if "+string+" is a palindrome")
    rev = reverse(string)
    # pad("\tReversed string is: \""+rev+"\"")
    if string == rev:
        # pad(string+" is a palindrome")
        return True
    # pad(string+" is not a palindrome")
    return False

def isPalindromeInBaseTwoAndTen(number):
    # pad("Checking if "+str(number)+" is a palindrome in base two and ten")
    if isPalindrome(str(number)) and isPalindrome(str(getBinaryString(number))):
        # pad("\tIt is")
        return True
    # pad("\tIt isn't")
    return False

def findPalsInRange(searchRange):
    pad("Looking for base two and ten palindromes under "+str(searchRange))
    pals = []
    for number in tqdm(range (searchRange)):
        if isPalindromeInBaseTwoAndTen(number):
            pad("\tFound: "+str(number)+" (binary: "+getBinaryString(number)+")")
            pals.append(number)
    pad("Found "+str(len(pals))+" numbers")
    return pals

##########################################

def run () :
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    pals = findPalsInRange(1000000)
    pad("The sum of numbers under 1 000 000 which are palindromic in base 10 and 2 is "+str(sum(pals)))
    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()