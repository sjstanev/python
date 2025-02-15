# import sys
# from io import StringIO
#
# test_input = '''4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67
# '''
# sys.stdin = StringIO(test_input)
#
# matrix = list()
# even_matrix = list()
#
#
# n = int(input())
#
# # Create matrix
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(",")])
#
# # Create matrix that contain only even elements with nested comprehensions
# even_matrix = [[index for index in matrix[row] if index % 2 == 0] for row in range(len(matrix))]
#
# print(even_matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Using loops top traverse multidimensional list
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
print()
# Using comprehension to traverse the multidimensional list

# new matrix that contain only second element on each row (multidimensional list)
matrix_v2 = [[row[x] for x in range(len(row)) if x == 1] for row in matrix]


# create simple list from matrix
matrix_v3 = [x for row in matrix for x in row ]
print(matrix_v2)
print(matrix_v3)
























# row, col = [int(x) for x in input().split(",")]
#
# for index in range(row):
#     matrix.append([int(x) for x in input().split(",")])
#     sum_elements += sum([x for x in matrix[index]])
#
# print(sum_elements)
# print(matrix)
#
# flattening
# matrix = [[j for j in range(1, 4)] for i in range(3)]
# print(matrix)
