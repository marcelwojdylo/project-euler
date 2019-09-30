import math, time
import matplotlib.pyplot as plt 
from tqdm import tqdm

numbers = []
differencesNumberFactorial = []
def isCurious(number):
    global numbers
    global differencesNumberFactorial
    # numbers.append(number)
    number = str(number)
    sumOfFactorials = 0
    for digit in number:
        # print("digit: "+digit)
        # print("factorial: "+str(math.factorial(int(digit))))
        sumOfFactorials += math.factorial(int(digit))
        # print("sum of factorials: "+str(sumOfFactorials))
    # differencesNumberFactorial.append(int(number)-sumOfFactorials)
    return True if sumOfFactorials == int(number) else False
# print("Is 145 curious?")
# print(isCurious(145))

# print("Min factorial of one digit number: "+str(math.factorial(1)))
# print("Max factorial of one digit number: "+str(math.factorial(9)))

start = time.time()

curiousNumbers = []
for number in tqdm(range (3, 2050000), desc="Progress: "):
    if isCurious(number):
        curiousNumbers.append(number)


finish = time.time()
print(curiousNumbers)
print("Sum: "+str(sum(curiousNumbers)))
print("Execution time: " + str(finish-start))

zeros = [0 for x in range (len(numbers))]

# plt.plot(numbers, differencesNumberFactorial)
# plt.plot(numbers, zeros)
# plt.show()
