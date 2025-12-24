l=[10,20,30,[40,50,[60,70],80],90,100]
def f(l):
    sum=0
    for i in l:
        if type(i) is list:
            sum=sum+f(i)
        else:
            sum=sum+i
    return sum
print(f(l))
print(l[3][2][0])