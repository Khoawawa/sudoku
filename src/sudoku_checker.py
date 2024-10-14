def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    # Check 3x3 subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            subgrid = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not is_valid_group(subgrid):
                return False

    return True

def is_valid_group(group):
    group = [num for num in group if num != 0]  # Ignore empty cells (0)
    return len(group) == len(set(group))  # Ensure no duplicates