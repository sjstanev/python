matrix = list()
sum_elements = 0

row, col = [int(x) for x in input().split(",")]

for index in range(row):
    matrix.append([int(x) for x in input().split(",")])
    sum_elements += sum([x for x in matrix[index]])

print(sum_elements)
print(matrix)
