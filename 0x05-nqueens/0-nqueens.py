#!/usr/bin/python3
"""Module: 0-nqueens"""


def nqueens(
        n,
        row=0,
        columns=set(), left_diagonals=set(), right_diagonals=set(), board=[]
):
    """Placing N non-attacking queens on NxN chessboard"""
    if row >= n:
        # If we've placed all queens
        # add the current board configuration to the result
        print(board)
        return board

    solutions = []  # This will store all valid board configurations

    for col in range(n):
        l, r = row - col, row + col

        # Skip this column if it places a queen in an attacked position
        if col in columns or l in left_diagonals or r in right_diagonals:
            continue

        # Add this position to the sets to mark it as attacked
        columns.add(col)
        left_diagonals.add(l)
        right_diagonals.add(r)
        # Track the queen's column position for this row
        board.append([row, col])

        # Recur for the next row and add any solutions found
        solutions.extend(nqueens(
            n, row + 1, columns, left_diagonals, right_diagonals, board)
        )
        # Remove the current position from the attack sets and board
        columns.remove(col)
        left_diagonals.remove(l)
        right_diagonals.remove(r)
        board.pop()

    return solutions  # Return all solutions found for this configuration


if __name__ == '__main__':
    from sys import argv
    try:
        if len(argv) == 2:
            n = int(argv[1])
            if n < 4:
                print('N must be at least 4')
            else:
                nqueens(n)
        else:
            print('Usage: nqueens N')
    except ValueError:
        print('N must be a number')
