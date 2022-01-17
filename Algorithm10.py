result = 0
for a in range(2000001):
    count = 0
    for b in range(1, a+1):
        if a % b == 0:
            count += 1
        if count == 3:
            break
    if count == 2:
        result += a
        print('%s || %s'%(result, a))
print(result)
