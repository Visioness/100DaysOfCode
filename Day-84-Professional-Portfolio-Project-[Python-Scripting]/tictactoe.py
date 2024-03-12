board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
    
game_over = False
turn = ['X', 'O']
turn_index = 0
print(f'''
        -------------------
        |     |     |     |
        -------------------
        |     |     |     |
        -------------------
        |     |     |     |
        -------------------
    ''')

while not game_over:
    
    row, column = input('Enter the cell you want to fill with "X" or "O" - ex. (2,1)\n').split(',')
    row = int(row)
    column = int(column)

    if (' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]):
        print('Draw!')
        break

    if board[row][column] != ' ':
        print('You can not change the already existing "X" or "O".')
        continue

    board[row][column] = turn[turn_index % 2]
    design = f'''
        -------------------
        |  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |
        -------------------
        |  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |
        -------------------
        |  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |
        -------------------
    '''
    print(board)
    print(design)

    for j in range(3):
        if (board[j][0] == board[j][1] == board[j][2] != ' ' or
            board[0][j] == board[1][j] == board[2][j] != ' ' or
            (board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ')):
            game_over = True
            print(f'{turn[turn_index % 2]} has won the game!')
            break
    turn_index += 1
