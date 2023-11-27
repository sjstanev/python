"""
Input
3
1 5
10 3
3 4
"""
from collections import deque

stations = int(input())
# amount_of_petrol, distance = int(input().split())
pumps = deque()

for _ in range(stations):
    pumps.append([int(x) for x in input().split()])

for attempt in range(stations):
    trunk = 0
    failed = False
    for petrol, distance in pumps:  # we do unpacking
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())   # we can use rotate method => pumps.rotate(-1)
    else:
        print(attempt)
        break
