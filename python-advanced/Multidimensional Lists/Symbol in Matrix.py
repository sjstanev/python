n = int(input())

matrix = list()
is_found = False
index_position = set()

# Create a matrix
for _ in range(n):
    matrix.append([x for row in input().split() for x in row])

# Searching element
element = input()

for i in range(n):
    if is_found:
        break
    for j in range(n):
        if matrix[i][j] == element:
            index_position = (i, j)
            is_found = True
            break
if is_found:
    print(index_position)
else:
    print(f'{element} does not occur in the matrix')
