message = input()
command = input().split('|')

while not command[0] == "Decode":

    if command[0] == "Move":
        message = message[int(command[1]):] + message[:int(command[1])]
    elif command[0] == "Insert":
        char = int(command[1])
        index = command[2]
        message = list(message)
        message.insert(char, index)
        message = ''.join(message)

    elif command[0] == "ChangeAll":
        old_char = command[1]
        new_char = command[2]
        message = list(message)
        if old_char in message:
            #   lambda arguments : expression
            #   map(function_object, iterable1, iterable2,...)
            #   Syntax: l=list(map(lambda x: x.replace(‘old_value’,’new_value’),l))

            message = ''.join(list(map(lambda x: x.replace(old_char,new_char), message)))

    command = input().split('|')

print(f"The decrypted message is: {message}")
