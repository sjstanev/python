def add_piece(list_of_pieces: list, current_piece: str, current_composer:str, current_key: str ):
    is_already_inlist = False
    for x in list_of_pieces:
        if x['piece'] == current_piece:
            is_already_inlist = True
            break

    if is_already_inlist:
        print(f'{current_piece} is already in the collection!')
    else:
        print(f'{current_piece} by {current_composer} in {current_key} added to the collection!')
        return {'piece': current_piece, 'composer':current_composer, 'key':current_key}

def remove_piece(list_of_pieces: list, current_piece: str):

    for x in list_of_pieces:
        if x['piece'] == current_piece:
            print(f'Successfully removed {current_piece}!')
            return list_of_pieces.index(x)

    print(f'Invalid operation! {current_piece} does not exist in the collection.')
    return 'None'

def changekey_in_piece(list_of_pieces: list, current_piece: str, current_key: str ):
    for x in list_of_pieces:
        if x['piece'] == current_piece:
            print(f"Changed the key of {x['piece']} to {current_key}!")
            x['key'] = current_key
            return x['key']

    print(f'Invalid operation! {current_piece} does not exist in the collection.')
    return 'None'

#"{piece}|{composer}|{key}".
number_of_pieces = int(input())
pieces = {}
list_of_pieces = []

# Create list that contain dict with piece, their composer and key
for i in range(number_of_pieces):
    pieces_info = input().split('|')
    # Create dict with piece, their composer and key
    piece = {'piece': pieces_info[0], 'composer':pieces_info[1], 'key':pieces_info[2]}
    list_of_pieces.append(piece)

# executed commands received from console "Add|{piece}|{composer}|{key}" until receive 'STOP':
command = input()

while not command == "Stop":
    command = command.split('|')

    # Add piece to dict if missing
    if command[0] == 'Add':
        result = add_piece(list_of_pieces, command[1],command[2] ,command[3])
        if result:
            list_of_pieces.append(result)

    # Remove  piece from dict if it's there
    if command[0] == 'Remove':
        result = remove_piece(list_of_pieces, command[1])
        if not result == 'None':
            del list_of_pieces[result]

    # Change key for specific piece
    if command[0] == 'ChangeKey':
        result = changekey_in_piece(list_of_pieces, command[1],command[2])

    command = input()

for piece in list_of_pieces:
    print(f"{piece['piece']} -> Composer: {piece['composer']}, Key: {piece['key']}")