def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def main():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a cell (1-9): ")

        # Validate input
        if move not in [str(i) for i in range(1, 10)]:
            print("Invalid input! Try again.")
            continue

        # Find the cell
        placed = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = current_player
                    placed = True
                    break
            if placed:
                break
        else:
            print("Cell already taken! Try another.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
