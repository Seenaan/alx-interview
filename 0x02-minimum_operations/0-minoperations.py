#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0

    # Initialize the list to store the minimum operations for each number
    min_ops = [float('inf')] * (n + 1)
    min_ops[1] = 0  # Base case: 0 operations to have 1 `H`

    # Compute minimum operations for each number from 2 to n
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:  # `j` is a factor of `i`
                # Update the minimum operations for `i` using the factor `j`
                min_ops[i] = min(min_ops[i], min_ops[j] + (i // j))
    
    return min_ops[n]

# Example usage:
print(minOperations(9))  # Output: 6
