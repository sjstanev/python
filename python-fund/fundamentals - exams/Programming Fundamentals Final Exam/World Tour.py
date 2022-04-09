initial_text = input()
text = initial_text     # use this text in all manipulation and remain intact initial input, use it later in the script

command = input()
while not command == 'Travel':
    command = command.split(':')

    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]

        # Insert the given string at that index only if the index is valid
        if index in range(len(text) + 1):
            text = text[:index] + string + text[index:]
        print(text)

    if command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        # Remove the elements of the string from the starting index to the end index
        if start_index in range(len(text)) and end_index in range(len(text)):
            text = text[:start_index] + text[end_index + 1:]
        print(text)

    # If the old string is in the initial string, replace it with the new one (all occurrences)
    if command[0] == 'Switch':
        old_string = (command[1])
        new_string = (command[2])
        # convert string to list divided by ':'
        message = text.split(':')

        if old_string in initial_text:
            #   lambda arguments : expression
            #   map(function_object, iterable1, iterable2,...)
            #   Syntax: l=list(map(lambda x: x.replace(‘old_value’,’new_value’),l))
            text = ':'.join(list(map(lambda x: x.replace(old_string, new_string), message)))
        print(text)

    command = input()

print(f'Ready for world tour! Planned stops: {text}')
