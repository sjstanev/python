expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'

'''
'1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
s = [4, 9 

'1' not a bracket
' ' not a bracket
'+' not a bracket
'(' is opening bracket
    -> add its index to the stack
'2' not a bracket
' ' not a bracket
'-' not a bracket
' ' not a bracket
'(' is opening bracket
    -> add its index to the stack
'2' not a bracket
' ' not a bracket
'3' not a bracket
')' is classing bracket
    -> pop the top from the stack
    -> subexpression is between top of the stack and this closing bracket
    -> s = [4, (remove 9) ] => 9,15 => (2 + 3)
' ' not a bracket
.....
'''

s = []
for i in range(len(expression)):
    if expression[i] == '(':
        s.append(i)
    elif expression[i] == ')':
        start_index = s.pop()
        end_index = i
        print(expression[start_index:end_index+1])
