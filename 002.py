# Project Euler #2
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum
# of the even-valued terms.

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

i, s = 0, 0
while True:
    i = i + 3
    f = fib(i)
    if f < 4000000:
        s = s + f
    else:
        print(s)
        break

