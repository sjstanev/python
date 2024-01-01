"""
Input:
1 2 3 4 5
------------------------
Output:
5 4 3 2 1
"""

stack = input().split()
reverse_stack = []

while stack:
    reverse_stack.append(stack.pop())

print(' '.join(reverse_stack))

"""
BETTER SOLUTION

while stack:
    last_number = stack.pop()
    print(last_number, end = ' ')
"""
