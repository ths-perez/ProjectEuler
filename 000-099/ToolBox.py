# get a number
# convert to string (char array)
# if string equals string revered, number is pal
def IsPalNum(num):
    s = str(num)
    return s == s[::-1]

# get a string
# convert to string (char array)
# if string equals string revered, number is pal
def IsPalString(string):
    return string == string[::-1]

#get prime list up to n
def GetPrimeList(n):
    CEIL = int(n/2)
    #init 2 by 2
    prime = [True for i in range(CEIL)]
    p = 1
    
    while(p*p <= n):      
        if (prime[p] == True):
            for i in range(p*2+1+p, CEIL, p*2+1):
                prime[i] = False
        p += 1

    PrimeList = [2]
    for p in range(1,len(prime)):
        if prime[p]:
            PrimeList.append(2*p+1)
    return PrimeList