print('hello','how','are','you',sep='#',end='@');
print('hello world');
# AS YOU CAN SEE SINCE DEFAULT OF VALUE OF \n IS CHANGED TO @ the next print statement will start from @ as observed
print('hello','how','are','you',sep=None,end=None);

print('x={:7d},y={:4d}'.format(5,3));
#7d represents that the width of the field is 7 or minimum seven that is why there are 6 spaces before 5 and by default right alignment is done
print('x={:5d},y={:4d}'.format(234567,32));
# here we took 5d and took more integer than 5 so it will print the integer as it is 

print('x={:5d},y={:4d}'.format(True,False));

# print('x={:5d},y={:4d}'.format('braintabs','pwlive'));
#gives value error since we are trying to print string in integer format

