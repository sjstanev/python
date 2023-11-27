current_sum = 0
sub_matrix_sum = 0
matrix = list()
matrix_elements = list()

row, column = [int(x) for x in input().split(',')]

# Create a matrix
for _ in range(row):
    matrix.append([int(x) for x in input().split(',')])

for i in range(row-1):
    for j in range(column-1):

        # find substring current sum
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if sub_matrix_sum < current_sum:
            sub_matrix_sum = current_sum
            matrix_elements = f'{matrix[i][j]} {matrix[i][j+1]} {matrix[i+1][j]} {matrix[i+1][j+1]}'.split()

print(" ".join(matrix_elements[:2]))
print(" ".join(matrix_elements[2:]))
print(sub_matrix_sum)