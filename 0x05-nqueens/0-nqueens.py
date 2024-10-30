#!/usr/bin/python3
import sys

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def is_not_under_attack(row, col, queens):
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def place_queen(row, n, queens, solutions):
    if row == n:
        solutions.append(queens.copy())
        return

    for col in range(n):
        if is_not_under_attack(row, col, queens):
            queens.append((row, col))
            place_queen(row + 1, n, queens, solutions)
            queens.pop()

def n_queens(n):
    solutions = []
    place_queen(0, n, [], solutions)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = n_queens(n)
    print_solutions(solutions)
