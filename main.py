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

def user_selection():
    while True:
        row = int(input("Choose 0 for top row, 1 for middle , 2 for bottom\n"))
        if row < 3 :
            break
        else:
          print("Please Try again")
    while True:
        column = int(input("Choose 0 for left column , 1 for middle, 2 for right\n"))
        if column < 3:
             break
        else:
          print("Please Try again")

    board[row][column] = "X"
    display_board()

user_selection()
