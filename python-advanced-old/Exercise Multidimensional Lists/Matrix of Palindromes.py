import string

matrix = list()

rows, cols = [int(x) for x in input().split()]

alpha = list(string.ascii_lowercase)

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        alpha_str = alpha[row] + alpha[row + col] + alpha[row]
        matrix[row].append(alpha_str)

# print(matrix)
for row in range(len(matrix)):
    print(' '.join(matrix[row]))
