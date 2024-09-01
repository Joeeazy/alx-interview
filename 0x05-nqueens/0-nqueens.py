#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

board_size = int(sys.argv[1])


def findQueenPositions(board_size, row=0, cols=[], diag1=[], diag2=[]):
    """ find Queen positions """
    if row < board_size:
        for col in range(board_size):
            if col not in cols and row + col not in diag1 and row - col not in diag2:
                yield from findQueenPositions(
                    board_size, row + 1, cols + [col], diag1 + [row + col], diag2 + [row - col]
                )
    else:
        yield cols


def nQueensSolver(board_size):
    """ solve n queens problem"""
    solutions = []
    row = 0
    for solution in findQueenPositions(board_size, 0):
        for col in solution:
            solutions.append([row, col])
            row += 1
        print(solutions)
        solutions = []
        row = 0


nQueensSolver(board_size)
