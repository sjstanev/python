message = input()
command = input()

while not command == "Reveal":
    command = input().split(':|:')
    if command[0] == "InsertSpace":
        index = command[1]
        message = message[:index] + " " + message[index:]
        print(message)
    if command[0] == "Reverse":
        pass
    if command[0] == "ChangeAll":
        pass
    command = input()

print("You have a new text message: {message}")