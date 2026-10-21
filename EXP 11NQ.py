def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def nqueen(board, row, n):
    if row == n:
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            nqueen(board, row + 1, n)
            board[row] = -1


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


n = int(input("Enter the value of N: "))
board = [-1] * n

nqueen(board, 0, n)