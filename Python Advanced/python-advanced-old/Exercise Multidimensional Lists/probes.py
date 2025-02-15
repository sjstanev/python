from io import StringIO
import sys

text_input = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''

sys.stdin = StringIO(text_input)
matrix = list()

n = int(input())

# Create matrix
for _ in range(n):
    matrix.append([int(x) for x in input().split(",")])

#matrix = [['1', '2', '3'], ['4', '5', '6']]
def swap(matrix , row1, col1, row2, col2):
    temp = matrix[row1][col1]
    matrix[row1][col1] = matrix[row2][col2]
    matrix[row2][col2] = temp
    return matrix

print(matrix)
print('swapped matrix: ', swap(matrix, 0, 0, 1, 1))

# Some probes
