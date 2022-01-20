#두 과잉수의 합으로 나타낼 수 없는 모든 양의 정수의 합은?

def divisors(num):
    sum = 0
    for j in range(1, num):
        if i % j== 0:
            sum += j
    if sum > i:
        abundant.append(num)

abundant  = []
for i in range(1, 28124):
    divisors(i)

all_numbers = set(range(1,28124))

for abun1 in abundant:
    for abun2 in abundant:
        if abun1 + abun2 in all_numbers:
            all_numbers.remove(abun1 + abun2)

total = 0
for i in range(len(all_numbers)):
    total += list(all_numbers)[i]

print(total)