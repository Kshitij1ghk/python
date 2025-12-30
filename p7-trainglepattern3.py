n=int(input("enter your umber"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()

# another method 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()