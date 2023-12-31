"""DEFINITION
https://projecteuler.net/problem=10
The sum of the primes below 10 is 
2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million.

"""
import time
import ToolBox

print("Starting Process")
ts = time.time()

iMax = 2_000_000

print("Sum is :",sum(ToolBox.GetPrimeList(iMax)))

ts = time.time() - ts
print("Time Elapsed :",ts,"s")