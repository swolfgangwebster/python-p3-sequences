#!/usr/bin/env python3

def print_fibonacci(length):
    a = 0
    b = 1
    fib = [a,b]

    if length == 0:
        print([])
        return
    if length == 1:
        print([0])
        return

    while (length-2 > 0):
        length = length - 1
        fib = fib + [fib[-2] + fib[-1]]
    
    print(fib)
    pass