import itertools as it

print("".join(str(n) for n in list(it.permutations(range(10), 10))[999999]))