"""DEFINITION
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
import Tools
print("Starting Process")
ts = time.time()

yMax = 999
yMin = 100
xMax = 999
xMin = 100

PalFound = 0 #mem
resx=0 #mem
resy=0 #mem

for y in range(yMax, yMin ,-1):
    for x in range(xMax,xMin,-1):
        res = x*y #store result
        #compare with mem
        if PalFound > res:
            # if temp is lower, no need to stay in x loop
            break 
        elif (Tools.IsPalNum(res)):
            #res is bigger than stored pal and is pal -> store it
            PalFound = res
            resx=x
            resy=y
            #pal found no need to stay in loop
            break



ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("RESULT: ",PalFound,"=",resx,"*",resy,"")