import random

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

print("TIC TAC TOE")
while True:
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    move = int(input("Enter position (1-9): "))
    if board[move - 1] != "X" and board[move - 1] != "O":
        board[move - 1] = "X"
    else:
        print("Position already taken!")
        continue
    if (board[0] == board[1] == board[2] == "X" or
        board[3] == board[4] == board[5] == "X" or
        board[6] == board[7] == board[8] == "X" or
        board[0] == board[3] == board[6] == "X" or
        board[1] == board[4] == board[7] == "X" or
        board[2] == board[5] == board[8] == "X" or
        board[0] == board[4] == board[8] == "X" or
        board[2] == board[4] == board[6] == "X"):

        print()
        print(board[0], "|", board[1], "|", board[2])
        print("---------")
        print(board[3], "|", board[4], "|", board[5])
        print("---------")
        print(board[6], "|", board[7], "|", board[8])

        print("You Win!")
        break

    draw = True

    for item in board:
        if item != "X" and item != "O":
            draw = False

    if draw:
        print()
        print(board[0], "|", board[1], "|", board[2])
        print("---------")
        print(board[3], "|", board[4], "|", board[5])
        print("---------")
        print(board[6], "|", board[7], "|", board[8])

        print("Match Draw!")
        break

    while True:
        ai = random.randint(1, 9)

        if board[ai - 1] != "X" and board[ai - 1] != "O":
            board[ai - 1] = "O"
            break

    if (board[0] == board[1] == board[2] == "O" or
        board[3] == board[4] == board[5] == "O" or
        board[6] == board[7] == board[8] == "O" or
        board[0] == board[3] == board[6] == "O" or
        board[1] == board[4] == board[7] == "O" or
        board[2] == board[5] == board[8] == "O" or
        board[0] == board[4] == board[8] == "O" or
        board[2] == board[4] == board[6] == "O"):

        print()
        print(board[0], "|", board[1], "|", board[2])
        print("---------")
        print(board[3], "|", board[4], "|", board[5])
        print("---------")
        print(board[6], "|", board[7], "|", board[8])

        print("Computer Wins!")
        break
