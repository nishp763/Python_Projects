import copy

# this function checks whether a number can be placed in row,col specified by the user
# Rules of Sudoku:
# - a number can only appear once along any row
# - a number can only appear once along any col
# - a number can only appear once in the mini 3x3 grid
def is_move_possible(row,col,num,puzzle_list):
    # check along row and col
    for index in range(0,9):
        if puzzle_list[row][index] == num: # if number exists in the row
            #print("Number found along Row")
            return False

        if puzzle_list[index][col] == num: # if number exists in the col
            #print("Number found along Column")
            return False

    # check within the mini 3x3 grid
    x0 = (row//3)*3
    y0 = (col//3)*3
    for x in range(0,3):
        for y in range(0,3):
            if puzzle_list[x0+x][y0+y] == num:
                #print("Number found in Grid")
                return False
    return True # number doesn't exist and the move is valid

def solve_sudoku(puzzle_list):
    for row_i in range(0,9):
        for col_i in range(0,9):
            if puzzle_list[row_i][col_i] == 0:
                for n in range(1,10):
                    if is_move_possible(row_i,col_i,n,puzzle_list):
                        puzzle_list[row_i][col_i] = n
                        if (trial := solve_sudoku(puzzle_list)):
                            return trial
                        else:
                            puzzle_list[row_i][col_i] = 0
                return False
    return puzzle_list

def print_sudoku(puzzle_list):
    localpuzzle = copy.deepcopy(puzzle_list)
    row_count = 0 # tracks which row is being printed
    print() # print empty line
    for row in localpuzzle: # iterate through row by row
        row_count += 1 # increment row count
        for item in range(0,9): # replace 0's with *
            if (row[item] == 0):
                row[item] = '*'

        print('{} {} {} | {} {} {} | {} {} {}'
                .format(row[0],row[1],row[2],row[3],
                row[4],row[5],row[6],row[7],row[8]))

        # Print horizontal line after 3rd and 6th row
        if (row_count == 3) or (row_count == 6):
            print('-'*21)

    print() # print emtpy line
    return

if __name__ == "__main__":
    # declare puzzle variable which contains the sudoku puzzle
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    print("\nPUZZLE_______________")
    print_sudoku(puzzle)

    # call solve function to provide the solution          
    print("\nSOLUTION_____________")
    solved = solve_sudoku(puzzle)
    print_sudoku(solved)