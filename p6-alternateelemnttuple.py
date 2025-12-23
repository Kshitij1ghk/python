# for alternate values in atuple
t=(10,20,30,40,50)
def f(t):
    for i in range(0,len(t),2):
        print(t[i])
        i+=2
f(t)
# for max and min in alist
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

# using reccursions 
l=[]
n=int(input())
for i in range(n):
    l.append(input())
t=tuple(l)
print(t)
def rev(t):
    if len(t)==0:
        return
    print(t[0])
    rev(t[2:])
rev(t)
# here rev(t[2:]) creates new tuple starting from index 2 and then prints 
#value at index 0 and then calls rev(t[2:]) again