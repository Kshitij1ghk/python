#rotate the given list by k positions

#1.my method
k=int(input("by how much you want to rotate the list"))
list=[10,20,30,40,50,60]
temp=[]

#store first k elements
for i in range(k):
    temp.append(list[i])
    
#remove first k elements
for i in range(k):
    list.pop(0)

# add stored elements at the end 
list.extend(temp)

print(list)

#2.inbuilt method
k=int(input("by how much you want to rotate the list"))
list=[10,20,30,40,50,60]
print(list[k:]+list[:k])

# This method rotates the list using slicing (no loops needed)
# list[k:]  → elements from index k to the end
# list[:k]  → elements from index 0 to index k-1
# By adding them, we first take elements from k to end
# and then append the first k elements at the end
# This results in a left rotation by k positions

#3.sir's method
l=[]
n=int(input("enter list numbers:"))
for i in range(n):
    l.append(int(input()))
print("list=",l)
k=int(input())
for i in range(k):
    value=l[0]
    l.remove(l[0])
    l.append(value)
print(l)
    
