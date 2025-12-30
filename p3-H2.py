#write a python code to find absolute difference between sum of even numbers and sum of odd numbers uto given n value
n=int(input('enter the value of n'))
sum_even,sum_odd=0,0
for i in range(1,n+1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print('absolute difference between sum of even numbers and sum of odd numbers is',abs(sum_even-sum_odd))
#range works as follows in python range(start,stop,step)
# for the above code range Start: 1 - begins at 1
# Stop: n+1 - stops before n+1 (meaning it includes n)
# Step: Not specified, so defaults to 1

# another way to write the above code is
b=int(input('enter the value of number'))
even_sum,odd_sum=0,0
while b>=1:
    if(b%2==0):
        even_sum+=b
    else:
        odd_sum+=b
    b=b-1
if even_sum>=odd_sum:
    print('absolute difference between sum of even numbers and sum of odd numbers is',even_sum-odd_sum)
else:
    print('absolute difference between sum of even numbers and sum of odd numbers is',odd_sum-even_sum)


#write a python code to display given string speerated by each word
y=int(input('enter the value of n'))
for i in range(1,y+1,2):
    print(i)
#range(start,stop,step)
# for the above code range Start: 1 - begins at 1
# Stop: y+1 - stops before y+1 (meaning it includes y)
# Step: 2 - increments by 2 each time
# DEfault value for step is 1 that is increment by 1


#write a python code to check if a number is prime or not
prime=int(input())
if prime==1:
    print('number is not prime')
else:
    for i in range(2,prime):
        if prime%i==0:
            print('number is not prime')
            break
    else:
        print("number is prime ")

# sum of all prime numbers till the input number
n=int(input("enter your number"))
prime_sum=0
while n>1:
    count=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            count+=1
    if count==0:
        prime_sum+=n
    n=n-1
print(prime_sum)



        