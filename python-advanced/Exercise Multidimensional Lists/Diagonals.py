matrix = list()
primary_diagonal = list()
secondary_diagonal = list()


n = int(input())

for _ in range(n):
    matrix.append([int(x) for x in input().split(',')])

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n-1-i])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

