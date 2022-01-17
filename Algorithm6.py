result = 0
sum = 0
for i in range(1, 101):
    result += i**2
    sum += i
print(sum**2 - result)
