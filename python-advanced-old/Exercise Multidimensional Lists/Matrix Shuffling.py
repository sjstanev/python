from io import StringIO
import sys

text_input = '''1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
'''


def swap(new_matrix, row1, col1, row2, col2):
    temp = new_matrix[row1][col1]
    new_matrix[row1][col1] = new_matrix[row2][col2]
    new_matrix[row2][col2] = temp
    return new_matrix


sys.stdin = StringIO(text_input)
matrix = list()
rows, cols = [x for x in input().split(' ')]

for _ in range(int(rows)):
    matrix.append([x for x in input().split()])

command = input()

while command != 'END':

    # find length of the command, whether contain 5 elements
    len_command = len([x for x in command.split(' ')])

    # find that command with the "swap" keyword along with four valid coordinates
    if command.startswith('swap ') and len_command == 5:
        start_with, row1, col1, row2, col2 = [x for x in command.split(' ')]
        if row1 < rows and row2 < rows and col1 < cols and col2 < cols:
            swap(matrix, int(row1), int(col1), int(row2), int(col2))
            [print(' '.join(row)) for row in matrix]
    else:
        print('Invalid input!')

    command = input()
