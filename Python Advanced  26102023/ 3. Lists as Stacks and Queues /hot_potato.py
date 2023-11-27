"""
Input:
George Peter Michael William Thomas
10
Output:
Removed Thomas
Removed Peter
Removed Michael
Removed George
Last is William
"""
from collections import deque

kids_string = input()
tosses_count = int(input())

kids = deque(kids_string.split(' '))

current_count = 0
while len(kids) > 1:
    current_count += 1
    kid = kids.popleft()
    if current_count < tosses_count:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current_count = 0

print(f'Last is {kids.popleft()}')
