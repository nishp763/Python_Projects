def solve_sudoku(puzzle_list):
    print_sudoku(puzzle_list)

def print_sudoku(puzzle_list):
    row_count = 0 # tracks which row is being printed
    print() # print empty lne
    for row in puzzle_list: # iterate through row by row
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

    # call solve function to provide the solution          
    solve_sudoku(puzzle) 