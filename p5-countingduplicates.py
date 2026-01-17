l=list()
status=[]
n=int(input("enter the no of list numbers"))
for i in range(n):
    l.append(int(input()))
    status.append(0)
count=0
print("elements of list=",l)
print("status list =",status)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if status[j]==0:
            if l[i]==l[j]:
                count=count+1
                status[j]=1
print("status list=",status)
print("count of duplicates=",count)

# how the above code works 
#it counts the duplicates in the list
# and it uses a status list to keep track of the duplicates
# if the element is already visited then it is marked as 1
# using a status list to avoid counting the same duplicate more than once.
# if the element is not visited then it is marked as 0
