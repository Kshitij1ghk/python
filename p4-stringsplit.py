#write a python code to display given string separated by each word
# check how split works from notes
sent=str(input('enter your sentence'))
for i in sent.split():
    print(i)
words=sent.split()
print(words)

# another method for above code without using inbuilt method
string=input("enter your sentence:")
n=len(string)
for i in range(0,n):
    if(string[i]!=" "):
        print(string[i],end="")
    else:
        print()
# another method by me 
string=input("enter your sentence")
sum=""
for i in string:
    if i!=" ":
        sum+=i
    else:
        print(sum)
        sum=""
if sum:
    print(sum)