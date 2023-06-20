""" DEFINITION
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are 
  multiples of 3 or 5, we get 3,5,6 and 9. 
  The sum of these multiples is 23

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

print("Starting Process")
ts = time.time()
#set the max value to the target
ValMax = 1000
tot = 0
for i in range(3,ValMax):
    #iterate 3..999
    #--if multiple of 3, sum the number
    if(i%3==0):
        tot +=i
    #-- else if multiple of 5
    elif (i%5==0):
        tot +=i

ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("The sum of all the multiples of 3 or 5 below ",ValMax, "is", tot)