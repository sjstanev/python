"""
Input:
5 4 8 6 3 8 7 7 9
16
-------
Output
16
"""

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

counter_of_racks = 1
current_capacity = rack_capacity

while clothes:
    current_clothe = clothes[-1]
    if current_clothe < current_capacity:
        clothes.pop()   # stack pop()
        current_capacity -= current_clothe  # decrease current_capacity
    else:
        counter_of_racks += 1
        current_capacity = rack_capacity


print(counter_of_racks)
