# nested comprehensions
matrix = [[j for j in range(1, 4)] for i in range(3)]
print(matrix)

# -----------------------------------------------------------------------------------
import sys
from io import StringIO

test_input = '''4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
'''
sys.stdin = StringIO(test_input)

matrix = list()
even_matrix = list()
even_matrix_v2 = list()

n = int(input())

# Create matrix
for _ in range(n):
    matrix.append([int(x) for x in input().split(",")])

# Create matrix that contain only even elements
for row in range(len(matrix)):
    even_matrix.append([])
    for index in matrix[row]:
        if index % 2 == 0:
            even_matrix[row].append(index)

# Create the same matrix that contain only even elements using nested comprehensions
even_matrix_v2 = [[index for index in matrix[row] if index % 2 == 0] for row in range(len(matrix))]

print(even_matrix)
print(even_matrix_v2)

# -----------------------------------------------------------------------------------
n = int(input())

# Create simple list from matrix


# Using map we create map object
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map(function, iterables)
# convert the map into a list, for readability: list(x)
# EXAMPLE:
# def myfunc(a):
#   return len(a)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))
#
# print(x)
#
# RESULT:
# <map object at 0x056D44F0>
# [5, 6, 6]
matrix = [map(int, input().split(',')) for _ in range(n)]

flatted_v2 = list()
# Create simple list from matrix
for row in matrix:
    for x in list(row):
        flatted_v2.append(x)

print(flatted_v2)

# Create simple list from matrix using list comprehension
flatted = [x for row in matrix for x in row]
print(flatted)

# -----------------------------------------------------------------------------------
# multidimensional vs simple list
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

# new matrix that contain only second element on each row (multidimensional list)
matrix_v2 = [[row[x] for x in range(len(row)) if x == 1] for row in matrix]
print(matrix_v2)

# create simple list from matrix
matrix_v3 = [x for row in matrix for x in row ]
print(matrix_v3)
# -----------------------------------------------------------------------------------

