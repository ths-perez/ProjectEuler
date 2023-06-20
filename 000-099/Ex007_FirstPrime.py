"""DEFINITION
https://projecteuler.net/problem=7

By listing the first six prime numbers:
2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import time
print("Starting Process")
ts = time.time()

lastPrime= 0
primelist = [2]

numStop = 10001
it = 1
x = 3
while it < numStop:
   if x > 1:
      # check for factors
      for i in primelist:
         if (x % i) == 0:
            break
      else:
         primelist.append(x)
         lastPrime = x
         it+=1
   x+=2 #two by two

         
ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("last prime :", lastPrime)
print("nb Prime:", len(primelist))
