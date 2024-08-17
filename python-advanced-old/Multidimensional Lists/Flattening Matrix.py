n = int(input())

# Create matrix
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

flatted = [x for row in matrix for x in row]
print(flatted)
