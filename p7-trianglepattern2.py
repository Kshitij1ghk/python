# problem 2 we have to use same logic as previous printing patterns here by rinting column numbers 
n=int(input("enter your number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
# another method 
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
    #Your method creates a counting pattern across columns, while the other method repeats the row number.
    # Both are valid patterns, just serving different purposes!