n=int(input())
a=0
b=1
evensum=0
oddsum=0
while a<=n:
    evensum+=a
    a=a+2
while b<=n:
    oddsum+=b
    b=b+2
if evensum>=oddsum:
    print(evensum-oddsum)
else:
    print(oddsum-evensum)

# another method is by using the bit wise operator
n=int(input())
evensum=0
oddsum=0
while n>=1:
    if n&1==1:
        oddsum+=n
    else:
        evensum+=n
    n=n-1
if evensum>=oddsum:
    print(evensum-oddsum);
else:
    print(oddsum-evensum)