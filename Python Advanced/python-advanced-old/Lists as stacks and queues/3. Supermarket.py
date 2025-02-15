from collections import deque

people_in_queue = deque()
command = input()

while command != "End":
    if command == "Paid":
        while len(people_in_queue):
            print(people_in_queue.popleft())
    else:
        people_in_queue.append(command)
    command = input()

print(f"{len(people_in_queue)} people remaining.")


