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

# using recurrsion for min and max
l1=[12,7,5,25,31,10]
def maximum(list,max_element):
    if len(list)==1:
        return max_element
    if max_element<list[0]:
        max_element=list[0]
    return maximum(list[1:],max_element)
print(maximum(l1,l1[0]))
# Call 1: [12,7,5,25,31,10], max=12 → check 12, max=12 → recurse [7,5,25,31,10]
# Call 2: [7,5,25,31,10], max=12    → check 7, max=12  → recurse [5,25,31,10]
# Call 3: [5,25,31,10], max=12      → check 5, max=12  → recurse [25,31,10]
# Call 4: [25,31,10], max=12        → check 25, max=25 → recurse [31,10]
# Call 5: [31,10], max=25           → check 31, max=31 → recurse [10]
# Call 6: [10], max=31              → check 10, max=31 → recurse []
# NOW LEN OF LIST IS 1 SO RETURN MAX_ELEMENT
def minimum(list,min_element):
    if len(list)==1:
        return min_element
    if min_element>list[0]:
        min_element=list[0]
    return minimum(list[1:],min_element)
print(minimum(l1,l1[0]))
# this is for minimum element

# using reccursion for min and max
l2=[12,31,45,67,3,42]
def max(l,maximum_value):
    if len(l)==1:
        print("maximum value printed in recurrsive function is:",maximum_value)
        return maximum_value
    if maximum_value<l[1]:
        maximum_value=l[1]
    return max(l[1:],maximum_value)
def min(l,minimum_value):
    if len(l)==1:
        print("minimum value printed in recurrsive function is:",minimum_value)
        return minimum_value
    if minimum_value>l[1]:
        minimum_value=l[1]
    return min(l[1:],minimum_value)
print("values printed in print function is:",max(l2,l2[0]),min(l2,l2[0]))
# golden rule of reccursion is every recursivve call must return 
