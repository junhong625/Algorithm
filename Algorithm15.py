import numpy as np

square = np.ones((21, 21))
for num in range(1, 21):
    for num2 in range(1, 21):
        square[num][num2] = square[num-1][num2] + square[num][num2-1]

print(int(square[-1][-1]))

