text = list(input())
openning_parenthesis = []
clossed_parenthesis = []
match_parenthesis = []

for x in range(len(text)):

    if text[x] == "(":
        openning_parenthesis.append(x)
    if text[x] == ")" and openning_parenthesis:
        start_index = int(openning_parenthesis.pop())
        end_index = int(x)
        match_parenthesis.append("".join(text[start_index:end_index+1]))

for expression in match_parenthesis:
    print(expression)