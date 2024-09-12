#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in a file.

    Args:
        n (int): The number of H characters to achieve.

    Returns:
        int: The minimum number of operations required to reach n H characters.
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
