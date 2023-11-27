text = input()
command = input()

while not command == "For Azeroth":
    command = command.split()

    if command[0] == "GladiatorStance":
        text = text.upper()
        print(text)

    elif command[0] == "DefensiveStance":
        text = text.lower()
        print(text)

    elif command[0] == "Dispel":
        index = int(command[1])
        letter = command[2]
        if index in range(len(text)):
            text = text[:index] + letter + text[index+1:]
            print("Success!")
        else:
            print("Dispel too weak.")

    elif command[0] + ' ' + command[1] == "Target Change":
        first_str = command[2]
        second_str = command[3]
        if first_str in text:
            text = text.replace(first_str, second_str)
            print(text)
        else:
            print(text)

    elif command[0] + ' ' + command[1] == "Target Remove":
        sub_str = command[2]
        if sub_str in text:
            text = text.replace(sub_str, '')
            print(text)
    else:
        print("Command doesn't exist!")

    command = input()
