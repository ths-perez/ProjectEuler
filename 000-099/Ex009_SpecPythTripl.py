"""DEFINITION
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, 
a < b < c, 
for which,
a**2 +b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.
Find the product abc.

"""
import time
import math as m
print("Starting Process")
ts = time.time()

def Solve(goal):
   ab_max = int(goal/2)
   triplets = []
   for a in range(ab_max):
      a2 = a**2
      for b in range (a+1,ab_max):
         b2 = b**2
         c = m.sqrt(a2 + b2)
         if int(c) == c:
            if a + b + c == goal:
               return a, b, c
   return 0,0,0

a,b,c = Solve(1000)
ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("Sol: ",(a*b*c))
print(" a:",a)
print(" b:",b)
print(" c:",c)