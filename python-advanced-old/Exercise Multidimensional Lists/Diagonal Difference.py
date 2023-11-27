matrix = list()
sum_primary_diagonal = 0
sum_secondary_diagonal = 0


n = int(input())

for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

for i in range(len(matrix)):
    sum_primary_diagonal += matrix[i][i]
    sum_secondary_diagonal += matrix[i][n - 1 - i]

print(abs(sum_primary_diagonal - sum_secondary_diagonal))


