#!/usr/bin/python3
for i in reversed(range(0, 26)):
    if i % 2 == 1:
        val = 97 + i
    else:
        val = 65 + i
    print('{:c}'.format(val), end="")
