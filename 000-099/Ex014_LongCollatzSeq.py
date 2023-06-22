"""DEFINITION
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 
1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
import ToolBox
import numpy as np

print("Starting Process")
ts = time.time()

nMax = 1_000_000

l = [True for i in range(nMax+1)] #create map table to not calculate everything

max_chain_leng = 0
max_chain_starting_number = 0
###CODE HERE
for i in range(nMax-1,1,-1): #for each in array
    chain_leng = 0
    val = i
    if (l[val]):
        while val != 1:
            if val <= nMax:
                l[val] = False #memo
            chain_leng +=1
            if (val%2==0):
                val=int(val/2)
            else:
                val = val * 3 + 1
    if(chain_leng>= max_chain_leng):
        max_chain_starting_number = i
        max_chain_leng = chain_leng

                       
ts = time.time() - ts
print("Longest chain is ", max_chain_leng)
print("Starting with ", max_chain_starting_number)
print("Time Elapsed :",ts,"s")

