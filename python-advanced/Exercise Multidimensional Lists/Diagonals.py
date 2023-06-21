elements = int(input())

matrix = list()
for _ in range(elements):
    matrix.append([x for x in input().split(",")])

print(len(matrix))

# for index in [row for row in matrix]:
#     print(index)
#     #print(matrix[index][index])
# print(matrix)
for row in matrix:
    for col in matrix:
        if row == col:
            print(matrix[row][col])


