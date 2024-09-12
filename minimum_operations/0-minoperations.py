#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the minimum number of operations required to reach a string of length n.

    The operations allowed are:
    - Append a character to the end of the string (cost: 1 operation)
    - Copy the entire string and append it to the end (cost: 1 operation)

    Args:
        n (int): The length of the target string.

    Returns:
        int: The minimum number of operations required to reach a string of length n.

    """
    operations = 0
    current_chars = 1
    while current_chars < n:
        if current_chars * 2 > n:
            operations += n - current_chars
            break
        else:
            operations += 1
            current_chars *= 2
    return operations if current_chars == n else 0
