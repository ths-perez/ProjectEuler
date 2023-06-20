"""DEFINITION
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

this methode works for small number but is slow af. could be better ;)
"""
import time

print("Starting Process")
ts = time.time()

PrimeList = [] #empty list
Goal = 600851475143
memGoal = Goal
LastPrime = 2
while Goal > LastPrime:
    #starting from two
    # then keep dividing if the rest is 0
    if(Goal%LastPrime==0):
        PrimeList.append(LastPrime)
        Goal/=LastPrime
    else:
    # else, increase number by one
        LastPrime+=1
PrimeList.append(LastPrime)

print("DenomFactor:")
print(PrimeList)
print("Biggest", LastPrime)

ts = time.time() - ts
print("Time Elapsed :",ts,"s")
print("What is the largest prime factor of the number 600851475143 is", LastPrime)