#!/usr/bin/python3

"""Will print the alphabet in lowercase, not followed by a new line."""

for i in range(26):
    print('{:c}'.format(97 + i), end="")
