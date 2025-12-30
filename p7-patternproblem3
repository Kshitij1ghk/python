#problem 3
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

# problem 4
for i in range(n): 
    for j in range(n):
        print(i,end=" ")
        i=i+1
    print() # solved by me btw so i startss from 0 and then goes into the next for loop with 0 itself and 
    #in j loop it goes from 0 to n-1 and then prints i for each j but i is getting updated in j lopp with increment of +1 so it 
    # prints as 0 1 2 3 4 and then we go into the first loop i where now its range gets updated to 1 and then j loop goes from 
    # 0 to n-1 and then prints i for each j but i is getting updated in j lopp with increment of +1 so it prints as 1 2 3 4 5 and 
    # then we go into the first loop i where now its range gets updated to 2 and then j loop goes from 0 to n-1 and then prints 
    # i for each j but i is getting updated in j lopp with increment of +1 so it prints as 2 3 4 5 6 and so on


# another way to do it is that the o/p in problem 4 is baiscally i+j
for i in range(0,n+1):
    for j in range(0,n+1):
        print(i+j,end=' ')
    print()
    # here we apply the logic of i+j as with sum of row + column to get same o/p as above 
    # | i | j values  | Output    |
    # - | --------- | --------- |
    # 0 | 0 1 2 3 4 | 0 1 2 3 4 |
    # 1 | 0 1 2 3 4 | 1 2 3 4 5 |
    # 2 | 0 1 2 3 4 | 2 3 4 5 6 | 
    # mor preferrable since it causes less bugs
    # why?
    #i is controlled by range(n)
    #Python decides the value of i
    #i is not your variable — it belongs to the loop.
    



