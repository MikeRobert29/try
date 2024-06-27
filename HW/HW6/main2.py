import random

# Constants
EMPTY_CELL = 0

def initialize_board(width, height, candy_types):
    board = [[random.randint(1, candy_types) for _ in range(width)] for _ in range(height)]
    return board

def display_board(board, score):
    
    newBoard = ["".join(str(element) for element in sublist) for sublist in board]
    col = []
    
    for i in range(len(newBoard[0])) :
        col.append(str(i))
    
    print("\n\n")
    print("\t\t    " + "   ".join(col))
    
    i = 0
    while i < len(newBoard) :

        row = " " * (len(str(len(newBoard))) - len(str(i)))
        
        print("\t\t " + " " * len(str(len(newBoard))) + "+---" * len(newBoard[0]) + "+")
        print("\t\t" + row + str(i) + " | " + " | ".join(newBoard[i]) + " |")
        i += 1

    print("\t\t " + " " * len(str(len(newBoard))) + "+---" * len(newBoard[0]) + "+")
    print("\n")

    print(f"\t\tSCORE : {score}")
    print("\n")

def get_user_input():
    while True:
        try:
            x1, y1 = map(int, input("\n\t\tEnter the coordinates of the first candy (row col)            : ").split())
            x2, y2 = map(int, input("\n\t\tEnter the coordinates of the adjacent candy to swap (row col) : ").split())
            if abs(x1 - x2) + abs(y1 - y2) == 1:
                return (x1, y1), (x2, y2)
            else:
                print("\n\t\tCandies must be adjacent. Try again.")
        except ValueError:
            print("\n\t\tInvalid input. Try again.")

def crush_candies(board):
    rows, cols = len(board), len(board[0])
    to_crush = set()
    
    # Detect candies to crush
    for i in range(rows):
        for j in range(cols - 2):
            if board[i][j] and board[i][j] == board[i][j + 1] == board[i][j + 2]:
                to_crush.update([(i, j), (i, j + 1), (i, j + 2)])
                
    for i in range(rows - 2):
        for j in range(cols):
            if board[i][j] and board[i][j] == board[i + 1][j] == board[i + 2][j]:
                to_crush.update([(i, j), (i + 1, j), (i + 2, j)])
                
    if not to_crush:
        return board, 0
    
    # Crush candies
    for i, j in to_crush:
        board[i][j] = EMPTY_CELL
    
    # Drop candies
    for j in range(cols):
        write_index = rows - 1
        for i in range(rows - 1, -1, -1):
            if board[i][j] != EMPTY_CELL:
                board[write_index][j] = board[i][j]
                if write_index != i:
                    board[i][j] = EMPTY_CELL
                write_index -= 1
    print(len(to_crush))
    return board, len(to_crush)

def refill_board(board, candy_types):
    rows, cols = len(board), len(board[0])
    for j in range(cols):
        for i in range(rows):
            if board[i][j] == EMPTY_CELL:
                board[i][j] = random.randint(1, candy_types)

def swap_candies(board, pos1, pos2):
    (x1, y1), (x2, y2) = pos1, pos2
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

def is_valid_swap(board, pos1, pos2):
    swap_candies(board, pos1, pos2)
    new_board, crushed = crush_candies(board)
    swap_candies(board, pos1, pos2)  # Swap back to original
    return crushed > 0

def main():
    width       = int(input("\n\t\tEnter the width of the board      : "))
    height      = int(input("\n\t\tEnter the height of the board     : "))
    candy_types = int(input("\n\t\tEnter the number of candy types   : "))
    max_moves   = int(input("\n\t\tEnter the maximum number of moves : "))

    board = initialize_board(width, height, candy_types)
    score = 0
    moves = 0

    while moves < max_moves:
        display_board(board, score)
        pos1, pos2 = get_user_input()
        
        if not is_valid_swap(board, pos1, pos2):
            print("\n\t\tInvalid move. No candies would be crushed. Try again.")
            continue
        
        swap_candies(board, pos1, pos2)
        moves += 1
        
        while True:
            board, crushed = crush_candies(board)
            if crushed == 0:
                break
            score += crushed
            refill_board(board, candy_types)
        
    display_board(board, score)
    print("\n\n\t\t\tEND OF THE GAME\n")

if __name__ == "__main__":
    main()