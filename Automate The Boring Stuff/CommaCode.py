spam = ['apples', 'bananas', 'tofu', 'cats']


def convert_list_to_string(list_param):

    new_string = ""
    lists_length = len(list_param)
    for index in range(int(lists_length)):

        if index != lists_length - 2 and index != lists_length - 1:
            new_string += list_param[index] + ", "
        else:
            if index == lists_length - 2:
                new_string += list_param[index] + ", and "
            else:
                new_string += list_param[index]
    return new_string


new_list = convert_list_to_string(spam)
print(new_list)
