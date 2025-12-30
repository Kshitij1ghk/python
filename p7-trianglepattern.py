# problem 1 of triangle pattern my method
n=int(input())
char=input()
for i in range(n):
    for j in range(n):
        if i>=j:
            print(char,end=' ')
    print() 

    # another way to solve this
for i in range(n):
    for j in range(i+1):
        print(char,end=' ')
    print()
#The second method is more efficient because it only loops as many times
# as needed, while yours checks every position but skips some with the condition. For small values of n this 
# doesn't matter much, but for large n, the second approach does roughly half the work!
#first method has iterations n^2 times while second method has iterations n^2/2 times 