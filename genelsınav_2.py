import random

def create_board():
    return [[' ' for _ in range(10)] for _ in range(10)]

def print_board(board):
    print("   A B C D E F G H I J")
    for i, row in enumerate(board, start=1):
        print(f"{i:2} {' '.join(row)}")

def place_ship(board, ship, ship_symbol):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, 9 - ship)
            y = random.randint(0, 9)
            if all(board[y][x+i] == ' ' for i in range(ship)):
                for i in range(ship):
                    board[y][x+i] = ship_symbol
                break
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - ship)
            if all(board[y+i][x] == ' ' for i in range(ship)):
                for i in range(ship):
                    board[y+i][x] = ship_symbol
                break

def is_valid_move(move):
    try:
        x = ord(move[0].upper()) - ord('A')
        y = int(move[1:]) - 1
        return 0 <= x < 10 and 0 <= y < 10
    except (ValueError, IndexError):
        return False

def main():
    player_board = create_board()
    computer_board = create_board()

    ships = {'Mine': 1, 'Submarine': 2, 'Frigate': 3, 'Destroyer': 4, 'Cruiser': 5}

    for ship, size in ships.items():
        place_ship(computer_board, size, '+')

    turns = 0

    while True:
        print("\nYour Board:")
        print_board(player_board)
        
        try:
            player_move = input("Enter target coordinate (e.g., A1): ")
            
            if not is_valid_move(player_move):
                print("Invalid move. Try again.")
                continue

            x = ord(player_move[0].upper()) - ord('A')
            y = int(player_move[1:]) - 1

            if computer_board[y][x] == ' ':
                print("Miss!")
                player_board[y][x] = 'X'
            elif computer_board[y][x] == '+':
                print("Hit!")
                player_board[y][x] = '*'
                computer_board[y][x] = '*'
            else:
                print("You already fired at this location. Try again.")
                continue

            if all(cell == '*' for row in computer_board for cell in row):
                print("\nCongratulations! You sank all computer's ships!")
                break

            turns += 1

        except (ValueError, IndexError):
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
