"""DEFINITION
https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
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

