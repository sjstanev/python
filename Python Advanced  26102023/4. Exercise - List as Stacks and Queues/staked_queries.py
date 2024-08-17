"""
Input:
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

Output:
26
20
91, 20, 26
"""

queries_count = int(input())
stack = []

for _ in range(queries_count):
    expression = [x for x in input().split()]
    command = expression[0]

    if command == '1':
        stack.append(expression[1])
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())

print(', '.join(reversed_stack))
