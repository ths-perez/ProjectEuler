"""DEFINITION
https://projecteuler.net/problem=8
The four adjacent digits in the 1000-digit number that have the 
greatest product are 9 x 9 x 8 x 9 =5832.

Find the thirteen adjacent digits in the 1000-digit number that 
have the greatest product. What is the value of this product?
"""
import time
import Tools

print("Starting Process")
ts = time.time()

iMax = 2_000_000

print("Sum is :",sum(Tools.GetPrimeList(iMax)))

ts = time.time() - ts
print("Time Elapsed :",ts,"s")

print(Tools.GetPrimeList(35))