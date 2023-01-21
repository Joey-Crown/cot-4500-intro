import numpy as np

matrix = np.zeros((3, 3), np.int32)

num_row = matrix.shape[0]
num_col = matrix.shape[1]

for i in range(num_row):
    for j in range(num_col):
        if i == j:
            matrix[i, j] = 1
        print(matrix[i, j], end=" ")
    print()

print()

for i in range(num_row):
    for j in range(num_col):
        if i != j:
            matrix[i, j] += 3
        print(matrix[i, j], end=" ")
    print()

print()

for i in range(num_row):
    for j in range(num_col - 1):
        print(matrix[i, j], end=" ")
    print()

