original_string = input()

# better solutions
# original_string = [::-1]
# original_string.reverse()

s = []
for c in original_string:
    # push into the stack
    s.append(c)

reversed_string = ''

while s:
    reversed_string += s.pop()  # pop the top of stack

print(reversed_string)