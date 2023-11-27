from collections import deque

# input => George "Peter", "William", "Paid", "Michael", "Oscar", "Olivia", "Linda", "End"

queue = deque()

while True:

    command = input()

    if command == 'End':
        print(f'{len(queue)} people remaining')
        break
    elif command == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)


