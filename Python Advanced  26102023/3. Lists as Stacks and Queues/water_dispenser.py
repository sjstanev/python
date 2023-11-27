"""
Input:
2
Peter
Amy
Start
2
refill 1
1
End

Output:
Peter got water
Amy got water
0 liters left
"""
from collections import deque

water_quantity = int(input())
people = deque()

while True:
    command = input()
    if command == 'Start':
        break

    people.append(command)

while True:
    command = input()
    if command == 'End':
        break

    elif command.startswith('refill'):
        params = command.split(' ')
        water_quantity += int(params[1])
    else:
        person = people.popleft()
        water_wanted = int(command)

    if water_wanted <= water_quantity:
        print(f'{person} got wait')
        water_quantity -= water_wanted
    else:
        print(f'{person} must wait')

print(f'{water_quantity} litters left')
