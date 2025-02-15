matrix = list()
even_matrix = list()

n = int(input())

# Create matrix
for _ in range(n):
    matrix.append([int(x) for x in input().split(",")])

# Create matrix that contain only even elements with nested comprehensions
even_matrix = [[index for index in matrix[row] if index % 2 == 0] for row in range(len(matrix))]

print(even_matrix)
