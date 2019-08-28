numberOfSides = 4
n = 1
cycle = 1
interval = 1
sum = 1
maxSideLength = 1001
currentSideSize = 3

while currentSideSize <= maxSideLength:
    print("Cycle: "+str(cycle))
    for x in range(numberOfSides):
        for times in range (interval):
            n += 1
        n+= 1
        sum += n
        print("     Side "+str(x+1)+", adding "+str(n)+", sum is "+str(sum))
    print("Sum after cycle "+str(cycle)+" is "+str(sum)+"\n----")
    interval += 2
    cycle+=1
    currentSideSize = 2*cycle + 1
print(sum)