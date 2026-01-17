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
# in this method we loop through the string and print the string until we get a space
# if we get a space then we print a new line
# we use end="" to print the string in the same line

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
#in this method we loop through the string and print the string until we get a space
# if we get a space then we print the string and reset the string to ""
# after resetting the string we loop through the string again and print the string until we get a space