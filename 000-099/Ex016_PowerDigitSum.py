"""DEFINITION
https://projecteuler.net/problem=16

2**15 = 32768  and the sum of its digits is 26.

What is the sum of the digits of the number 2**1000
?
"""
import time;
ts = time.time()

#DEFINITION HERE
l = []
p = 1000
r = 0

###CODE HERE
r = (2**p)
l = list(map(int, str(r)))
p = sum(l)

ts = time.time() - ts

print("Sol :", p)
print("Time Elapsed :",ts,"s")

