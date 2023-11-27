message = input()
command = input()

while not command == "Reveal":

    command = command.split(':|:')
    if command[0] == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    if command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            start_index = message.index(substring)
            end_index = start_index + len(substring)
            substring = substring[::-1]
            message = message[:start_index] + message[end_index:] + substring
            print(message)
        else:
            print('error')

    if command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)
        else:
            print('error')
    command = input()

print(f"You have a new text message: {message}")