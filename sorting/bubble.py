def bubble(list):
    flag=False
    for i in range(len(list)-1):
        for j in range(i,len(list)-i-1):
            if list[j]>list[j+1]:
                flag=True
                list[j],list[j+1]=list[j+1],list[j]
        if flag==False:
            return list
    return list

def bubbleRec(list,length):
    if length==1:
        return list
    for i in range(length-1):
        if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    ans=bubbleRec(list,length-1)
    return ans


list=[2,5,3,2,5,3,9,4]
print(bubbleRec(list,len(list)))
print(bubble(list))