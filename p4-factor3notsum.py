# sume of all numbers till n except factorial of 3
n=int(input("enter your number"))
factor3_sum=0
for i in range(1,n+1):
    if i%3==0:
        continue
    factor3_sum=factor3_sum+i
print(factor3_sum)
