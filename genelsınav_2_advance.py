import random

def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_boards(player_board, opponent_board, show_ships=False):
    print("Player Board:")
    print("   " + " ".join([chr(65+i) for i in range(len(player_board))]))
    for i, row in enumerate(player_board):
        print(f"{i+1:2} {' '.join(cell if cell == 'X' or cell == 'O' or show_ships else ' ' for cell in row)}")

    print("\nOpponent Board:")
    print("   " + " ".join([chr(65+i) for i in range(len(opponent_board))]))
    for i, row in enumerate(opponent_board):
        print(f"{i+1:2} {' '.join(cell if cell == 'X' or cell == 'M' else ' ' for cell in row)}")

def place_ship(board, ship_size):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, len(board) - ship_size)
            y = random.randint(0, len(board) - 1)
            if all(board[y][x+i] == ' ' for i in range(ship_size)):
                for i in range(ship_size):
                    board[y][x+i] = 'O'
                break
        else:
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board) - ship_size)
            if all(board[y+i][x] == ' ' for i in range(ship_size)):
                for i in range(ship_size):
                    board[y+i][x] = 'O'
                break

def is_valid_move(move, board):
    x, y = move
    return 0 <= x < len(board) and 0 <= y < len(board) and board[y][x] == ' '

def main():
    board_size = 8
    num_ships = 3
    player_board = create_board(board_size)
    opponent_board = create_board(board_size)

    for _ in range(num_ships):
        place_ship(player_board, 3)

    for _ in range(num_ships):
        place_ship(opponent_board, 3)

    turns = 0
    player_moves = set()
    opponent_moves = set()

    while True:
        print_boards(player_board, opponent_board)
        print("Previous Player Moves:", player_moves)
        
        try:
            x = ord(input("Enter target column (A-H): ").upper()) - ord('A')
            y = int(input("Enter target row (1-8): ")) - 1
            player_move = (x, y)

            if player_move in player_moves:
                print("You already fired at this location. Try again.")
                continue
            
            player_moves.add(player_move)

            if is_valid_move(player_move, opponent_board):
                if opponent_board[y][x] == 'O':
                    print("Hit!")
                    opponent_board[y][x] = 'X'
                    turns += 1
                else:
                    print("Miss!")
                    opponent_board[y][x] = 'M'
                    turns += 1
            else:
                print("Invalid move. Try again.")
                continue

            if all(cell == 'X' for row in opponent_board for cell in row):
                print_boards(player_board, opponent_board, show_ships=True)
                print(f"Congratulations! You sank all the opponent's battleships in {turns} turns.")
                break

            # Opponent's move
            while True:
                x = random.randint(0, len(player_board) - 1)
                y = random.randint(0, len(player_board) - 1)
                opponent_move = (x, y)
                if opponent_move not in opponent_moves:
                    opponent_moves.add(opponent_move)
                    break

            if is_valid_move(opponent_move, player_board):
                if player_board[y][x] == 'O':
                    print("Opponent hit your battleship!")
                    player_board[y][x] = 'X'
                else:
                    print("Opponent missed!")
                    player_board[y][x] = 'M'
            else:
                continue

            if all(cell == 'X' for row in player_board for cell in row):
                print_boards(player_board, opponent_board, show_ships=True)
                print(f"Game over! The opponent sank all your battleships in {turns} turns.")
                break

        except (ValueError, IndexError):
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
