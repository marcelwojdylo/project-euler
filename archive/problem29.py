import math

distinctPowers = []
for a in range(2, 101):
    for b in range(2, 101):
        power = math.pow(a,b)
        if power not in distinctPowers:
            distinctPowers.append(power)
for b in range(2,101):
    for a in range (2,101):
        power = math.pow(b,a)
        if power not in distinctPowers:
            distinctPowers.append(power)
print(distinctPowers)
print(len(distinctPowers))