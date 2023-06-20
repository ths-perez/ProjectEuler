"""DEFINITION
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1**2+2**2+...+10**2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 
3025-385=2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

"""
import time
print("Starting Process")
ts = time.time()


#Get goal
goal = 100
sumSquare = 0
squareSum = 0
for i in range(1, goal + 1):
   sumSquare += i**2
   squareSum += i
sol = abs(squareSum ** 2 - sumSquare)

ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("dif is :", sol)