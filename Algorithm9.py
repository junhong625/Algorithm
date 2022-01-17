result = 0
for a in range(333):
    for b in range(a, 666):
        for c in range(b,997):
            if a + b + c == 1000:
                if a < b < c:
                    if a**2 + b**2 == c**2:
                        result = a*b*c
                        break

print(result)
