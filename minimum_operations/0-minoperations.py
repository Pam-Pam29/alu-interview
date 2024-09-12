#!/usr/bin/python3

def minOperations(n):
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
