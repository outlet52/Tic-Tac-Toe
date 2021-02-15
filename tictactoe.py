def board():
    print(f'''---------
| {c[0]} {c[1]} {c[2]} |
| {c[3]} {c[4]} {c[5]} |
| {c[6]} {c[7]} {c[8]} |
---------''')


def cord(field, moves):
    global player
    if moves % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    return (int(field[0]) - 1) * 3 + (int(field[1]) - 1)


def input_field(moves):
    while True:
        field = input('Enter the coordinates:').split()
        if not ''.join(field).isnumeric():
            print('You should enter numbers!')
        elif [i for i in field if int(i) < 1 or int(i) > 3]:
            print('Coordinates should be from 1 to 3!')
        elif c[cord(field, moves)] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            c[cord(field, moves)] = player
            break


def win_condition(moves):
    win = [1 for i in range(3) if [player] * 3 == c[i * 3:i * 3 + 3] or [player] * 3 == c[i::3] or [player] * 3 == c[::4] or [player] * 3 == c[2:7:2]]
    if win:
        print(f'{player} wins')
        exit()
    elif moves == 8:
        print('Draw')


c = [' ' for _ in range(9)]
board()
for moves in range(9):
    input_field(moves)
    board()
    if moves >= 4:
        win_condition(moves)
