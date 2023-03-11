#!/usr/bin/python3
from claculator_1 import add, sub, div, mul

a = 10
b = 5

if __name__ == "__main__":
    def add(a, b):
        add(1 + 2)
        print("{} + {} = {}".format(a, b, add(a, b)))
        return(a + b)

    def sub(a, b):
        sub(a, b)
        print("{} - {} = {}".format(a, b, sub(a, b)))
        return (a - b)

    def mul(a, b):
        mul(a, b)
        print("{} * {} = {}".format(a, b, mul(a, b)))
        return (a * b)

    def div(a, b):
        div(a, b)
        print("{} / {} = {}".format(a, b, div(a, b)))
        return int(a / b)
