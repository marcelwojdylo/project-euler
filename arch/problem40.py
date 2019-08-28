
def clearFile () :
    champ = open("./champernone_word", "w+")
    champ.write("")
    champ.close()


def storeChampernoneWord(numberOfDigits):
    currentNumberOfDigits = 0
    numberToAdd = 1
    print("Generating Champernone word of "+str(numberOfDigits)+" digits")
    while currentNumberOfDigits < numberOfDigits:
        champ = open("./champernone_word", "a+")
        champ.write(str(numberToAdd))
        print("\tAdding "+str(numberToAdd)+" to file")
        numberToAdd += 1
        champ = open("./champernone_word","r")
        currentNumberOfDigits = len(champ.read())
        print("\t"+str(currentNumberOfDigits)+" digits in file")
        champ.close()

def getNthDigitOfChampernone(n):
    print("Getting nth digit of Champernone's word for n = "+str(n))
    champ = open("./champernone_word","r")
    champernoneWord = champ.read()
    print("\t"+champernoneWord[n-1])
    return int(champernoneWord[n-1])



def run () :
    firstDigit = getNthDigitOfChampernone(1)
    print(firstDigit)
    result = getNthDigitOfChampernone(1) * getNthDigitOfChampernone(10) * getNthDigitOfChampernone(100) * getNthDigitOfChampernone(1000) * getNthDigitOfChampernone(10000) * getNthDigitOfChampernone(100000) * getNthDigitOfChampernone(1000000)
    print(result)

run()