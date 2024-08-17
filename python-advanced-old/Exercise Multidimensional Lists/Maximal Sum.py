matrix = list()
max_sum_matrix = list()
# the same as -sys.maxsize
max_sum = float('-inf')
currant_sum = 0

rows, cols = [int(x) for x in input().split(' ')]

for _ in range(int(rows)):
    matrix.append([x for x in input().split(' ')])

for row in range(rows - 2):
    for col in range(cols - 2):
        # find max_sum and create list

        currant_sum = (
                int(matrix[row][col]) + int(matrix[row][col + 1]) + int(matrix[row][col + 2]) +
                int(matrix[row + 1][col]) + int(matrix[row + 1][col + 1]) + int(matrix[row + 1][col + 2]) +
                int(matrix[row + 2][col]) + int(matrix[row + 2][col + 1]) + int(matrix[row + 2][col + 2])
        )

        if max_sum < currant_sum:
            max_sum = currant_sum
            max_sum_matrix = [
                matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
            ]

print(f'Sum = {max_sum}')
print(' '.join(max_sum_matrix[:3]))
print(' '.join(max_sum_matrix[3:6]))
print(' '.join(max_sum_matrix[6:]))

