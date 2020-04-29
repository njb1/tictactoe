player1_marker = ""
player2_marker = ""
current_player = ""
board = ['']*10
win = False

def check_if_win(board):
    global win
    if board[1] == board[2] == board[3] !='':
        print(f"You win {current_player}")
        win = True
    elif board[4] == board[5]  == board[6] !='':
        print(f"You win {current_player}")
        win = True
    elif board[7] == board[8] == board[9] !='':
        print(f"You win {current_player}")
        win = True
    elif board[1] == board[4]  == board[7] !='':
        print(f"You win {current_player}")
        win = True
    elif board[2] == board[5] == board[8] !='':
        print(f"You win {current_player}")
        win = True
    elif board[3] == board[6] == board[9] !='':
        print(f"You win {current_player}")
        win = True
    elif board[1] == board[5] == board[9] !='':
        print(f"You win {current_player}")
        win = True
    elif board[3] == board[5] == board[7] !='':
        print(f"You win {current_player}")
        win = True
    else:
        win = False
        move()


def choose_marker():
    choice = input('Hello player 1, do you want to be X or O?" > ')
    global player1_marker
    global player2_marker
    global current_player
    if choice.upper() == 'X':
        player1_marker = 'X'
        player2_marker = 'O'
    elif choice.upper() == 'O':
        player1_marker = 'O'
        player2_marker = 'X'
    else:
        print("Does not compute... try again")
        choose_marker()

    print(f"Thank you... Player 1 is {player1_marker} and Player 2 is {player2_marker}")
    current_player = "Player 1"

def print_board(board):
    test_board = [' ']*10
    if len(board) == 0:
        print(test_board[7] + '|' + test_board[8] + '|' + test_board[9])
        print("-----")
        print(test_board[4] + '|' + test_board[5] + '|' + test_board[6])
        print("-----")
        print(test_board[1] + '|' + test_board[2] + '|' + test_board[3])
    else:
        print(board[7] + '|' + board[8] + '|' + board[9])
        print("-----")
        print(board[4] + '|' + board[5] + '|' + board[6])
        print("-----")
        print(board[1] + '|' + board[2] + '|' + board[3])


def move():
    counter = 0
    global current_player
    global board
    while counter <= 9 and not win:
        if current_player == "Player 1":
            print(f"Your move {current_player}")
            choice = input(f'Hello {current_player}, choose 1-9?')
            if board[int(choice)] == "" != "X" !="O":
                board.insert(int(choice), player1_marker)
                print_board(board)
                check_if_win(board)
                current_player = "Player 2"
                counter += 1
                move()
            else:
                print('Ooops... already taked, try again')
                move()
            current_player = "Player 2"
        else:
            if current_player == "Player 2":
                print(f"Your move {current_player}, choose 1-9")
                choice = input(f'Hello {current_player}, choose 1-9?')
                if board[int(choice)] == "":
                    board.insert(int(choice), player2_marker)
                    print_board(board)
                    check_if_win(board)
                    current_player = "Player 1"
                    counter += 1
                else:
                    print('Ooops... already taked, try again')
                    move()
            current_player = "Player 1"
        
    if current_player == "Player 1":
        current_player = "Player 2"
    else:
        current_player = "Player 1"


choose_marker()

move()


