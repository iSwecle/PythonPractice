print(input("""Welcome To Tic Tac Toe!
by Kurt Chim G. Beadoy (2024)
Press 'Enter' to start."""))
board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']
         ]
winner = False
crdrange = [0, 1, 2]
attempt = 0
limit = 9 
def grid():
    print("~TIC TAC TOE~")
    print("-------------")
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print("-------------")
grid()
def input1():
    global player
    print("~Player X~")
    while True:
        try:
            row = int(input("Which Row?(0-2):"))
            column = int(input("Which Column?(0-2):"))
            try:
                if board[row][column] == "-":
                    board[row][column] = 'X'
                else:
                    print("Cell Occupied")
                    input1()
                player = 'X'
                break
            except IndexError:
                print("Try Again.")
        except ValueError:
            print("Try Again.")
def input2():
    global player
    print("~Player O~")
    while True:
        try:
            row = int(input("Which Row?(0-2):"))
            column = int(input("Which Column?(0-2):"))
            try:
                if board[row][column] == "-":
                    board[row][column] = 'O'
                else:
                    print("Cell Occupied")
                    input2()
                player = 'O'
                break
            except IndexError:
                print("Try Again.")
        except ValueError:
            print("Try Again.")
def winnings():
    global winner
    if board[0][0] == board[0][1] == board[0][2] != '-':
        winner = True
    if board[1][0] == board[1][1] == board[1][2] != '-':
        winner = True
    if board[2][0] == board[2][1] == board[2][2] != '-':
        winner = True
    if board[0][0] == board[1][1] == board[2][2] != '-':
        winner = True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        winner = True
    if board[0][0] == board[1][0] == board[2][0] != '-':
        winner = True
    if board[0][1] == board[1][1] == board[2][1] != '-':
        winner = True
    if board[0][2] == board[1][2] == board[2][2] != '-':
        winner = True
    if all(box != "-" for row in board for box in row):
    #If every box in every row of the board is not equal to "-".
        print("IT'S A TIE!!")
        quit()
condition = True
while True:
    while condition == True:
        input1()
        grid()
        winnings()
        condition = False
        if winner == True:
            print(f"GAME OVER!! Player {player}'s Win")
            quit()
    while condition == False:
        input2()
        grid()
        winnings()
        condition = True
        if winner == True:
            print(f"GAME OVER!! Player {player}'s Win")
            quit()

