coins = [1,2,5,10,20,50,100,200]
n = 200
ways = [0 for i in range(n+1)]
ways[0] = 1

for coin in coins:
    for index, value in enumerate(ways):
        if index >= coin:
            ways[index] += ways[index-coin]

print(ways)