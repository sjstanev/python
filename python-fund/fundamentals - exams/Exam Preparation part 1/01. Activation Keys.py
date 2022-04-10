activation_key = input()
commnad = input()

while not commnad == "Generate":
    commnad = commnad.split(">>>")
    if commnad[0] == "Contains":
        if commnad[1] in activation_key:
            print(f"{activation_key} contains {commnad[1]}")
        else:
            print("Substring not found!")
    if commnad[0] == "Flip":
        startIndex = int(commnad[2])
        endIndex = int(commnad[3])
        if commnad[1] == "Upper":
            activation_key = activation_key[:startIndex] + activation_key[startIndex:endIndex].upper() + activation_key[endIndex:]
        elif commnad[1] == "Lower":
            activation_key = activation_key[:startIndex] + activation_key[startIndex:endIndex].lower() + activation_key[endIndex:]
        print(activation_key)
    if commnad[0] == "Slice":
        startIndex = int(commnad[1])
        endIndex = int(commnad[2])
        activation_key = activation_key[:startIndex] + activation_key[endIndex:]
        print(activation_key)
    commnad = input()

print(f"Your activation key is: {activation_key}")