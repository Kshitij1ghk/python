# python code to find lcm of given numbers in the list
# first we write the gcd logic since lcm(a,b) = (a*b)/gcd(a,b)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b) # uses // since lcm must be integer 

# applying the logic in a recursive list 
l=[3,6,9,12]
def f(l):
    if len(l)==1:
        return l[0]
    else:
        return lcm(l[0],f(l[1:]))
print(f(l))

# inbuilt method to find lcm of given numbers in the list
import math
l=[3,6,9,12]
def f(l):
    return math.lcm(*l)
print(f(l))
# what *l means its called argument unpacking
# for ex her l=[3,6,9,12]
# then *l expands to 3,6,9,12
# then math.lcm(3,6,9,12) is called
# the it returns the lcm of 3,6,9,12
# like the above method
