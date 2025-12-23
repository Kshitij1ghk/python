t=(10,20,30,40,50)
def f(t):
    for i in range(0,len(t),2):
        print(t[i])
        i+=2
f(t)
l=[10,20,30,40,50,60]

def max_min(l):
    max=l[0]
    min=l[0]
    for i in range(len(l)):
        if l[i]<min:
            min=l[i]
        if l[i]>max:
            max=l[i]
    return min,max
min,max=max_min(l)
print("the minimum number is :",min)
print("the maximum number is :",max)