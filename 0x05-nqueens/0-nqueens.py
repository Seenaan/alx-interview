#!/usr/bin/python3
import sys

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def is_safe(queens, row, col):
    for r, c in queens:
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def backtrack(n, row, queens, solutions):
    if row == n:
        solutions.append(queens.copy())
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append((row, col))  # Place the queen
            backtrack(n, row + 1, queens, solutions)  # Recur for the next row
            queens.pop()  # Remove the queen and backtrack

def nqueens(n):
    solutions = []
    backtrack(n, 0, [], solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
