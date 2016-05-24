#!/usr/bin/python

# fibonacci.py

def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        print(a + b)

fib()


