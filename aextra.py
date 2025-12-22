list=[1,2,1,2,3,1,2,3,1,2,1,1,2,3]
dupli_count=0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            dupli_count+=1
        else:
            continue
print(dupli_count)
