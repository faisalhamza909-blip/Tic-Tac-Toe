print("Welcome to tic tac toe")
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
def display_board():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("_________")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("_________")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

def player_select(symbol):
    while True:
        row = int(input(f"{symbol} user Choose 0 for top row, 1 for middle , 2 for bottom\n"))
        if not (0 <= row < 3):
            print("Please enter a correct row")
            continue
        column = int(input(f"{symbol} user Choose 0 for left column , 1 for middle, 2 for right\n"))
        if not ( 0 <= column < 3):
            print("Please enter a correct column")
            continue

        if board[row][column] == " ":
            board[row][column] = symbol
            display_board()
            break
        else:
            print("Invalid move")

def check_winner(symbol):
    # Rows
    if board[0] == [symbol, symbol, symbol]:
        print(f"{symbol} wins!")
        return True
    if board[1] == [symbol, symbol, symbol]:
        print(f"{symbol} wins!")
        return True
    if board[2] == [symbol, symbol, symbol]:
        print(f"{symbol} wins!")
        return True

    # Columns
    if board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
        print(f"{symbol} wins!")
        return True
    if board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol:
        print(f"{symbol} wins!")
        return True
    if board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol:
        print(f"{symbol} wins!")
        return True

    # Diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        print(f"{symbol} wins!")
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        print(f"{symbol} wins!")
        return True

    return False





display_board()

while True:
    player_select("X")
    if check_winner("X"):
        break
    player_select("O")
    if check_winner("O"):
        break






