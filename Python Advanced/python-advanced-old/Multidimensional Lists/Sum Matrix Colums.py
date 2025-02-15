matrix = list()

row, col = [int(x) for x in input().split(',')]

for _ in range(row):
    matrix.append([x for x in input().split(' ')])

for column_index in range(col):
    sum_col = 0
    for row in matrix:
        sum_col += int(row[column_index])
    print(sum_col)
