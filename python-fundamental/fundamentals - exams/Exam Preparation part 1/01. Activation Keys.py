activation_key = input()
command = input()

while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    if command[0] == "Flip":
        startIndex = int(command[2])
        endIndex = int(command[3])
        if command[1] == "Upper":
            activation_key = activation_key[:startIndex] + activation_key[startIndex:endIndex].upper() + activation_key[endIndex:]
        elif command[1] == "Lower":
            activation_key = activation_key[:startIndex] + activation_key[startIndex:endIndex].lower() + activation_key[endIndex:]
        print(activation_key)
    if command[0] == "Slice":
        startIndex = int(command[1])
        endIndex = int(command[2])
        activation_key = activation_key[:startIndex] + activation_key[endIndex:]
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")