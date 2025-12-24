
#1 square pattern
# write pyhton code to print square pattern with the given character
n=int(input())
char=input()
for i in range(n):
    for j in range(n):
        print(char,end=' ')
    print() # for going to next loop with new line
# problem 2
for i in range(1,n+1):
    for j in range(n):
        print(i,end=' ')
    print()