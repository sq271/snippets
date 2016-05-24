#!/usr/bin/python

# prime.py

def prime(x):
    a = True
    for i in range(2, x):
        if x % i == 0:
            a = False

    return(a)


def primegen(x):
    for i in range(1, x):
        if prime(i) == True:
            print(i)


primegen(10000000000000)


