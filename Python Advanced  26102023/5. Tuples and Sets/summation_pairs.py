"""
Sum of 2
1 5 4 2 2 3 1 3 2
4

with ordered values
1 1 2 2 2 3 3 4 5
target = 4
p1 = 1
p2 = 5

Algorithm:
current_sum = p1 + p2
current_sum <> target:
if current_sum == target:
    Great!
elif current_sum < target:
    p1 right
else: # current_sum < target:
    p2 left
"""
import time
from random import shuffle
ll = list(range(1024 * 8))
shuffle(ll)

print(ll)

target = 9
targets = set()
values_map = {}

start = time.time()
for value in ll:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f'{p1} + {p2} = {target}')
    else:
        targets.add(target-value)
        values_map[target-value] = value

end = time.time()
print(f'{end - start} s')

start = time.time()
for i1 in range(len(ll)):
    for i2 in range(i1 + 1, len(ll)):
        p1 = ll[i1]
        p2 = ll[i2]
        if p1 + p2 == target:
            print(f'{p1} + {p2} = {target}')

end = time.time()
print(f'{end - start} s')
