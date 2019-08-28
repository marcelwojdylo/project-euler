import time
import datetime
from tqdm import tqdm

problemNumber = 42

scratchpad = open("./problem"+str(problemNumber)+"_scratchpad", "a+")
wordsList = open("./problem42_words.txt", "r")

def pad (string):
    scratchpad.write(string+"\n")

def getCharacterValue(character):
    return ord(character)-64

def getWordValue(word):
    wordValue = 0
    # pad("Computing word value of "+word)
    for character in word:
        # pad("\tValue of "+character+" is "+str(getCharacterValue(character)))
        wordValue += getCharacterValue(character)
    # pad("Total value of "+word+" is "+str(wordValue))
    return wordValue

def getAllWordValues(words):
    values = []
    for word in words:
        values.append(getWordValue(word))
    return values

def findTriangularNumbersUnder(searchRange):
    triangularNumbers = [0]
    n = 1
    pad("Looking for triangular numbers under "+str(searchRange))
    while max(triangularNumbers) <= searchRange:
        triangularNumbers.append(makeNthTriangularNumber(n))
        pad("\tFound: "+str(makeNthTriangularNumber(n)))
        n+=1
    pad("Found "+str(len(triangularNumbers))+" triangular numbers in range")
    return triangularNumbers



def makeNthTriangularNumber(n):
    return int(0.5*n*(n+1))
##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    words = wordsList.read().replace('"','').split(",")
    values = getAllWordValues(words)
    triangularNumbers = findTriangularNumbersUnder(193)
    triangularWords = []
    pad("Checking for triangular numbers in values")
    for index in range (len(words)):
        if values[index] in triangularNumbers:
            triangularWords.append((words[index],values[index]))
    pad("Found "+str(len(triangularWords))+" triangular numbers in list of word values.")
    # pad(str(triangularWords))
    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()