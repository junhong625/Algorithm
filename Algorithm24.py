#0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 1,000,000번째 사전식 순열은?

import itertools as it

print("".join(str(n) for n in list(it.permutations(range(10), 10))[999999]))