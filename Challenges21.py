#Fibonacci

#In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each 
#number is the sum of the two preceding ones, starting from 0 and 1:

#The function fastFib(num) returns the fibonacci number Fn, of the given num as an argument.

#Examples
"""
fib_fast(5) ➞ 5

fib_fast(10) ➞ 55

fib_fast(20) ➞ 6765

fib_fast(50) ➞ 12586269025
"""
##Notes

#    The input number is always positive.


def fib_fast(num):
    fiblist = [0,1]
    for i in range(num + 1):
        if i !=  0 and i != 1:
            fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist[-1]