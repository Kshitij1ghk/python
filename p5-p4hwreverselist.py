l=[]
n=int(input("enter the no of list numbers"))
for i in range(n):
    l.append(int(input()))
print("list=",l)
b=[]
for item in l:
    b=[item]+b
print(b)
# the code works as follows
# for ex l=[10,20,30,40,50]
# iteration 1 - item = 10
# b = [10] + []
# b = [10]
# iteration 2 - item = 20
# b = [20] + [10]
# b = [20,10] and so on

# using a while loop 
list=[]
n=int(input("enter the no of list numbers"))
for i in range(n):
    list.append(int(input()))
print("list=",list)
reversed_a=[]
i=len(list)-1 # start from last index
# loop until we rech new index
while i>=0:
    reversed_a.append(list[i])  # add eleemnent to the new list
    i=i-1 # move to previous index

print(reversed_a)

# using a stack 
a = [1, 2, 3, 4, 5]

stack = []

# Push each element to the stack
for item in a:
    stack.append(item)

reversed_a = []

# Pop elements from the stack and add to the new list
while stack:
    reversed_a.append(stack.pop())  # pop from stack and append to reversed_a

print(reversed_a)

#inbuilt method
list=[10,20,30,40,50,60]
list.reverse()
print(list)

#method 2
list=[10,20,30,40,50,60]
print(list[: :-1])
#start = None → start from the end (because step is negative)
#stop = None → go till the beginning
#step = -1 → move backward

# method 3
l=[0,20,30,40,50,60]
i,j=0,len(l)-1
while i<j:
    l[i]=l[i]+l[j]
    l[j]=l[i]-l[j]
    l[i]=l[i]-l[j]
    i+=1
    j-=1
print(l)

# in this method we are using the concept of swaping
# we are adding the first and last element and then subtracting the first element from the sum and then subtracting the last element from the sum
# then we are adding the second and second last element and then subtracting the second element from the sum and then subtracting the second last element from the sum
# and so on
#for ex l[0]=0 l[5]=60 
#l[0]=l[0]+l[5]=60
#l[5]=l[0]-l[5]=0
#l[0]=l[0]-l[5]=60


