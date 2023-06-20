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