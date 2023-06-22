"""DEFINITION
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?
"""
import time
import ToolBox
import numpy as np
print("Starting Process")
ts = time.time()

#list primes from 2 to number
Primes = [2,3,5,7,11,13,17,19]
#number of max tim primes are used
divisors = [0 for x in range(len(Primes))]

#iterate 2->20
for i in range(2,21):
    # if primes, increment by one
    if i in Primes:
        divisors[Primes.index(i)] += 1
    else:
        #else find all divisors (18->2,3,3)
        n = i
        iterator = 0
        div = [0 for x in range(len(Primes))]
        while n != 1:
            p = Primes[iterator]
            if n%p == 0:
                n/=p
                div[Primes.index(p)] += 1
            else:
                iterator +=1
        #merge the maximum between the global list and the actual computed list
        divisors = np.c_[divisors,div].max(axis=1)
result = 1
for i in range(len(Primes)):
    result*= Primes[i]**divisors[i]
ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print(result)