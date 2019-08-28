import itertools
file = open("permutations.txt","r")
permutations = []
for line in file:
    permutations.append(str(line).replace("\n",""))
permutations = sorted(permutations)
print (permutations[1000000-1])


# tuple_to_permute = (["0","1","2","3","4","5","6","7","8","9"])
# permutations = list(itertools.permutations(["0","1","2","3","4","5","6","7","8","9"]))
# for permutation in permutations:
#     for digit in permutation:
#         file.write(str(digit))
#     file.write("\n")
# print("Finished!")
# for tuple in 