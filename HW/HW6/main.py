#coding : utf-8

def crush_candies(board):
    rows, cols = len(board), len(board[0])
    to_crush = set()
    
    # Step 1: Mark candies to be crushed
    for i in range(rows):
        for j in range(cols - 2):
            if board[i][j] and board[i][j] == board[i][j + 1] == board[i][j + 2]:
                to_crush.update([(i, j), (i, j + 1), (i, j + 2)])
                
    for i in range(rows - 2):
        for j in range(cols):
            if board[i][j] and board[i][j] == board[i + 1][j] == board[i + 2][j]:
                to_crush.update([(i, j), (i + 1, j), (i + 2, j)])
                
    if not to_crush:
        return board, False
    
    # Step 2: Crush the candies
    for i, j in to_crush:
        board[i][j] = 0
    
    # Step 3: Drop the candies
    for j in range(cols):
        write_index = rows - 1
        for i in range(rows - 1, -1, -1):
            if board[i][j] != 0:
                board[write_index][j] = board[i][j]
                if write_index != i:
                    board[i][j] = 0
                write_index -= 1
    
    return board, True

def candy_crush(board):
    while True:
        board, changed = crush_candies(board)
        if not changed:
            break
    return board

# Example usage
grid = [[9,9,7,9,9,9],[7,7,6,8,9,9],[5,6,5,6,8,8],[1,5,1,4,1,1],[2,1,4,1,1,1],[1,4,1,3,1,1],[1,1,2,1,3,1],[1,2,1,1,1,3]]
final_board = candy_crush(grid)

print(grid)