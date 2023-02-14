arr=[2,3,5,4,5,3,4,2,8]
new=[]
old=[]
for i in range(len(arr)):
    
        if arr[i] in new:
            old.append(arr[i])
        else:
            new.append(arr[i])    
for i in range(len(new)):
    if new[i] not in old:
        print(new[i])


# print(new,old)            
'''
EXOR:^
a^a=0
a^0=a



'''