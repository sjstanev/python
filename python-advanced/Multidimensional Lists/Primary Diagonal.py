n = int(input())

matrix = list()
sum_primary_diagonal = 0
# Create a matrix
for _ in range(n):
    matrix.append([x for x in input().split()])

for i in range(len(matrix)):
    sum_primary_diagonal += int(matrix[i][i])

print(sum_primary_diagonal)