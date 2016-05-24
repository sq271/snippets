#!/usr/bin/python

# fibonocciupto.py

def fib(x):
    num = 0
    a, b = 0, 1
    while num < x:
        a, b = b, a + b
        print(a + b)
        num += 1

fib(1200)




