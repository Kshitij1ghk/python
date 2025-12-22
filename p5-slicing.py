l=list()
n=int(input("no of elements in list:"))
for i in range(n):
    l.append(int(input()))
l1=l[0::2]
print(l1)
l2=l[::-1]
l2=l2[::3]
print(l2)
l3=l[n//2::1]
print(l3)
sum1=0
sum2=0
sum3=0
for i in range(len(l1)):
    sum1+=l1[i]
print(sum1)
for i in range(len(l2)):
    sum2+=l2[i]
print(sum2)
for i in range(len(l3)):
    sum3+=l3[i]
print(sum3)
average=(sum1+sum2+sum3)/3
print("the average of all sublists is: ",average)

# aother way to do this code is 