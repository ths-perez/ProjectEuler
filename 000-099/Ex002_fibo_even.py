"""DEFINITION
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1,2,3,5,8,13,21,34,55,89
By considering the terms in the Fibonacci sequence whose values do not 
exceed four million, find the sum of the even-valued terms.
"""
import time

print("Starting Process")
ts = time.time()

n_minus2 = 0 # n-2
n_minus1 = 1 # n-1
n = 0
sol= 0
ValMax = 4000000 # maximum value
while n < ValMax:
    n = n_minus1 + n_minus2
    if (n%2==0):
        sol += n    
    n_minus2 = n_minus1
    n_minus1 = n

ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("The sum of the even-valued terms in the fib seq under 4 millions is", sol)