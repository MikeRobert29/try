#coding : utf-8

import random
import os

def displayGrid(grid):
    
    newBoard = ["".join(str(element) for element in sublist) for sublist in grid]
    col = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    
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

def fillGrid(grid) :

	choices         = [x for x in range(10)]
	mineCoordinates = [[] * 9] * 9

	for i in choices :
		k = random.choice(choices)
		mineCoordinates[i].append(k)
		i += 1

    for row in mineCoordinates :
    	k = random.choice(choices)
    	row.append(k)
    	choices.remove(k)

    for coordinate in mineCoordinates :
    	grid[coordinate[0]][coordinate[1]] = "*"

    return mineCoordinates

def count_adjacent_mines(grid, row, col) :

    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (1, 1)]
    
    for d_row, d_col in directions:
        n_row, n_col = row + d_row, col + d_col
        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
            if grid[n_row][n_col] == '*':
                count += 1
                
    return count

def reveal_cell(grid, revealed, row, col) :

    if revealed[row][col] :
        return

    revealed[row][col] = True

    if grid[row][col] == 0:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for d_row, d_col in directions:
            n_row, n_col = row + d_row, col + d_col
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                reveal_cell(grid, revealed, n_row, n_col)

def main() :

    grid         = [[" "] * 9] * 9
    numberOfMine = 10
    playerInput  = ""
    tuto         = "Design a cell coordinates by the column where it is his column (a letter from a to i), followed by his row (ex : a5),\nadd f to the cell coordinats to add or remove a flag (ex : a5f)."
    
    print("\n\t\tWELCOME TO MINESWEEPER")
    print("\n\t\t\t:)")
    displayGrid(grid)
    
    while True :

        playerInput = input("Type \"yes\" if you want to start a new game and \"no\" otherwise : ")

        if playerInput == "no" :
        	break
        elif playerInput == "yes" :
        	
        	print(tuto)
        	os.system("cls")

        	mine = fillGrid(grid)
        	displayGrid(grid)
        
        if grid[row][col] == '*':
            print("Game Over! You hit a mine!")
            displayGrid(grid, reveal=True)
            break
        
        reveal_cell(grid, revealed, row, col)

        if all(all(revealed[row][col] or grid[row][col] == '*' for col in range(cols)) for row in range(rows)):
            print("Congratulations! You win!")
            print_grid(grid, reveal=True)
            break

if __name__ == "__main__":
    main()