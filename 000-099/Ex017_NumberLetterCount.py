"""DEFINITION
https://projecteuler.net/problem=17

If the numbers 1 to 5
 are written out in words:
    one, two, three, four, five, 
then there are 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?


 NOTE: Do not count spaces or hyphens.
 For example, 
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

"""
#IMPORT HERE
import time;

#DEFINITION HERE
START = 1
END = 1000
l_unit = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
#one two three four five six seven eight nine ....
l_dec = [6,6,5,5,5,7,6,6] 
#twenty thirty forty, ...
l_hund = 7 #hundred
l_t = 8
tot = 0
ts = time.time()
def GetTotal(n):
    if n == 1:
        return 0
    t = 3
    modH = int(n/100)
    #1-99 
    t += modH*(sum(l_unit) +10*sum(l_dec) + 8*(sum(l_unit[:9])))
    
    for i in range(modH-1):
        t += (99 * (l_unit[i] + l_hund + 3) + (l_unit[i] + l_hund))
    if (n == 1000):
        t+= l_t
    return t

###CODE HERE
                

tot = GetTotal(END) - GetTotal(START)

ts = time.time() - ts
print(tot)
print("Time Elapsed :",ts,"s")

