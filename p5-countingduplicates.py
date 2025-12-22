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