import random

board = [' ']*10
computer = 'X'
human = 'O'

def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('*' * 10)

def check_win():
    if (board[1]==board[2]==board[3] and board[1]!=' ') or \
       (board[4]==board[5]==board[6] and board[4]!=' ') or \
       (board[7]==board[8]==board[9] and board[7]!=' ') or \
       (board[1]==board[4]==board[7] and board[1]!=' ') or \
       (board[2]==board[5]==board[8] and board[2]!=' ') or \
       (board[3]==board[6]==board[9] and board[3]!=' ') or \
       (board[1]==board[5]==board[9] and board[1]!=' ') or \
       (board[7]==board[5]==board[3] and board[7]!=' '):
        return True
    else:
        return False

def check_draw():
    if board.count(' ') == 1:
        return True
    else:
        return False

def insert(letter, pos):
    if board[pos] == ' ':
        board[pos] = letter 
        display_board(board)
    else:
        if letter == 'O':
            pos = int(input('Not Free! Please re-enter the position: '))
            insert(letter, pos)
        else:
            pos = random.randint(1, 9)
            insert(letter, pos)

def human_move(letter):
    pos = int(input("Enter the Position to insert: "))
    insert(letter, pos)

def computer_move(letter):
    pos = random.randint(1, 9)
    insert(letter, pos)

while not (check_win() or check_draw()):
    display_board(board)
    computer_move(computer)
    if check_win() or check_draw():
        break
    human_move(human)

if check_win():
    if board.count('X') > board.count('O'):
        print("Computer Wins")
    else:
        print("Human Wins")
else:
    print("Game Draw")
